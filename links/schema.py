import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(object):
    links = graphene.List(LinkType)

    def resolve_links(self, info):
        return Link.objects.all()
