from graphene_django import DjangoObjectType
from links.models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link
