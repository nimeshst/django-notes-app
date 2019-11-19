from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TextNotes(models.Model):
    # model for our app for creating and deleting user notes
    note = models.TextField(max_length=10000)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, null=True, related_name='createdby')
    # we dont need reverse releationship here
    updated_by = models.ForeignKey(User, null=True, related_name='+')
