from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Account(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=101)
    last_name = models.CharField(max_length=101)
    email = models.EmailField(blank=True)
    position = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
