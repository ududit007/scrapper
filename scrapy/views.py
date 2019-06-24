from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render

from .models import User


def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(name, email, password)

        return HttpResponse('Ok')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return HttpResponse('Ok')

        else:
            return HttpResponse("Invalid Credentials.", status=401)






# def logout_user():



