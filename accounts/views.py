from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.user.is_anonymous:
        return render(request, 'accounts/login.html', {})
    else:
        return redirect('/admin/')
