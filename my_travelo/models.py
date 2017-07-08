from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth import login, authenticate

# Create your models here.

class User(models.Model):
    pic = models.FileField(default=None)
    name=models.CharField(max_length=100)
    location_from=models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.name)

class Upload(models.Model):
    pic=models.FileField()
    description=models.CharField(max_length=300)
    name=models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.name)
