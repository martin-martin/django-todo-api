from django.db import models
from django.contrib.auth.models import AbstractUser


'''
We use the same AbstractUser that the default Django User model uses,
but defining our own User model gives us the ability to easily edit it
later on while still retaining the same features as the default Django User.
'''


class User(AbstractUser):
    pass
