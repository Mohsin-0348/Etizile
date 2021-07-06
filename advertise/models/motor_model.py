from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.fields import GenericRelation

from rnd.models import Category, BaseAdvertise


class MotorPurposeChoice(models.TextChoices):
    FOR_SALE = 'sale'
    FOR_RENT = 'rent'


class Motors(models.Model):
    usage = models.CharField(max_length=64, blank=True, null=True)
    base_advertise = GenericRelation(BaseAdvertise)

    class Meta:
        abstract = True


class Car(Motors):
    purpose = models.CharField(max_length=16, choices=MotorPurposeChoice.choices)
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    trim = models.CharField(max_length=64, blank=True, null=True)
    regional_specs = models.CharField(max_length=64)
    body_condition = models.CharField(max_length=64)
    mechanic_condition = models.CharField(max_length=64)
    year = models.PositiveIntegerField(blank=True, null=True)
    body_type = models.CharField(max_length=64, blank=True, null=True)
    doors = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    mileage = models.PositiveIntegerField(blank=True, null=True)
    staring_side = models.CharField(max_length=64, blank=True, null=True)
    fuel_type = models.CharField(max_length=64, blank=True, null=True)
    no_of_cylinder = models.CharField(max_length=32)
    horse_power = models.CharField(max_length=32)
    transmission_type = models.CharField(max_length=32)
    insurance = models.CharField(max_length=64, blank=True, null=True)

    # extra information
    climate_control = models.BooleanField(default=False)
    cooled_seats = models.BooleanField(default=False)
    dvd_player = models.BooleanField(default=False)
    front_heel_drive = models.BooleanField(default=False)
    keyless_entry = models.BooleanField(default=False)
    leather_seats = models.BooleanField(default=False)
    navigation_system = models.BooleanField(default=False)
    parking_sensors = models.BooleanField(default=False)
    premium_sound_system = models.BooleanField(default=False)
    rear_view_camera = models.BooleanField(default=False)


class MotorCycle(Motors):
    purpose = models.CharField(max_length=16, choices=MotorPurposeChoice.choices)
    condition = models.CharField(max_length=64, blank=True, null=True)
    mileage = models.PositiveIntegerField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    final_drive_system = models.CharField(max_length=64, blank=True, null=True)
    wheels = models.CharField(max_length=64, blank=True, null=True)
    manufacturer = models.CharField(max_length=64, blank=True, null=True)
    engine_size = models.CharField(max_length=64, blank=True, null=True)
    warranty = models.CharField(max_length=64, blank=True, null=True)
    color = models.CharField(max_length=64, blank=True, null=True)


class MotorAccessoriesAndParts(Motors):
    condition = models.CharField(max_length=64, blank=True, null=True)


class HeavyVehicles(Motors):
    purpose = models.CharField(max_length=16, choices=MotorPurposeChoice.choices)
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    mileage = models.PositiveIntegerField(blank=True, null=True)
    body_condition = models.CharField(max_length=64)
    mechanic_condition = models.CharField(max_length=64)
    year = models.PositiveIntegerField(blank=True, null=True)
    warranty = models.CharField(max_length=64, blank=True, null=True)
    capacity_or_weight = models.CharField(max_length=64, blank=True, null=True)
    no_of_cylinder = models.CharField(max_length=32)
    horse_power = models.CharField(max_length=32)
    fuel_type = models.CharField(max_length=64, blank=True, null=True)


class BasicMotors(Motors):
    pass

