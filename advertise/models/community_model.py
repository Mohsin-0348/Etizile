from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# define local imports
from rnd.models import BaseAdvertise, Category


class Community(models.Model):
    """
        base community fields to be added
    """
    base_advertise = GenericRelation(BaseAdvertise)  # generate generic relation with BaseAdvertise model

    class Meta:
        """
            define the model as abstract
        """
        abstract = True


class CarLift(Community):
    """
        store extra information about car lift, inheritance with community fields
    """
    car_lift_from = models.CharField(max_length=32, blank=True, null=True)  # where the car may lift from
    car_lift_to = models.CharField(max_length=32, blank=True, null=True)  # where the car may lift to


class BasicCommunity(Community):
    """
        create basic model with community fields
    """
    pass


class PreLovedItems(Community):
    """
        store pre-loved items' information, inheritance with community fields
    """
    age = models.CharField(max_length=32, blank=True, null=True)  # store age of the product
    usage = models.CharField(max_length=32, blank=True, null=True)  # store how many time used
    condition = models.CharField(max_length=32)  # present condition of the product

    class Meta:
        """
            define the model as abstract
        """
        abstract = True


class BasicPreLovedItems(PreLovedItems):
    """
        create basic model with pre-loved items' information
    """
    pass


class JewelryAndWatches(PreLovedItems):
    """
        store jewelry and watches information, inheritance with pre-loved items' fields
    """
    amber = models.BooleanField(default=False)  # if material is amber
    beads = models.BooleanField(default=False)  # if material is beads
    bronze = models.BooleanField(default=False)  # if material is bronze
    ceramic = models.BooleanField(default=False)  # if material is ceramic
    crystal = models.BooleanField(default=False)  # if material is crystal
    cz = models.BooleanField(default=False)  # if material is cz
    diamond = models.BooleanField(default=False)  # if material is diamond
    gemstone = models.BooleanField(default=False)  # if material is gemstone
    leather = models.BooleanField(default=False)  # if material is leather
    plastic = models.BooleanField(default=False)  # if material is plastic
    platinum = models.BooleanField(default=False)  # if material is platinum
    rhinestones = models.BooleanField(default=False)  # if material is rhinestones
    rubber = models.BooleanField(default=False)  # if material is rubber
    semi_precious_or_birth_stones = models.BooleanField(default=False)  # if material is semi precious or birth stones
    shell_bone_coral = models.BooleanField(default=False)  # if material is shell bone coral
    silver = models.BooleanField(default=False)  # if material is silver
    steel = models.BooleanField(default=False)  # if material is steel
    titanium = models.BooleanField(default=False)  # if material is titanium
    white_gold = models.BooleanField(default=False)  # if material is white gold
    wood = models.BooleanField(default=False)  # if material is wood
    yellow_gold = models.BooleanField(default=False)  # if material is yellow gold
    other_material = models.BooleanField(default=False)  # if material is other material
    other_metal = models.BooleanField(default=False)  # if material is other metal
