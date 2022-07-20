from django.contrib import admin
from pfp.models import (
    Bank,
    BankAccount,
)

# Register your models here.
admin.site.register(Bank)
admin.site.register(BankAccount)