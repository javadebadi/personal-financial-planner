from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin

class DashboardView(PermissionRequiredMixin, View):
    permission_required =  (
        'subscribed',
        )

    def get(self, request):
        return HttpResponse("<h1>Hello Personal Financial Planner</h1>")