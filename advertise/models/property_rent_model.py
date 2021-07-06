from django.db import models

from django.contrib.contenttypes.fields import GenericRelation

from rnd.models import BaseAdvertise, Category


class PropertyChoice(models.TextChoices):
    Residential_Units = 'Residential units'
    Commercial = 'Commercial'
    Rooms = 'Rooms'
    Others = 'Others'


class PropertyForRent(models.Model):
    # broker information
    broker_id = models.CharField(max_length=32, blank=True, null=True)
    lister_company_name = models.CharField(max_length=32, blank=True, null=True)
    permit_number = models.CharField(max_length=32, blank=True, null=True)
    agent_name = models.CharField(max_length=32, blank=True, null=True)
    base_advertise = GenericRelation(BaseAdvertise)

    class Meta:
        abstract = True


class ResidentialUnitsForRent(PropertyForRent):
    bedrooms = models.PositiveIntegerField(blank=True, null=True)
    bathrooms = models.PositiveIntegerField(blank=True, null=True)
    developer = models.CharField(max_length=32, blank=True, null=True)
    annual_community_fee = models.DecimalField(max_digits=10, decimal_places=2)
    property_reference_id = models.CharField(max_length=32, blank=True, null=True)
    buyer_transfer_fee = models.DecimalField(max_digits=10, decimal_places=2)
    seller_transfer_fee = models.DecimalField(max_digits=10, decimal_places=2)
    maintenance_fee = models.DecimalField(max_digits=10, decimal_places=2)
    occupancy_status = models.CharField(max_length=32, blank=True, null=True)

    # extra information
    balcony = models.BooleanField(default=False)
    built_in_kitchen_appliances = models.BooleanField(default=False)
    built_in_wardrobes = models.BooleanField(default=False)
    central_ac_or_heating = models.BooleanField(default=False)
    concierge_service = models.BooleanField(default=False)
    covered_parking = models.BooleanField(default=False)
    maid_service = models.BooleanField(default=False)
    maids_room = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=False)
    private_garden = models.BooleanField(default=False)
    private_gym = models.BooleanField(default=False)
    private_jacuzzi = models.BooleanField(default=False)
    private_pool = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    shared_gym = models.BooleanField(default=False)
    shared_pool = models.BooleanField(default=False)
    shared_spa = models.BooleanField(default=False)
    study = models.BooleanField(default=False)
    view_of_landmark = models.BooleanField(default=False)
    view_of_water = models.BooleanField(default=False)
    walk_in_closet = models.BooleanField(default=False)


class CommercialForRent(PropertyForRent):
    bedrooms = models.PositiveIntegerField(blank=True, null=True)
    bathrooms = models.PositiveIntegerField(blank=True, null=True)
    developer = models.CharField(max_length=32, blank=True, null=True)
    property_reference_id = models.CharField(max_length=32, blank=True, null=True)
    annual_community_fee = models.DecimalField(max_digits=10, decimal_places=2)
    buyer_transfer_fee = models.DecimalField(max_digits=10, decimal_places=2)
    seller_transfer_fee = models.DecimalField(max_digits=10, decimal_places=2)
    maintenance_fee = models.DecimalField(max_digits=10, decimal_places=2)
    occupancy_status = models.CharField(max_length=32, blank=True, null=True)

    # extra information
    available_furnished = models.BooleanField(default=False)
    available_network = models.BooleanField(default=False)
    conference_room = models.BooleanField(default=False)
    covered_parking = models.BooleanField(default=False)
    dining_in_building = models.BooleanField(default=False)
    retail_in_building = models.BooleanField(default=False)
    shared_gym = models.BooleanField(default=False)
    shared_spa = models.BooleanField(default=False)
    view_of_landmark = models.BooleanField(default=False)
    view_of_water = models.BooleanField(default=False)


class RoomsForRent(PropertyForRent):
    property_reference_id = models.CharField(max_length=32, blank=True, null=True)
    minimum_contract_period = models.CharField(max_length=32, blank=True, null=True)
    notice_period = models.CharField(max_length=32, blank=True, null=True)
    room_type = models.CharField(max_length=32, blank=True, null=True)
    bathroom = models.CharField(max_length=32, blank=True, null=True)
    security_deposit = models.CharField(max_length=32, blank=True, null=True)
    number_of_tenants = models.PositiveIntegerField(blank=True, null=True)
    balcony = models.BooleanField(default=False)

    # extra information
    cable_tv = models.BooleanField(default=False)
    dryer = models.BooleanField(default=False)
    cleaning_included = models.BooleanField(default=False)
    kitchen_appliances = models.BooleanField(default=False)
    recreation_centre = models.BooleanField(default=False)
    maid_service = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    jacuzzi = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    washer = models.BooleanField(default=False)
    wireless_internet = models.BooleanField(default=False)


class BasicPropertyForRent(PropertyForRent):
    property_type = models.CharField(max_length=32, choices=PropertyChoice.choices)
    property_reference_id = models.CharField(max_length=32, blank=True, null=True)
    minimum_contract_period = models.CharField(max_length=32, blank=True, null=True)



