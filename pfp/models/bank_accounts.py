from operator import mod
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Bank(models.Model):
    
    bank_id = models.AutoField(
        primary_key=True,
    )

    bank_name = models.CharField(
        max_length=64,
    )

    # country: TODO

    def __str__(self) -> str:
        return self.bank_name


class BankAccount(models.Model):

    ACCOUNT_TYPE_CHOICES = (
        ('checking', 'checking'),
        ('saving', 'saving'),
    )

    bank_account_id = models.AutoField(
        primary_key=True,
    )

    account_type = models.CharField(
        max_length=16,
        choices=ACCOUNT_TYPE_CHOICES,
        default='checking',
    )

    IBAN = models.CharField(
        max_length=32,
        null=True,
        blank=True,
    )

    card_number = models.CharField(
        max_length=16,
    )

    card_expire_date = models.DateField(
        null=True,
        blank=True,
    )

    balance = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0,
        )

    bank = models.ForeignKey(
        Bank,
        on_delete=models.PROTECT,
        db_column='bank_id',
        related_name='accounts',
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='bank_accounts',
    )

    def __str__(self):
        return str(self.user) + " - " + str(self.card_number)

    class Meta:
        pass