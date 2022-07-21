from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import make_naive
from pfp.models import BankAccount

User = get_user_model()


class Transaction(models.Model):

    INFLOW_CHOICES = (
        ('I', 'inflow'),
        ('O', 'outflow'),
    )

    transaction_id = models.CharField(
        max_length=48,
        primary_key=True,
    )

    bank_account = models.ForeignKey(
        BankAccount,
        on_delete=models.CASCADE,
        db_column='bank_account_id',
        related_name='transactions',
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='transactions',
    )

    amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0,
        )

    transaction_datetime = models.DateTimeField()

    inflow = models.CharField(
        max_length=1,
        choices=INFLOW_CHOICES,
    )

    def __str__(self) -> str:
        return super().__str__()

    def save(self, *args, **kwargs) -> str:
        if self.transaction_id is None:
            return super(Transaction, self).save(*args, **kwargs)
        else:
            self.transaction_id = str(self.user.id).rjust(10, '0') + '-'
            self.transaction_id += str(self.transaction_datetime) + '-'
            self.transaction_id +=  str(self.bank_account.bank_account_id).rjust(10, '0')
            return super(Transaction, self).save(*args, **kwargs)

    class Meta:
        ordering = (
            '-transaction_datetime',
        )

