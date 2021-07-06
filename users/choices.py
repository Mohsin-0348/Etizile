from django.db import models


class GenderChoices(models.TextChoices):
    Female = 'female'
    Male = 'male'
    Other = 'other'


class SocialAccountTypeChoices(models.TextChoices):
    FACEBOOK = 'facebook'
    LINKEDIN = 'linkedin'
    GOOGLE = 'google'
    APPLE = 'apple'


class DeviceTypeChoices(models.TextChoices):
    IOS = "ios"
    ANDROID = "android"
    WEB = "web"


class WeekdayChoices(models.TextChoices):
    MON = "Mon"
    TUE = "Tue"
    WED = "Wed"
    THU = "Thu"
    FRI = "Fri"
    SAT = "Sat"
    SUN = "Sun"


