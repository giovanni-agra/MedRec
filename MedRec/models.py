from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class GeneralPractitioner(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.User}"

    @receiver(post_save, sender=User)
    def create_account(sender, instance, created, **kwargs):
        if created:
            print(User.username)
            print('User created')
            instance.groups.add(Group.objects.get(name='Practitioners'))
            print('User added to Practitioner Group')
