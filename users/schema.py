import graphene
from graphql import GraphQLError
from graphql_auth.schema import MeQuery, UserQuery
from graphql_auth import mutations
from graphene_django import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from django.contrib.auth import get_user_model


# class UserType(DjangoObjectType):
#     class Meta:
#         model = get_user_model()
#
#
# class CreateUser(graphene.Mutation):
#     user = graphene.Field(UserType)
#
#     class Arguments:
#         username = graphene.String(required=True)
#         email = graphene.String(required=True)
#         phone = graphene.Int(required=True)
#         password = graphene.String(required=True)
#
#     def mutate(self, info, username, password, email, phone):
#         user = get_user_model()(
#             username=username,
#             email=email,
#             phone=phone,
#         )
#         user.set_password(password)
#         user.save()
#
#         return CreateUser(user=user)


class AuthMutation(graphene.ObjectType):
    """
        defining mutation functions to be performed
    """
    # create_user = CreateUser.Field()
    register = mutations.Register.Field()  # registration of user
    verify_account = mutations.VerifyAccount.Field()  # verify user account
    resend_activation_email = mutations.ResendActivationEmail.Field()  # resend activation email for verify user account
    password_change = mutations.PasswordChange.Field()  # changing user password
    update_account = mutations.UpdateAccount.Field()  # update user account
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()  # send email for reset password
    password_reset = mutations.PasswordReset.Field()  # reset user password

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()  # generate token for user login


class Query(UserQuery, MeQuery, graphene.ObjectType):
    """
        pass all the queries together
    """
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    """
        pass all the mutations together
    """
    pass

