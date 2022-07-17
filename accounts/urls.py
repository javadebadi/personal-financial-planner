from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    SignupView,
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='accounts_login'),
    path('logout/', LogoutView.as_view(), name='accounts_logout'),
    path('signup/', SignupView.as_view(), name='accounts_signup'),
]
