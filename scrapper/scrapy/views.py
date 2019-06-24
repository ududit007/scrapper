from django.http import HttpResponse
from django.shortcuts import render
from scrapy.models import User

def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create(
            name = name,
            email = email,
            password = password
        )
        return HttpResponse('')
