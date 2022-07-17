from django.urls import path
from pfp.views import (
    DashboardView,
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(DashboardView.as_view()), name='pfp_dasboard'),
]