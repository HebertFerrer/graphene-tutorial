import graphene

from django.contrib.auth import get_user_model

from .types import UserType


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    me = graphene.Field(UserType)


    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in')
        return user
