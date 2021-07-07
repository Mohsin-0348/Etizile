import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, AbstractUser, UserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# ThirdParty Library Import
from easy_thumbnails.fields import ThumbnailerImageField
from django_countries.fields import CountryField

# Own Apps Files Import
from .choices import GenderChoices
from bases.models import BaseModel


class User(BaseModel, AbstractUser):
    """
        Store custom user information. all fields are common for all users.
    """
    email = models.EmailField(max_length=100, unique=True)  # unique email to perform email login and send alert mail.
    phone_code = models.CharField(max_length=5, blank=True, null=True)  # set user phone code
    phone = models.CharField(max_length=15, null=True, blank=True)  # store user phone number
    gender = models.CharField(max_length=8, choices=GenderChoices.choices, blank=True,
                              null=True)  # user gender specification.
    date_of_birth = models.DateField(blank=True, null=True)  # date of user birth.
    photo = ThumbnailerImageField(_('Profile Picture'), upload_to='profile_pictures/', blank=True,
                                  null=True)  # user photo.
    is_superuser = models.BooleanField(default=False)  # main man of this application.
    last_active_on = models.DateTimeField(null=True, blank=True)  # define last time of active.
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)  # define when account is created.
    deactivation_reason = models.TextField(null=True, blank=True)  # store account deactivation reason.
    nationality = CountryField(blank=True, null=True)  # store user country belongs to
    current_city = models.CharField(max_length=30, blank=True, null=True)  # store user current city
    carrier_level = models.CharField(max_length=20, blank=True, null=True)  # store user carrier level
    current_position = models.CharField(max_length=32, blank=True, null=True)  # store user current position
    current_company = models.CharField(max_length=32, blank=True, null=True)  # store user current company working on
    salary_expectations = models.CharField(max_length=32, blank=True, null=True)  # user salary expectations
    commitment = models.CharField(max_length=32, blank=True, null=True)  # if user have any commitment
    notice_period = models.CharField(max_length=32, blank=True, null=True)  # when to notice for job
    visa_status = models.CharField(max_length=32, blank=True, null=True)  # if user have visa or not
    highest_education = models.CharField(max_length=32, blank=True, null=True)  # user highest education achieved
    cv = models.FileField(upload_to="user/cv/", blank=True, null=True)  # if user have any cv attached
    is_deleted = models.BooleanField(default=False)  # if user account was deleted
    term_and_condition_accepted = models.BooleanField(default=False)  # if user accepted the terms and conditions
    privacy_policy_accepted = models.BooleanField(default=False)  # if user accepted the privacy policy

    # last login will provide by django abstract_user
    # password also provide by django abstract_user

    # objects = UserManager()  # define user manager

    """
        email assign as username because by default django auth use username and password.
        to login email and password we did it.
    """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]  # while creating account username is must.

    # class Meta:
    #     db_table = f"{settings.DB_PREFIX}_users"  # define database table name.

    """
        generate user full name by using user first name and last name.
    """
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username
