from django.db import models


class Example(models.Model):
    title = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
