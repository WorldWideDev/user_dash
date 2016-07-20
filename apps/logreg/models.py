from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, related_name='cust')
    desc = models.TextField(max_length = 250, blank=True)
    def __str__(self):
        return self.user.username
    class Meta:
        db_table = 'custom_users'

