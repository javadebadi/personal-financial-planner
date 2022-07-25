"""A module for asset related models
"""

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class AssetCategory(models.Model):

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
    
    user = models.ForeignKey(
        User,
        db_column='user_id',
        on_delete=models.CASCADE,
        related_name='asset_categories',
    )

    name = models.CharField(
        max_length=64,
    )


    class Meta:
        verbose_name = "Asset Category"
        verbose_name_plural = "Asset Categories"

