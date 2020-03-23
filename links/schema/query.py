import graphene
from graphene_django import DjangoObjectType

from django.db.models import Q

from links.schema.types import LinkType, VoteType
from links.models import Link, Vote


class Query(object):
    links = graphene.List(
        LinkType,
        search=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int(),
    )
    votes = graphene.List(VoteType)

    def resolve_links(self, info, search=None, first=None, skip=None):
        qs = Link.objects.all()
        if search:
            qs.filter(
                Q(url__icontains=search) |
                Q(description__icontains=search),
            )
        if skip:
            qs = qs[skip:]
        if first:
            qs = qs[:first]
        return qs

    def resolve_votes(self, info):
        return Vote.objects.select_related('user', 'link').all()
