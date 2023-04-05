from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=20)
    salary = models.FloatField()
    company = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
