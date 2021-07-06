from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from rnd.models import Category, BaseAdvertise
from advertise.choices import MobileChoice


class Electronics(models.Model):
    age = models.CharField(max_length=32, blank=True, null=True)
    usage = models.CharField(max_length=32, blank=True, null=True)
    condition = models.CharField(max_length=32)
    base_advertise = GenericRelation(BaseAdvertise)

    class Meta:
        abstract = True


class Computers(Electronics):
    brand = models.CharField(max_length=32)
    memory = models.CharField(max_length=32)
    processor_speed = models.CharField(max_length=32)
    hard_drive = models.CharField(max_length=32)
    warranty = models.CharField(max_length=32, blank=True, null=True)


class MobilePhones(Electronics):
    model = models.CharField(max_length=32, choices=MobileChoice.choices)
    memory = models.CharField(max_length=32, blank=True, null=True)
    color = models.CharField(max_length=32, blank=True, null=True)
    warranty = models.CharField(max_length=32, blank=True, null=True)


class BasicElectronics(Electronics):
    pass

