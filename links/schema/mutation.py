import graphene

from django.shortcuts import get_object_or_404

from links.models import Link, Vote
from users.schema.types import UserType
from links.schema.types import LinkType, VoteType


class CreateLink(graphene.Mutation):
    link = graphene.Field(LinkType)

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, **kwargs):
        kwargs['posted_by'] = info.context.user or None
        link = Link.objects.create(**kwargs)
        return CreateLink(link=link)


class CreateVote(graphene.Mutation):
    vote = graphene.Field(VoteType)

    class Arguments:
        link_id = graphene.Int()

    def mutate(self, info, link_id):
        user = info.context.user
        if user.is_anonymous:
            return Exception('You must be logged in')
        link = get_object_or_404(Link, id=link_id)
        vote = Vote.objects.create(user=user, link=link)
        return CreateVote(vote=vote)


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()
