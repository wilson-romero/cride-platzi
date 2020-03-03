from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from cride.utils.models import CRideModel

# Create your models here.


class User(CRideModel, AbstractUser):

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',
        message='You must enter a valid phone number'
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=15, blank=True
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. ',
            'Clients are the main type of users.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user have verified its email address.'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username
