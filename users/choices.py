from django.db import models


class GenderChoices(models.TextChoices):
    """
        selection fields of gender choice
    """
    Female = 'female'
    Male = 'male'
    Other = 'other'


class SocialAccountTypeChoices(models.TextChoices):
    """
    selection fields for social account type choice
    """
    FACEBOOK = 'facebook'
    LINKEDIN = 'linkedin'
    GOOGLE = 'google'
    APPLE = 'apple'


class DeviceTypeChoices(models.TextChoices):
    """
        selection fields for device type of user
    """
    IOS = "ios"
    ANDROID = "android"
    WEB = "web"


class WeekdayChoices(models.TextChoices):
    """
        selection fields for week day choice
    """
    MON = "Mon"
    TUE = "Tue"
    WED = "Wed"
    THU = "Thu"
    FRI = "Fri"
    SAT = "Sat"
    SUN = "Sun"


