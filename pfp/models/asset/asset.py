"""A module for Asset
"""

from django.db import models
from django.contrib.auth import get_user_model
from .asset_category import AssetCategory
from .asset_subcategory import AssetSubCategory
from ..base import BaseItem
User = get_user_model()


class Asset(BaseItem):

    """Asset
    """

    asset_id = models.AutoField(
        primary_key=True,
        )

    category = models.ForeignKey(
        AssetCategory,
        db_column='asset_category_id',
        on_delete=models.PROTECT,
        related_name='items',
    )

    sub_category = models.ForeignKey(
        AssetSubCategory,
        db_column='asset_subcategory_id',
        on_delete=models.PROTECT,
        related_name='items',
    )

    def __str__(self) -> str:
        return self.name + ' | ' + self.user.__str__()

    class Meta:
        verbose_name = "Asset"
        verbose_name_plural = "Assets"

