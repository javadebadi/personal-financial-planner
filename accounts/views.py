from django.views import View
from django.conf import settings
from django.shortcuts import (
    render,
    redirect,
    )
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    )
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()


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


class LogoutView(View):

    def post(self, request):
        logout(request)
        return redirect('accounts_login')

    def get(self, request):
        logout(request)
        return redirect('accounts_login')


class SignupView(View):

    def post(self, request):
        try:
            username = request.POST['username']
            email = request.POST.get('email')
            password = request.POST['password']
            user = User.objects.create_user(
                username,
                email,
                password,
                )
            login(
                request,
                user,
                backend='django.contrib.auth.backends.ModelBackend',
                )
            return redirect(settings.SOCIAL_AUTH_LOGIN_REDIRECT_URL)
        except IntegrityError as e:
            raise NotImplementedError("Signup of exising user is not implemented")


    def get(self, request):
        if request.user.is_anonymous:
            return render(request, 'accounts/signup.html', {})
        else:
            return redirect(settings.SOCIAL_AUTH_LOGIN_REDIRECT_URL)