from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    SignupView,
)
from django.conf import settings


ACCOUNTS_URLS = settings.URL_ENDPOINTS.get("account")
if ACCOUNTS_URLS is not None:
    LOGIN_URL = ACCOUNTS_URLS.get("login", "login/")
    LOGOUT_URL = ACCOUNTS_URLS.get("logout", "logout/")
    SIGNUP_URL = ACCOUNTS_URLS.get("logout", "signup/")
else:
    LOGIN_URL = 'login/'
    LOGOUT_URL = 'logout/'
    SIGNUP_URL = 'signup/'

urlpatterns = [
    path(LOGIN_URL, LoginView.as_view(), name='accounts_login'),
    path(LOGOUT_URL, LogoutView.as_view(), name='accounts_logout'),
    path(SIGNUP_URL, SignupView.as_view(), name='accounts_signup'),
]
