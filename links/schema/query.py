import graphene
from graphene_django import DjangoObjectType

from django.db.models import Q

from links.schema.types import LinkType, VoteType
from links.models import Link, Vote


class Query(object):
    links = graphene.List(LinkType, search=graphene.String())
    votes = graphene.List(VoteType)

    def resolve_links(self, info, search=None):
        if search:
            return Link.objects.filter(
                Q(url__icontains=search) |
                Q(description__icontains=search),
            )
        return Link.objects.all()

    def resolve_votes(self, info):
        return Vote.objects.select_related('user', 'link').all()
