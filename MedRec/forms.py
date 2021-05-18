from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateAccount(UserCreationForm):
    POSITION_CHOICES = (
        ('Practitioner', 'Practitioner'),
        ('Nurse', 'Nurse'),
        ('Accountant', 'Accountant'),
    )

    position = forms.ChoiceField(choices=POSITION_CHOICES)

    class Meta:
        model = User
        fields = ['position', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'position']

    def __str__(self):
        return self.position
