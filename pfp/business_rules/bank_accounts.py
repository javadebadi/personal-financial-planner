from typing import List
from unicodedata import decimal
from pfp.models import BankAccount, bank_accounts
from django.contrib.auth import get_user_model
User = get_user_model()

class BankAccountBR:

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

    def display(self, user: User) -> List[dict]:
        """Retrieves basic information about user accounts

        user : User
            the user for which we need to get information
        """
        bank_accounts_objs = BankAccount.objects.filter(
            user=user
        )
        bank_accounts = []
        for obj in bank_accounts_objs:
            data = {}
            data['card_number'] = BankAccountBR.display_card_number(obj.card_number)
            data['bank_name'] = obj.bank.bank_name
            data['balance'] = BankAccountBR.display_balance(obj.balance)
            data['memo'] = obj.memo
            bank_accounts.append(data)
        return bank_accounts
        
