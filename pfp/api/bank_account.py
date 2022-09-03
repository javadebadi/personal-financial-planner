from rest_framework.views import APIView
from rest_framework.response import Response
from pfp.business_rules import BankAccountBR


class BankAccountAPIView(APIView):

    def get(self, request, bank_account_id):
        user = request.user
        br = BankAccountBR(user)
        data = {}
        data['detail'] = "OK"
        data['result'] = br.display_single_bank_account(bank_account_id)
        return Response(
            data=data,
            status=200,
        )
