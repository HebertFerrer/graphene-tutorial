import graphene

from links.models import Link


class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, **kwargs):
        link = Link.objects.create(**kwargs)
        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
        )


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
