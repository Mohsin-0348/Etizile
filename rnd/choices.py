from django.db import models


class CategoryKeywordChoice(models.TextChoices):
    MOTORS = 'BasicMotors'
    CAR = 'Car'
    MOTOR_CYCLE = 'MotorCycle'
    MOTOR_ACCESSORIES_AND_PARTS = 'MotorAccessoriesAndParts'
    Heavy_Vehicles = 'HeavyVehicles'

    Property_For_Sale = 'BasicPropertyForSale'
    Residential_For_Sale = 'ResidentialForSale'
    Commercial_For_Sale = 'CommercialForSale'
    Land_For_Sale = 'LandForSale'

    Property_For_Rent = 'BasicPropertyForRent'
    Residential_Units_For_Rent = 'ResidentialUnitsForRent'
    Commercial_For_Rent = 'CommercialForRent'
    Rooms_For_Rent = 'RoomsForRent'

    Jobs = 'Jobs'
    Job_Hiring = 'JobHiring'
    Job_Seeking = 'JobSeeking'

    Community = 'BasicCommunity'
    Car_Lift = 'CarLift'
    Pre_Loved_Items = 'BasicPreLovedItems'
    Jewelry_And_Watches = 'JewelryAndWatches'

    Electronics = 'BasicElectronics'
    Computers = 'Computers'
    Mobile_Phones = 'MobilePhones'


class CurrencyChoice(models.TextChoices):
    BIRR = 'birr'
    USD = 'usd'


class RegionChoice(models.TextChoices):
    Addis_Ababa = 'Addis ababa'
    Dire_Dawa = 'Dire dawa'
    Oromia_Region = 'Oromia Region'
    Amhara_Region = 'Amhara Region'
    Somali_Region = 'Somali Region'
    Afar_Region = 'Afar Region'
    Tigray_Region = 'Tigray Region'


class CityChoice(models.TextChoices):
    Bole = 'Bole'
    Adama = 'Adama'
    Jimma = 'Jimma'
    Bahir_Dar = 'Bahir dar'
    Arsi = 'Arsi'
    West_Arsi = 'West Arsi'
    Yeka = 'Yeka'
    Akaki_Kality = 'Akaki Kality'
    Kirkos = 'Kirkos'
    Gullele = 'Gullele'
    Arada = 'Arada'
    Lideta = 'Lideta'
    Addis_Ketema = 'Addis Ketema'
    Kolfe_keranio = 'Kolfe keranio'
    Nefas_silk_lafto = 'Nefas silk lafto'

