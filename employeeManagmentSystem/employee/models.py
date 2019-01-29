from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from departments.models import Departments
from project.models import Project


class Employee(User):
    department_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

