import graphene
from graphql import GraphQLError
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

import users.schema
import rnd.schema


class Query(users.schema.Query, rnd.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, rnd.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
