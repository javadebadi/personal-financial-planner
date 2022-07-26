from typing import List
from unicodedata import decimal
from pfp.models import BankAccount, bank_accounts
from django.contrib.auth import get_user_model
User = get_user_model()

class BankAccountBR:

    def __init__(self, user: User) -> None:
        self.user = user
        self._bank_accounts_objs = BankAccount.objects.filter(
            user=self.user
        )
        self._total_balance = None

    @staticmethod
    def display_card_number(
        card_number: str,
        ) -> str:
        """A method to display card-number in - separated format
        """
        if card_number:
            return "-".join(card_number[i:i+4] for i in range(0, 16, 4))
        else:
            return ""

    @staticmethod
    def display_balance(
        balance: decimal,
        ) -> str:
        """A method to display balance in , separated format
        """
        balance = str(balance)
        s = ""
        if balance:
            if "." in balance:
                splitted = balance.split(".")
                s += "." + (splitted[1] if splitted[1] else "00")
                balance = splitted[0]
            while balance != "":
                s = balance[-3:] + "," + s
                balance = balance[:-3]
            s = s.replace(",.",".")
            if s.endswith(","):
                s = s[:-1]
        else:
            s = "0"
        return s

    def display_single_bank_account(self, bank_account_id: int) -> dict:
        """Retrives basic information about give account
        """
        if type(bank_account_id) == int:
            obj = BankAccount.objects.get(user=self.user, bank_account_id=bank_account_id)
        elif isinstance(bank_account_id, BankAccount):
            obj = bank_account_id

        data = {}
        data['card_number'] = BankAccountBR.display_card_number(obj.card_number)
        data['bank_name'] = obj.bank.bank_name
        data['balance'] = BankAccountBR.display_balance(obj.balance)
        data['memo'] = obj.memo
        data['currency_code'] = obj.currency_code
        data['bank_account_id'] = obj.bank_account_id
        return data

    def display(self) -> List[dict]:
        """Retrieves basic information about user accounts

        user : User
            the user for which we need to get information
        """
        bank_accounts = []
        for obj in self._bank_accounts_objs:
            data = self.display_single_bank_account(obj)
            bank_accounts.append(data)
        return bank_accounts

    def get_total_balance(self, base_currency='IRR'):
        """Gets the total balance of the user
        
        It sets the `_total_balance` attribute of the BR class and returns 
        the total balance of the user which is sum of balances of all
        accounts.
        """
        # TODO: implement sum with a base curreny code
        if self._total_balance is None:
            self._total_balance = sum(obj.balance for obj in self._bank_accounts_objs)
        return self._total_balance

    def display_total_balance(self, currency_code='IRR'):
        return {
            "balance": BankAccountBR.display_balance(
                self.get_total_balance()
                ),
            "currency_code": currency_code,
        }

        
