import graphene
from graphql import GraphQLError
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required, superuser_required

from .models import City, Category, BaseAdvertise


class CategoryType(DjangoObjectType):

    class Meta:
        model = Category


class CategoryQuery(graphene.ObjectType):
    categories = graphene.List(CategoryType, id=graphene.Int())

    @login_required
    def resolve_categories(self, info, id=None, **kwargs):
        if id:
            return Category.objects.filter(id=id)
        return Category.objects.all()


class CreateCategory(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    parent = graphene.Field(CategoryType)
    depth = graphene.Int()
    keyword = graphene.String()

    class Arguments:
        name = graphene.String()
        parent_id = graphene.Int()
        depth = graphene.Int()
        keyword = graphene.String()

    @superuser_required
    def mutate(self, info, name, parent_id, depth, keyword):
        if parent_id > 0:
            parent = Category.objects.get(id=parent_id)
        else:
            parent = None
        category = Category(name=name, parent=parent, depth=depth, keyword=keyword)
        category.save()

        return CreateCategory(id=category.id,
                              name=category.name,
                              parent=category.parent,
                              depth=category.depth,
                              keyword=category.keyword
                              )


class CityType(DjangoObjectType):

    class Meta:
        model = City


class CityQuery(graphene.ObjectType):
    cities = graphene.List(CityType)

    @login_required
    def resolve_cities(self, info, **kwargs):
        return City.objects.all()


class CreateCity(graphene.Mutation):
    id = graphene.Int()
    region = graphene.String()
    city = graphene.String()

    class Arguments:
        region = graphene.String()
        city = graphene.String()

    @superuser_required
    def mutate(self, info, city, region):
        city = City(region=region, city=city)
        city.save()

        return CreateCity(id=city.id,
                          region=city.region,
                          city=city.city
                          )


class Query(CategoryQuery, CityQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_city = CreateCity.Field()

