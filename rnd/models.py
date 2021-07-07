from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from .choices import CategoryKeywordChoice, CityChoice, RegionChoice, CurrencyChoice
from bases.models import BaseModel

User = get_user_model()


class City(models.Model):
    """
        Store information of cities by region and city name
    """
    region = models.CharField(max_length=32, choices=RegionChoice.choices)  # store region name
    city = models.CharField(max_length=32, choices=CityChoice.choices)  # store city name

    def __str__(self):
        return f"{self.region}, {self.city}"

    class Meta:
        verbose_name_plural = 'Cities'
        unique_together = ('region', 'city')


class Category(models.Model):
    """
        Store category information by making a hierarchy of category and sub-category including depth
    """
    name = models.CharField(max_length=64, unique=True)  # uniquely define category
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, related_name='parent_category', blank=True,
                               null=True)  # define the category for any sub-category
    depth = models.PositiveIntegerField(default=0)  # define the level of hierarchy
    keyword = models.CharField(max_length=64, choices=CategoryKeywordChoice.choices)  # find the actual model-name of the category that belongs

    def __str__(self):
        return self.name

    # def get_update_url(self):
    #     return reverse("categories", kwargs={"pk": self.id})

    class Meta:
        verbose_name_plural = 'Categories'


class BaseAdvertise(BaseModel):
    """
        posting minimum required fields for advertising
    """
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='city_advertise', blank=True,
                             null=True)  # define a city for posting
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="posted_user", blank=True,
                             null=True)  # define the user who posted
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='post_category', blank=True,
                                 null=True)  # define the category of the post
    title = models.CharField(max_length=100)  # name of the advertise
    description = models.TextField()  # some details about the advertise
    price = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)  # store the value of the advertise
    currency = models.CharField(max_length=5, choices=CurrencyChoice.choices, blank=True, null=True,
                                default=CurrencyChoice.BIRR)  # define in which currency used for selling
    location = models.CharField(max_length=100, blank=True, null=False)  # location of the advertise
    availability = models.BooleanField(default=True)  # if it is available or not
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # store model information for other fields
    object_id = models.PositiveIntegerField()  # model object value
    content_object = GenericForeignKey()  # define that model as generic foreign key

    def __str__(self):
        return f"{self.category}: {self.title}"


class AdvertiseAttachment(models.Model):
    """
        store multiple attachment for advertising a post
    """
    base = models.ForeignKey(BaseAdvertise, on_delete=models.DO_NOTHING,
                             related_name='attachment_base')  # define reference model object
    file = models.FileField(upload_to='advertise/attachment/')  # store files


# class Favourite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_favourite", blank=True,
#                              null=True)
#     category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='favourite_category', blank=True,
#                                  null=True)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
