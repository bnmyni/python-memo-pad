from django.db import models

# Create your models here.
class Books(models.Model):
    bname = models.CharField(max_length=128)
    price = models.FloatField()