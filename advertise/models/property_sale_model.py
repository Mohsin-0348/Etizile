from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# define local imports
from rnd.models import BaseAdvertise, Category


class PropertyChoice(models.TextChoices):
    """
        define selection fields for property type
    """
    Residential = 'Residential'
    Commercial = 'Commercial'
    Land = 'Land'
    Others = 'Others'


class PropertyForSale(models.Model):
    """
        base property for sale fields to be added
    """
    size = models.CharField(max_length=32, blank=True, null=True)  # size of the property
    total_closing_fee = models.DecimalField(max_digits=10, decimal_places=2)  # define total closing fee
    property_reference_id = models.CharField(max_length=32, blank=True, null=True)  # define property reference ID
    buyer_transfer_fee = models.DecimalField(max_digits=10, decimal_places=2)  # define buyer transfer fee
    seller_transfer_fee = models.DecimalField(max_digits=10, decimal_places=2)  # define seller transfer fee

    # seller information
    seller_type = models.CharField(max_length=32, blank=True, null=True)  # is seller is landlord or agent
    completion_status = models.BooleanField(default=False)  # if landlord has completed the property or not
    landlord_name = models.CharField(max_length=32, blank=True, null=True)  # define landlord name
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


class ResidentialForSale(PropertyForSale):
    """
        store extra information about residential property for sale, inheritance with property for sale fields
    """
    bedrooms = models.PositiveIntegerField(blank=True, null=True)  # define number of bedrooms
    bathrooms = models.PositiveIntegerField(blank=True, null=True)  # define number of bathrooms
    developer = models.CharField(max_length=32, blank=True, null=True)  # store developer information of the property
    annual_community_fee = models.DecimalField(max_digits=10, decimal_places=2)  # define annual community fee
    maintenance_fee = models.DecimalField(max_digits=10, decimal_places=2)  # define property maintenance fee
    occupancy_status = models.CharField(max_length=32, blank=True, null=True)  # if property is occupied or vacant

    # extra information
    balcony = models.BooleanField(default=False)  # if property has balcony or not
    built_in_kitchen_appliances = models.BooleanField(default=False)  # if property has built in kitchen appliances or not
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


class CommercialForSale(PropertyForSale):
    """
        store extra information about commercial property for sale, inheritance with property for sale fields
    """
    bedrooms = models.PositiveIntegerField(blank=True, null=True)  # define number of bedrooms
    bathrooms = models.PositiveIntegerField(blank=True, null=True)  # define number of bathrooms
    developer = models.CharField(max_length=32, blank=True, null=True)  # store developer information of the property
    annual_community_fee = models.DecimalField(max_digits=10, decimal_places=2)  # define annual community fee
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


class LandForSale(PropertyForSale):
    """
        store extra information about land property for sale, inheritance with property for sale fields
    """
    approved_build_up_area_size = models.CharField(max_length=32, blank=True,
                                                   null=True)  # define approved build up area size of the property
    zoned_for = models.CharField(max_length=32, blank=True, null=True)  # define why th property zoned for
    freehold = models.BooleanField(default=False)  # if property has freehold or not


class BasicPropertyForSale(PropertyForSale):
    """
        create basic model with property for sale fields
    """
    property_type = models.CharField(max_length=32, choices=PropertyChoice.choices)  # define property type
