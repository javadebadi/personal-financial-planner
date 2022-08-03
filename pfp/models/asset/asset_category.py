"""A module for asset related models
"""

from django.db import models
from django.contrib.auth import get_user_model
from ..base import BaseItem
User = get_user_model()


class AssetCategory(BaseItem):

    """Class to determine asset categories of users.
    
    Personal Assets can be categorized in various ways.
    In PFP app, we define 4 default categories for assets however a user can
    delete any of these categories and/or add her/his own categories.

    The four default personal asset groups are:
    - Cash like
    - Persoanl Property
    - Real estate
    - Investment

    """

    asset_category_id = models.AutoField(
        primary_key=True,
        )
    

    def __str__(self) -> str:
        return self.name + ' | ' + self.user.__str__()


    class Meta:
        verbose_name = "Asset Category"
        verbose_name_plural = "Asset Categories"
        ordering = (
            'user',
            'name',
        )

