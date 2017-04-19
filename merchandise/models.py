from __future__ import unicode_literals
from django.db import models
from django.conf import settings


# Create your models here.
class Merchandise(models.Model):

    image = models.ImageField(upload_to="merch_images", blank=True, null=True)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.name
