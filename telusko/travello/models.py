from django.db import models

# Create your models here.
class Destination(models.Model):
    # id = models.IntegerField()
    name =  models.CharField(max_length=100)
    img = models.ImageField()
    desc = models.CharField(max_length=100)
    price = models.IntegerField()
    offer = models.BooleanField()
