from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Physical(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    height = models.FloatField()
    weight = models.FloatField()

