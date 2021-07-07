from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# define local imports
from rnd.models import BaseAdvertise, Category


class PropertyChoice(models.TextChoices):
    """
        define selection fields for property type
    """
    Residential_Units = 'Residential units'
    Commercial = 'Commercial'
    Rooms = 'Rooms'
    Others = 'Others'


class PropertyForRent(models.Model):
    """
        base property for rent fields to be added
    """
    property_reference_id = models.CharField(max_length=32, blank=True, null=True)  # define property reference ID
    minimum_contract_period = models.CharField(max_length=32, blank=True, null=True)  # define minimum contract period

    # broker information
    broker_id = models.CharField(max_length=32, blank=True, null=True)  # define broker ID
    lister_company_name = models.CharField(max_length=32, blank=True, null=True)  # define lister company name of broker
    permit_number = models.CharField(max_length=32, blank=True, null=True)  # permit number of lister company
    agent_name = models.CharField(max_length=32, blank=True, null=True)  # define agent name

    base_advertise = GenericRelation(BaseAdvertise)  # generate generic relation with BaseAdvertise model

    class Meta:
        """
            define the model as abstract
        """
        abstract = True


class ResidentialUnitsForRent(PropertyForRent):
    """
        store extra information about residential property for rent, inheritance with property for rent fields
    """
    bedrooms = models.PositiveIntegerField(blank=True, null=True)  # define number of bedrooms
    bathrooms = models.PositiveIntegerField(blank=True, null=True)  # define number of bathrooms
    maintenance_fee = models.DecimalField(max_digits=10, decimal_places=2)  # define property maintenance fee
    occupancy_status = models.CharField(max_length=32, blank=True, null=True)  # if property is occupied or vacant

    # extra information
    balcony = models.BooleanField(default=False)  # if property has balcony or not
    built_in_kitchen_appliances = models.BooleanField(
                                default=False)  # if property has built in kitchen appliances or not
    built_in_wardrobes = models.BooleanField(default=False)  # if property has built in wardrobes or not
    central_ac_or_heating = models.BooleanField(default=False)  # if property has central AC or heating or not
    concierge_service = models.BooleanField(default=False)  # if property has concierge service or not
    covered_parking = models.BooleanField(default=False)  # if property has covered parking or not
    maid_service = models.BooleanField(default=False)  # if property has maid service or not
    maids_room = models.BooleanField(default=False)  # if property has maids room or not
    pets_allowed = models.BooleanField(default=False)  # if pets allowed in property or not
    private_garden = models.BooleanField(default=False)  # if property has private garden or not
    private_gym = models.BooleanField(default=False)  # if property has private gym or not
    private_jacuzzi = models.BooleanField(default=False)  # if property has private jacuzzi or not
    private_pool = models.BooleanField(default=False)  # if property has private pool or not
    security = models.BooleanField(default=False)  # if property has security or not
    shared_gym = models.BooleanField(default=False)  # if property has shared gym or not
    shared_pool = models.BooleanField(default=False)  # if property has shared pool or not
    shared_spa = models.BooleanField(default=False)  # if property has shared spa or not
    study = models.BooleanField(default=False)  # if property has study or not
    view_of_landmark = models.BooleanField(default=False)  # if property has view of landmark or not
    view_of_water = models.BooleanField(default=False)  # if property has view of water or not
    walk_in_closet = models.BooleanField(default=False)  # if property has walk in closet or not


class CommercialForRent(PropertyForRent):
    """
        store extra information about commercial property for rent, inheritance with property for rent fields
    """
    bedrooms = models.PositiveIntegerField(blank=True, null=True)  # define number of bedrooms
    bathrooms = models.PositiveIntegerField(blank=True, null=True)  # define number of bathrooms
    maintenance_fee = models.DecimalField(max_digits=10, decimal_places=2)  # define property maintenance fee
    occupancy_status = models.CharField(max_length=32, blank=True, null=True)  # if property is occupied or vacant

    # extra information
    available_furnished = models.BooleanField(default=False)  # if property has available furnished
    available_network = models.BooleanField(default=False)  # if property has available network
    conference_room = models.BooleanField(default=False)  # if property has conference room
    covered_parking = models.BooleanField(default=False)  # if property has covered parking
    dining_in_building = models.BooleanField(default=False)  # if property has dining in building
    retail_in_building = models.BooleanField(default=False)  # if property has retail in building
    shared_gym = models.BooleanField(default=False)  # if property has shared gym
    shared_spa = models.BooleanField(default=False)  # if property has shared spa
    view_of_landmark = models.BooleanField(default=False)  # if property has view of landmark or not
    view_of_water = models.BooleanField(default=False)  # if property has view of water or not


class RoomsForRent(PropertyForRent):
    """
        store extra information about commercial property for rent, inheritance with property for rent fields
    """
    notice_period = models.CharField(max_length=32, blank=True, null=True)  # define notice period
    room_type = models.CharField(max_length=32, blank=True, null=True)  # define room type
    bathroom = models.CharField(max_length=32, blank=True, null=True)  # bathroom status of the room
    security_deposit = models.CharField(max_length=32, blank=True, null=True)  # define security deposit
    number_of_tenants = models.PositiveIntegerField(blank=True, null=True)  # define number of tenants room has
    balcony = models.BooleanField(default=False)  # if room has balcony or not

    # extra information
    cable_tv = models.BooleanField(default=False)  # if room has cable tv or not
    dryer = models.BooleanField(default=False)  # if room has dryer or not
    cleaning_included = models.BooleanField(default=False)  # if room has cleaning included or not
    kitchen_appliances = models.BooleanField(default=False)  # if room has kitchen appliances or not
    recreation_centre = models.BooleanField(default=False)  # if room has recreation centre or not
    maid_service = models.BooleanField(default=False)  # if room has maid service or not
    pets_allowed = models.BooleanField(default=False)  # if pets allowed in room or not
    gym = models.BooleanField(default=False)  # if room has gym or not
    jacuzzi = models.BooleanField(default=False)  # if room has jacuzzi or not
    swimming_pool = models.BooleanField(default=False)  # if room has swimming pool or not
    washer = models.BooleanField(default=False)  # if room has washer or not
    wireless_internet = models.BooleanField(default=False)  # if room has wireless internet or not


class BasicPropertyForRent(PropertyForRent):
    """
        create basic model with property for rent fields
    """
    property_type = models.CharField(max_length=32, choices=PropertyChoice.choices)  # define property type



