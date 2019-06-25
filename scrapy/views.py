from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render

from .constants import NON_USER
from .forms import UserRegisterForm
from .models import User


def create_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User.objects.create_user(name, email, password)
            return render(request, 'login.html')

        else:
            return render(request, 'register.html', {'form': form, 'data': request.POST})


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            print(user)
            return render(request, 'loggedIn.html')

        else:
            print("inside else")
            # return HttpResponse("Invalid Credentials.", status=401)
            return render(request, 'login.html', {'error': NON_USER})


def logout_user(request):
    logout(request)

    return render(request, 'home.html')










