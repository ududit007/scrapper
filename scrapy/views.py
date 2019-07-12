import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .constants import NON_USER, FLIPKART, AMAZON
from .forms import UserRegisterForm
from .models import User, ScrappedData
from .utils import scrap_amazon, scrap_flipkart


def create_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User.objects.create_user(email, name=name, password=password)
            return render(request, 'login.html')

        else:
            return render(request, 'register.html', {'form': form, 'data': request.POST})


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect('/scrapy/')

        else:
            # return HttpResponse("Invalid Credentials.", status=401)
            return render(request, 'login.html', {'error': NON_USER})


@login_required
def logout_user(request):
    logout(request)

    return redirect('/scrapy/')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'loggedIn.html')

    return render(request, 'home.html')


@login_required
def scrap(request):
    if request.method == 'GET':
        q = request.GET.get('search')

        flipkart_data = ScrappedData.objects.filter(keyword=q, source='flipkart')
        amazon_data = ScrappedData.objects.filter(keyword=q, source='amazon')

        if not flipkart_data and not amazon_data:
            all_data = []
            flipkart_list = scrap_flipkart(q)
            amazon_list = scrap_amazon(q)

            for flipkart_dict in flipkart_list:
                all_data.append(ScrappedData(**flipkart_dict))

            for amazon_dict in amazon_list:
                all_data.append(ScrappedData(**amazon_dict))

            ScrappedData.objects.bulk_create(all_data)

            # existing_data = ScrappedData.objects.filter(keyword=q)
            flipkart_data = ScrappedData.objects.filter(keyword=q, source='flipkart')
            amazon_data = ScrappedData.objects.filter(keyword=q, source='amazon')

        paginator_flipkart = Paginator(flipkart_data, 2)
        paginator_amazon = Paginator(amazon_data, 2)
        page_flipkart = request.GET.get('page_flipkart')
        page_amazon = request.GET.get('page_amazon')
        data_list_flipkart = paginator_flipkart.get_page(page_flipkart)
        data_list_amazon = paginator_amazon.get_page(page_amazon)

        return render(request, 'loggedIn.html', {'data_list_flipkart': data_list_flipkart, 'data_list_amazon': data_list_amazon,'q': q})









