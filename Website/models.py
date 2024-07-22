from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Login(models.Model):
    login_id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.login_id  