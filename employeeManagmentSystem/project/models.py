from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.TextField(max_length=10, unique=True)

    def __str__(self):
        return self.project_name

