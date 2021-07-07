from django.db import models


class MobileChoice(models.TextChoices):
    """
        define selection fields for mobile model choice
    """
    ACER = 'Acer'
    ALCATEL = 'Alcatel'
    APPLE_IPHONE = 'Apple iPhone'
    AsusASUS = 'Asus'
    BLACKBERRY = 'Blackberry'
    CAT = 'CAT'
    CECT = 'CECT'
    GOOGLE = 'Google'
    HTC = 'HTC'
    HEWLETT_PACKARD = 'Hewlett Packard'
    HUAWEI = 'Huawei'
    LG = 'LG'
    LAVA = 'Lava'
    LENOVO = 'Lenovo'
    MEIZU = 'Meizu'
    MOTOROLA = 'Motorola'
    NOKIA = 'Nokia'
    ONEPLUS = 'OnePlus'
    OPPO = 'Oppo'
    PALM = 'Palm'
    REALME = 'Realme'
    gSAMSUNG = 'Samsung'
    SANYO = 'Sanyo'
    SIDEKICK = 'Sidekick'
    SONY_ERICSSON = 'Sony Ericsson'
    VERTU = 'Vertu'
    VIVO = 'Vivo'
    XIAOMI = 'Xiaomi'
    YOTA = 'Yota'
    IMATE = 'iMate'
    OTHER = 'Other'


class ManufacturerChoice(models.TextChoices):
    """
        define selection fields for motor cycle manufacturer choice
    """
    Access_Motor = 'Access Motor'
    Aprillia = 'Aprillia'
    Asiawing = 'Asiawing'
    Bajaj = 'Bajaj'
    Benelli = 'Benelli'
    BMW = 'BMW'
    Buell = 'Buell'
    Can_am = 'Can-am'
    Ducati = 'Ducati'
    Gas_Gas = 'Gas Gas'
    Harley_Davidson = 'Harley Davidson'
    Honda = 'Honda'
    Husaberg = 'Husaberg'
    Husqvarna = 'Husqvarna'
    Indian = 'Indian'
    Kawasaki = 'Kawasaki'
    KTM = 'KTM'
    Moto_Guzzi = 'Moto Guzzi'
    MV_Agusta = 'MV Agusta'
    Norton = 'Norton'
    Polaris = 'Polaris'
    Royal_Enfield = 'Royal Enfield'
    Suzuki = 'Suzuki'
    Triumph = 'Triumph'
    Vespa = 'Vespa'
    Victory = 'Victory'
    Yamaha = 'Yamaha'
    Other = 'Other'


