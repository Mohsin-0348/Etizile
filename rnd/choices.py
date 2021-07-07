from django.db import models


class CategoryKeywordChoice(models.TextChoices):
    """
        define selection fields for category model choice
    """
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
    """
        define selection fields for currency choice
    """
    BIRR = 'birr'
    USD = 'usd'


class RegionChoice(models.TextChoices):
    """
        define selection fields for region choice
    """
    Addis_Ababa = 'Addis Ababa'
    Dire_Dawa = 'Dire Dawa'
    Oromia_Region = 'Oromia Region'
    Amhara_Region = 'Amhara Region'
    Somali_Region = 'Somali Region'
    Afar_Region = 'Afar Region'
    Tigray_Region = 'Tigray Region'


class CityChoice(models.TextChoices):
    """
        define selection fields for city choice
    """
    Bole = 'Bole'
    Yeka = 'Yeka'
    Akaki_Kality = 'Akaki Kality'
    Kirkos = 'Kirkos'
    Gullele = 'Gullele'
    Arada = 'Arada'
    Lideta = 'Lideta'
    Addis_Ketema = 'Addis Ketema'
    Kolfe_keranio = 'Kolfe keranio'
    Nefas_silk_lafto = 'Nefas silk lafto'

    Adama = 'Adama'
    Arsi = 'Arsi'
    Shashemense = 'Shashemense'
    Bale = 'Bale'
    East_Hararghe = 'East Hararghe'
    East_Shewa = 'East Shewa'
    East_Welega = 'East Welega'
    Jimma = 'Jimma'
    Borena = 'Borena'
    Guji = 'Guji'
    West_Shewa = 'West Shewa'
    West_Hararghe = 'West Hararghe'
    Oromia_Finfine = 'Oromia Finfine'
    North_Shewa = 'North Shewa'
    West_Arsi = 'West Arsi'
    West_Welega = 'West Welega'
    Kelem_Welega = 'Kelem Welega'
    South_west_shewa = 'South west shewa'
    ILLubabor = 'ILLubabor'
    Horo_Gudru_Welega = 'Horo Gudru Welega'
    West_Guji = 'West Guji'

    Agew_Awi = 'Agew Awi'
    Bahir_Dar = 'Bahir Dar'
    East_Gojjam = 'East Gojjam'
    North_Gondar = 'North Gondar'
    North_Wollo = 'North Wollo'
    South_Gondor = 'South Gondor'
    South_Wollo = 'South Wollo'
    Wag_Hemra = 'Wag Hemra'
    West_Gojam = 'West Gojam'

    Afder = 'Afder'
    Dawa = 'Dawa'
    Degehabur = 'Degehabur'
    Dollo = 'Dollo(werder)'
    Erer = 'Erer'
    Fafan = 'Fafan(Jigjiga)'
    Gode = 'Gode'
    Harawo = 'Harawo'
    Jarar = 'Jarar(Degehabur)'
    Kebri_Beyah = 'Kebri Beyah'
    Korahe = 'Korahe'
    Liben = 'Liben'
    Nogob = 'Nogob(Fiq)'
    Shebelle = 'Shebelle(Godey)'
    Sitti = 'Sitti(Shinile)'

    Dire_Dawa_city = 'Dire Dawa city'
    Gurgura = 'Gurgura'

    Argoba = 'Argoba'
    Awsi_Rasu = 'Awsi Rasu'
    Fanti_Rasu = 'Fanti Rasu'
    Gabi_Rasu = 'Gabi Rasu'
    Harri_Rasu = 'Harri Rasu'
    Kilbati_Rasu = 'Kilbati Rasu'

    Adwa = 'Adwa'
    Aksum = 'Aksum'
    Adigrat = 'Adigrat'
    Shire = 'Shire'

