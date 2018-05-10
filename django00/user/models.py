from django.db import models

# Create your models here.
## 先写model再执行 python manage.py makemigrations
## 再执行 python manage.py migrate
class UserInfo(models.Model):
    username = models.CharField(max_length=64)
    pwd = models.CharField(max_length=32)
    age = models.IntegerField(max_length=3)


class Books(models.Model):
    name = models.CharField(max_length=128)
    r = models.ManyToManyField("UserInfo")