from django.contrib import admin
from pfp.models import (
    Bank,
    BankAccount,
    Transaction,
)

# Register your models here.
admin.site.register(Bank)
admin.site.register(BankAccount)


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
