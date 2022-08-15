from django.contrib import admin
from pfp.models import (
    Bank,
    BankAccount,
    Transaction,
    AssetCategory,
    AssetSubCategory,
    Asset,
    Currency,
)

# Register your models here.
admin.site.register(Bank)
admin.site.register(BankAccount)
admin.site.register(Currency)


@admin.register(Transaction)
class TranactionAdmin(admin.ModelAdmin):
    list_display = (
        'transaction_id',
        'transaction_datetime',
        'amount',
        'bank_account',
        'inflow',
        )

    list_filter = (
        'user',
    )


@admin.register(AssetSubCategory)
class AssetSubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'asset_subcategory_id',
        'user',
        'name',
        'category',
        )

    list_filter = (
        'user',
    )


@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'asset_category_id',
        'user',
        'name',
        )

    list_filter = (
        'user',
    )

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        'asset_id',
        'user',
        'name',
        'category',
        'sub_category',
        'amount',
        'unit_value',
        'unit_value_currency_code',
        )

    list_filter = (
        'user',
        'category',
        'sub_category',
    )
