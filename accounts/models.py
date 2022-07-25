from operator import mod
from django.db import models
from django.contrib.auth import get_user_model


# get django auth's system User model
User = get_user_model() 

# Create your models here.
class UserProfile(models.Model):
    """A Django model for User Profile.
    """

    user = models.OneToOneField(
        User,
        db_column='user_id',
        primary_key=True,
        on_delete=models.CASCADE,
    )


    