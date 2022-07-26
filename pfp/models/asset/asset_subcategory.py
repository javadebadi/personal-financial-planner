"""A module for asset related models
"""

from django.db import models
from django.contrib.auth import get_user_model
from .asset_category import AssetCategory
User = get_user_model()


class AssetSubCategory(models.Model):

    """Class to determine asset sub categories of users.
    
    Each category of asset may categorized to more groups. We call these
    groups subcategories.


    - Cash
        * Cash
        * Checking Account
        * Saving Account
        * Money Market Account
        * Certificates of Deposit (CDs)
        * U.S. Government Treasury Bill
    -
    """

    asset_subcategory_id = models.AutoField(
        primary_key=True,
        )
    
    user = models.ForeignKey(
        User,
        db_column='user_id',
        on_delete=models.CASCADE,
        related_name='asset_subcategories',
    )

    name = models.CharField(
        max_length=64,
    )

    category = models.ForeignKey(
        AssetCategory,
        db_column='asset_category_id',
        on_delete=models.PROTECT,
        related_name='subcategories',
    )

    def __str__(self) -> str:
        return self.name + ' | ' + self.user.__str__()

    class Meta:
        verbose_name = "Asset Sub-category"
        verbose_name_plural = "Asset Sub-Categories"

