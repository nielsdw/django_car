from django.db import models

# Create your models here.


class Car(models.Model):
    no_doors = models.IntegerField()
    engine = models.CharField(max_length=256)
    roof = models.BooleanField()
    production = models.DateField()
