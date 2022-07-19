from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin

class DashboardView(PermissionRequiredMixin, View):
    permission_required =  (
        'subscribed',
        )

    def get(self, request):
        user = request.user
        context = {
            'title': 'dashboard',
        }
        print(context)
        return render(request, 'pfp/base.html', context=context)