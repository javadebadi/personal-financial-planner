"""A module for Asset
"""

from operator import mod
from django.db import models
from django.contrib.auth import get_user_model
from .asset_category import AssetCategory
from .asset_subcategory import AssetSubCategory
from ..base import BaseItem
from ..currency import Currency
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
        editable=False,
    )

    sub_category = models.ForeignKey(
        AssetSubCategory,
        db_column='asset_subcategory_id',
        on_delete=models.PROTECT,
        related_name='items',
    )

    amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
    )

    unit_value = models.DecimalField(
        max_digits=18,
        decimal_places=2,
    )

    unit_value_currency_code = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        db_column='currency_code',
    )

    def __str__(self) -> str:
        return self.name + ' | ' + self.user.__str__()


    def save(self, *args, **kwargs):
        self.category = self.sub_category.category
        super(Asset, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Asset"
        verbose_name_plural = "Assets"
        ordering = (
            '-asset_id',
            )

