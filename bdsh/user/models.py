from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length = 32)
    passwd = models.CharField(max_length = 32)
    phone = models.CharField(max_length = 24)
    email = models.EmailField()