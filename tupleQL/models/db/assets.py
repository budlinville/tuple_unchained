from django.db import models


class TrackedAsset(models.Model):
    ticker      = models.CharField(max_length=10)
    name        = models.CharField(max_length=50)
    industry    = models.CharField(max_length=50)
    type        = models.CharField(max_length=15)
