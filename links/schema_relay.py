import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Link, Vote


class LinkNode(DjangoObjectType):
    class Meta:
        model = Link
        filter_fields = ('url', 'description')
        interfaces = (graphene.relay.Node, )


class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote
        interfaces = (graphene.relay.Node, )


class RelayQuery(graphene.ObjectType):
    relay_link = graphene.relay.Node.Field(LinkNode)
    relay_links = DjangoFilterConnectionField(LinkNode)


class RelayCreateLink(graphene.relay.ClientIDMutation):
    link = graphene.Field(LinkNode)

    class Input:
        url = graphene.String()
        description = graphene.String()

    def mutate_and_get_payload(root, info, **kwargs):
        user = info.context.user
        kwargs['posted_by'] = user if not user.is_anonymous else None
        link = Link.objects.create(**kwargs)
        return RelayCreateLink(link=link)


class RelayMutation(graphene.AbstractType):
    relay_create_link = RelayCreateLink.Field()
