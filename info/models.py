from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=40)
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey('Family', 
                    on_delete=models.CASCADE)


class Family(models.Model):
    name = models.CharField(max_length=40)

