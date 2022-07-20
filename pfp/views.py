from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from pfp.business_rules import BankAccountBR

class DashboardView(PermissionRequiredMixin, View):
    permission_required =  (
        'subscribed',
        )

    def get(self, request):
        user = request.user
        br = BankAccountBR(user)
        context = {
            'title': 'dashboard',
            'bank_accounts': br.display(),
            'total_balance': br.display_total_balance(),
        }
        print(context)
        return render(request, 'pfp/base.html', context=context)