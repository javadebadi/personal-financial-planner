from django.views import View
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.messages import get_messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie


class LoginView(View):

    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        if request.user.is_anonymous:
            return render(request, 'accounts/login.html', {})
        else:
            return redirect(settings.SOCIAL_AUTH_LOGIN_REDIRECT_URL)

    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password,
            )
        if user is not None:
            login(request, user)
            return redirect(settings.SOCIAL_AUTH_LOGIN_REDIRECT_URL)
        else:
            messages.error(request, 'Username or password is wrong!')
            return render(request, 'accounts/login.html')


