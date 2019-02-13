from django.db import models
from employee.models import Employee

# Create your models here.
# funcs2

class Journey(models.Model):

    journey_destination = models.CharField(max_length=10)
    journey_purpose = models.CharField(max_length=100)
    journey_begin = models.DateTimeField()
    journey_end = models.DateTimeField()
    journey_cost = models.FloatField()
    journey_employee = models.ManyToManyField(Employee)

    def __str__(self):
        return self.journey_destination

