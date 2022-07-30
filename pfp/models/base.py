"""Module for Base Category
"""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseItem(models.Model):
    """BaseItem is a class with user and name.

    This class is the base for several child classes
    """

    user = models.ForeignKey(
        User,
        db_column='user_id',
        on_delete=models.CASCADE,
        related_name="%(class)s",
    )

    name = models.CharField(max_length=64)
    

    class Meta:
        abstract = True