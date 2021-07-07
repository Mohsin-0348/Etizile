from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.fields import GenericRelation

# define local imports
from rnd.models import Category, BaseAdvertise
from advertise.choices import ManufacturerChoice


class MotorPurposeChoice(models.TextChoices):
    """
        define selection fields for sale or rent
    """
    FOR_SALE = 'sale'
    FOR_RENT = 'rent'


class Motors(models.Model):
    """
        base electronics fields to be added
    """
    usage = models.CharField(max_length=64, blank=True, null=True)  # store how many time used
    base_advertise = GenericRelation(BaseAdvertise)  # generate generic relation with BaseAdvertise model

    class Meta:
        """
            define the model as abstract
        """
        abstract = True


class Car(Motors):
    """
        store extra information about car, inheritance with motors fields
    """
    purpose = models.CharField(max_length=16, choices=MotorPurposeChoice.choices)  # define wishing to sale or rent
    brand = models.CharField(max_length=64)  # store brand name of car
    model = models.CharField(max_length=64)  # store model name of car
    trim = models.CharField(max_length=64, blank=True, null=True)  # store trim information
    regional_specs = models.CharField(max_length=64)  # regional specification of the car
    body_condition = models.CharField(max_length=64)  # define body condition of car
    mechanic_condition = models.CharField(max_length=64)  # define mechanical condition of car
    year = models.PositiveIntegerField(blank=True, null=True)  # year of manufacture
    body_type = models.CharField(max_length=64, blank=True, null=True)  # define body type of car
    doors = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # how many doors car has
    mileage = models.PositiveIntegerField(blank=True, null=True)  # how many kilometer does the car run
    staring_side = models.CharField(max_length=64, blank=True, null=True)  # on which side the staring of car located
    fuel_type = models.CharField(max_length=64, blank=True, null=True)  # which type of fuel does the car need
    no_of_cylinder = models.CharField(max_length=32)  # how many cylinders car has
    horse_power = models.CharField(max_length=32)  # horse power of car
    transmission_type = models.CharField(max_length=32)  # transmission type of car
    insurance = models.CharField(max_length=64, blank=True, null=True)  # if car has insurance or not

    # extra information
    climate_control = models.BooleanField(default=False)  # if car has climate control or not
    cooled_seats = models.BooleanField(default=False)  # if car has cooled seats or not
    dvd_player = models.BooleanField(default=False)  # if car has dvd player or not
    front_heel_drive = models.BooleanField(default=False)  # if car has front heel drive or not
    keyless_entry = models.BooleanField(default=False)  # if car has keyless entry or not
    leather_seats = models.BooleanField(default=False)  # if car has leather seats or not
    navigation_system = models.BooleanField(default=False)  # if car has navigation system or not
    parking_sensors = models.BooleanField(default=False)  # if car has parking sensors or not
    premium_sound_system = models.BooleanField(default=False)  # if car has premium sound system or not
    rear_view_camera = models.BooleanField(default=False)  # if car has rear view camera or not


class MotorCycle(Motors):
    """
        store extra information about motor cycle, inheritance with motors fields
    """
    purpose = models.CharField(max_length=16, choices=MotorPurposeChoice.choices)  # define wishing to sale or rent
    condition = models.CharField(max_length=64, blank=True, null=True)  # define motor cycle condition
    mileage = models.PositiveIntegerField(blank=True, null=True)  # how many kilometer does the motor cycle run
    year = models.PositiveIntegerField(blank=True, null=True)  # year of manufacture
    final_drive_system = models.CharField(max_length=64, blank=True,
                                          null=True)  # define what final drive system it belongs
    wheels = models.CharField(max_length=64, blank=True, null=True)  # how many wheels the motor cycle has
    manufacturer = models.CharField(max_length=64, choices=ManufacturerChoice.choices, blank=True,
                                    null=True)  # manufacturer company of the motor cycle
    engine_size = models.CharField(max_length=64, blank=True, null=True)  # what is the engine size in cc
    warranty = models.CharField(max_length=64, blank=True, null=True)  # if motor cycle has warranty or not
    color = models.CharField(max_length=64, blank=True, null=True)  # color of the motor cycle


class MotorAccessoriesAndParts(Motors):
    condition = models.CharField(max_length=64, blank=True, null=True)  # define component present condition


class HeavyVehicles(Motors):
    """
        store extra information about motor cycle, inheritance with motors fields
    """
    purpose = models.CharField(max_length=16, choices=MotorPurposeChoice.choices)  # define wishing to sale or rent
    brand = models.CharField(max_length=64)  # store brand name of the vehicle
    model = models.CharField(max_length=64)  # store model name of the vehicle
    mileage = models.PositiveIntegerField(blank=True, null=True)  # how many kilometer does the vehicle run
    body_condition = models.CharField(max_length=64)  # define body condition
    mechanic_condition = models.CharField(max_length=64)  # define mechanical condition of vehicle
    year = models.PositiveIntegerField(blank=True, null=True)  # year of manufacture
    warranty = models.CharField(max_length=64, blank=True, null=True)  # if vehicle has warranty or not
    capacity_or_weight = models.CharField(max_length=64, blank=True, null=True)  # max capacity of the vehicle
    no_of_cylinder = models.CharField(max_length=32)  # how many cylinders vehicle has
    horse_power = models.CharField(max_length=32)  # horse power of vehicle
    fuel_type = models.CharField(max_length=64, blank=True, null=True)  # which type of fuel does the vehicle need


class BasicMotors(Motors):
    """
        create basic model with motors fields
    """
    pass

