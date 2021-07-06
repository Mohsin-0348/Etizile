from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from .choices import CategoryKeywordChoice, CityChoice, RegionChoice, CurrencyChoice
from bases.models import BaseModel

User = get_user_model()


class City(models.Model):
    region = models.CharField(max_length=32, choices=RegionChoice.choices)
    city = models.CharField(max_length=32, choices=CityChoice.choices)

    def __str__(self):
        return f"{self.region}, {self.city}"

    class Meta:
        verbose_name_plural = 'Cities'
        unique_together = ('region', 'city')


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, related_name='parent_category', blank=True,
                               null=True)
    depth = models.PositiveIntegerField(default=0)
    keyword = models.CharField(max_length=64, default='None', choices=CategoryKeywordChoice.choices)

    def __str__(self):
        return self.name

    # def get_update_url(self):
    #     return reverse("categories", kwargs={"pk": self.id})

    class Meta:
        verbose_name_plural = 'Categories'


class BaseAdvertise(BaseModel):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='city_advertise', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="posted_user", blank=True,
                             null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='post_category', blank=True,
                                 null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=16, decimal_places=2)
    currency = models.CharField(max_length=5, choices=CurrencyChoice.choices, default=CurrencyChoice.BIRR)
    location = models.CharField(max_length=100, blank=True, null=False)
    availability = models.BooleanField(default=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return f"{self.category}: {self.title}"


class AdvertiseAttachment(models.Model):
    base = models.ForeignKey(BaseAdvertise, on_delete=models.DO_NOTHING, related_name='attachment_base')
    file = models.FileField(upload_to='advertise/attachment/')

# class Favourite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_favourite", blank=True,
#                              null=True)
#     category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='favourite_category', blank=True,
#                                  null=True)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
