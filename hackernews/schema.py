import graphene
import graphql_jwt

from links import schema as links_schema
from links import schema_relay as links_schema_relay
from users import schema as users_schema


class Query(
    links_schema.Query,
    links_schema_relay.RelayQuery,
    users_schema.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    links_schema.Mutation,
    links_schema_relay.RelayMutation,
    users_schema.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
