from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation

# define local imports
from rnd.models import Category, BaseAdvertise

User = get_user_model()  # define user model


class JobTypeChoice(models.TextChoices):
    """
        define selection fields for job advertising
    """
    HIRING = 'hiring'
    SEEKING = 'seeking'


class Company(models.Model):
    """
        company information of user for job advertising
    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='company_user')  # company belongs to which user
    name = models.CharField(max_length=100)  # name of the company
    trade_license = models.CharField(max_length=32, blank=True, null=True)  # trade license number of the company
    industry = models.CharField(max_length=32)  # category industry of the company
    company_size = models.CharField(max_length=10)  # how many employees works on
    company_website = models.URLField(blank=True, null=True)  # url address of the company website
    description = models.TextField(blank=True, null=True)  # som details of the company in words
    contact_name = models.CharField(max_length=32, blank=True, null=True)  # whom to be contact
    phone_number = models.CharField(max_length=16, blank=True, null=True)  # contact number of the company
    address = models.CharField(max_length=64, blank=True, null=True)  # location of company

    def __str__(self):
        return self.name


class Jobs(models.Model):
    """
        base job advertising fields to be added
    """
    carrier_level = models.CharField(max_length=64, blank=True, null=True)  # carrier level of employee
    work_experience = models.CharField(max_length=64, blank=True, null=True)  # work experience in years
    education_level = models.CharField(max_length=64, blank=True, null=True)  # educational degree of employee
    salary_range = models.CharField(max_length=64, blank=True, null=True)  # salary range for that job

    base_advertise = GenericRelation(BaseAdvertise)  # generate generic relation with BaseAdvertise model

    class Meta:
        """
            define the model as abstract
        """
        abstract = True


class JobHiring(Jobs):
    """
        store extra information for hiring employee, inheritance with job fields
    """
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, related_name='job_company',
                                blank=True, null=True)  # company belongs to that job
    employment_type = models.CharField(max_length=32)  # category of employee
    cv_required = models.BooleanField(default=False)  # if cv required or not
    benefits = models.CharField(max_length=64)  # benefits of the job


class Skills(models.Model):
    """
        store multiple skills for hiring employees
    """
    job = models.ForeignKey(JobHiring, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=32)


class JobSeeking(Jobs):
    """
        store extra information for seeking jobs, inheritance with job fields
    """
    cv = models.FileField(upload_to='advertise/jobs/cv/', blank=True, null=True)  # candidate cv to be uploaded
    gender = models.CharField(max_length=64, blank=True, null=True)  # candidate gender specification
    nationality = models.CharField(max_length=64, blank=True, null=True)  # store candidate country belongs to
    current_location = models.CharField(max_length=64, blank=True, null=True)  # store candidate current city
    current_company = models.CharField(max_length=64, blank=True, null=True)  # store candidate current company
    current_position = models.CharField(max_length=64, blank=True, null=True)  # store candidate current position
    notice_period = models.CharField(max_length=64, blank=True, null=True)  # when to notice for job
    visa_status = models.CharField(max_length=64, blank=True, null=True)  # if candidate have visa or not
    commitment = models.CharField(max_length=64, blank=True, null=True)  # if candidate have any commitment
    location_prefer = models.CharField(max_length=64, blank=True, null=True)  # where candidate wish to work

