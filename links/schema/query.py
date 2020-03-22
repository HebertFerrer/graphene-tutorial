import graphene
from graphene_django import DjangoObjectType

from .types import LinkType

class Query(object):
    links = graphene.List(LinkType)

    def resolve_links(self, info):
        return Link.objects.all()
