import os
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pfp_project.settings')
setup()


from pfp.models import Transaction, BankAccount, Bank
from django.contrib.auth import get_user_model

User = get_user_model()
for bank_account in BankAccount.objects.all():
    bank_account = BankAccount.objects.get(pk=bank_account.bank_account_id)
    total_balance = 0
    print(len(bank_account.transactions.all()))
    for obj in bank_account.transactions.all():
        if obj.inflow  == 'I':
            total_balance = total_balance + float(obj.amount)
        elif obj.inflow == 'O':
            print("OUT")
            total_balance = total_balance -  float(obj.amount)
        else:
            total_balance += 0 # TODO what if not inflow or outlfow
    bank_account.balance = total_balance
    bank_account.save()


