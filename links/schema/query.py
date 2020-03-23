import graphene
from graphene_django import DjangoObjectType

from links.schema.types import LinkType, VoteType
from links.models import Link, Vote


class Query(object):
    links = graphene.List(LinkType)
    votes = graphene.List(VoteType)

    def resolve_links(self, info):
        print("Si paso por aqui pidiendo directamente los votes")
        return Link.objects.all()

    def resolve_votes(self, info):
        return Vote.objects.select_related('user', 'link').all()
