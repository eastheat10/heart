from django.db import models
# from django.contrib.auth.models import *

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 100)
    useremail = models.EmailField(max_length =128, verbose_name = '사용자이메일')