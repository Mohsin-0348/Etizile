from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# define local imports
from rnd.models import Category, BaseAdvertise
from advertise.choices import MobileChoice


class Electronics(models.Model):
    """
        base electronics fields to be added
    """
    age = models.CharField(max_length=32, blank=True, null=True)  # store age of the product
    usage = models.CharField(max_length=32, blank=True, null=True)  # store how many time used
    condition = models.CharField(max_length=32)  # present condition of the product
    base_advertise = GenericRelation(BaseAdvertise)  # generate generic relation with BaseAdvertise model

    class Meta:
        """
            define the model as abstract
        """
        abstract = True


class Computers(Electronics):
    """
        store extra information about computer, inheritance with electronics fields
    """
    brand = models.CharField(max_length=32)  # define brand of computer
    memory = models.CharField(max_length=32)  # define memory/RAM of computer
    processor_speed = models.CharField(max_length=32)  # which processor does computer belongs
    hard_drive = models.CharField(max_length=32)  # define storage of computer
    warranty = models.CharField(max_length=32, blank=True, null=True)  # if computer has warranty or not


class MobilePhones(Electronics):
    """
        store extra information about mobile phones, inheritance with electronics fields
    """
    model = models.CharField(max_length=32, choices=MobileChoice.choices)  # define model of mobile
    memory = models.CharField(max_length=32, blank=True, null=True)  # define storage of mobile
    color = models.CharField(max_length=32, blank=True, null=True)  # define color of the mobile
    warranty = models.CharField(max_length=32, blank=True, null=True)  # if mobile has warranty or not


class BasicElectronics(Electronics):
    """
        create basic model with electronics fields
    """
    pass

