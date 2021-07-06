from django.contrib import admin
from .models.motor_model import Car, MotorCycle, HeavyVehicles
from .models.jobs_model import JobHiring, JobSeeking

admin.site.register(Car)
admin.site.register(MotorCycle)
admin.site.register(HeavyVehicles)
admin.site.register(JobSeeking)
