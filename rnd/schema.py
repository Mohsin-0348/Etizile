import graphene
from django.apps import apps
from graphql import GraphQLError
from graphql_auth import mutations
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required, superuser_required

from .models import City, Category, BaseAdvertise
from users.schema import UserType


class CategoryType(DjangoObjectType):

    class Meta:
        model = Category


class CategoryQuery(graphene.ObjectType):
    categories = graphene.List(CategoryType, id=graphene.Int())

    @login_required
    def resolve_categories(self, info, id=None, **kwargs):
        if id:
            # category = Category.objects.get(id=id)
            # categories = Category.objects.filter(parent__id=id)
            # return {'category': category, 'categories': categories}
            return Category.objects.filter(parent__id=id)
        return Category.objects.filter(parent__isnull=True)


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


class AdvertiseType(DjangoObjectType):

    class Meta:
        model = BaseAdvertise


class AdvertiseQuery(graphene.ObjectType):
    advertises = graphene.List(AdvertiseType)

    @superuser_required
    def resolve_advertises(self, info, **kwargs):
        return BaseAdvertise.objects.all()


class CreateAdvertise(graphene.Mutation):
    id = graphene.Int()
    city = graphene.Field(CityType)
    user = graphene.Field(UserType)
    category = graphene.Field(CategoryType)
    title = graphene.String()
    description = graphene.String()
    location = graphene.String()
    price = graphene.String()
    currency = graphene.String()

    class Arguments:
        city_id = graphene.Int()
        user_id = graphene.Int()
        category_id = graphene.Int()
        title = graphene.String()
        description = graphene.String()
        location = graphene.String()
        price = graphene.String()
        currency = graphene.String()

    @login_required
    def mutate(self, info, city_id, user_id, category_id, title, description, location, price=None, currency=None):
        user = info.context.user
        city = City.objects.get(id=city_id)
        category = Category.objects.get(id=category_id)
        category_model = apps.get_model(app_label='advertise', model_name=category.keyword)
        advertise = BaseAdvertise(city=city, user=user, category=category, title=title, description=description,
                                  location=location, price=price, currency=currency)
        print(advertise, category_model)
        # advertise.save()

        return CreateAdvertise(
            id=advertise.id, city=advertise.city, user=advertise.user, category=advertise.category,
            title=advertise.title, description=advertise.description, location=advertise.location,
            price=advertise.price, currency=advertise.currency
        )


class Query(CategoryQuery, CityQuery, AdvertiseQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_city = CreateCity.Field()

