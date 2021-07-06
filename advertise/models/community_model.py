from django.db import models

from django.contrib.contenttypes.fields import GenericRelation

from rnd.models import BaseAdvertise, Category


class Community(models.Model):
    base_advertise = GenericRelation(BaseAdvertise)

    class Meta:
        abstract = True


class CarLift(Community):
    # for car lifting
    car_lift_from = models.CharField(max_length=32, blank=True, null=True)
    car_lift_to = models.CharField(max_length=32, blank=True, null=True)


class BasicCommunity(Community):
    pass


class PreLovedItems(Community):
    age = models.CharField(max_length=32, blank=True, null=True)
    usage = models.CharField(max_length=32, blank=True, null=True)
    condition = models.CharField(max_length=32)

    class Meta:
        abstract = True


class BasicPreLovedItems(PreLovedItems):
    pass


class JewelryAndWatches(PreLovedItems):
    # extra information
    amber = models.BooleanField(default=False)
    beads = models.BooleanField(default=False)
    bronze = models.BooleanField(default=False)
    ceramic = models.BooleanField(default=False)
    crystal = models.BooleanField(default=False)
    cz = models.BooleanField(default=False)
    diamond = models.BooleanField(default=False)
    gemstone = models.BooleanField(default=False)
    leather = models.BooleanField(default=False)
    plastic = models.BooleanField(default=False)
    platinum = models.BooleanField(default=False)
    rhinestones = models.BooleanField(default=False)
    rubber = models.BooleanField(default=False)
    semi_precious_or_birth_stones = models.BooleanField(default=False)
    shell_bone_coral = models.BooleanField(default=False)
    silver = models.BooleanField(default=False)
    steel = models.BooleanField(default=False)
    titanium = models.BooleanField(default=False)
    white_gold = models.BooleanField(default=False)
    wood = models.BooleanField(default=False)
    yellow_gold = models.BooleanField(default=False)
    other_material = models.BooleanField(default=False)
    other_metal = models.BooleanField(default=False)
