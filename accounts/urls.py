from django.urls import path
from .views import (
    LoginView,
    LogoutView,
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='accounts_login'),
    path('logout/', LogoutView.as_view(), name='accounts_logout'),
]
