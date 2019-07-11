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

            User.objects.create_user(name, email, password)
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


def get_json_data(existing_data):

    flipkart_data = []
    amazon_data = []
    for data in existing_data:
        data_dict = {
            'keyword': data.keyword,
            'name': data.name,
            'actual_price': data.actual_price,
            'selling_price': data.selling_price,
            'rating': data.rating,
            'image': data.image,
            'link_product': data.link_product,

        }
        if data.source == FLIPKART:
            flipkart_data.append(data_dict)

        else:
            amazon_data.append(data_dict)

    return json.dumps({'flipkart': flipkart_data, 'amazon': amazon_data})


@login_required
def scrap(request):
    if request.method == 'GET':
        q = request.GET.get('search')

        existing_data = ScrappedData.objects.filter(keyword=q)

        if existing_data:
            json_data = get_json_data(existing_data)
            return HttpResponse(json_data)

        else:
            all_data = []
            flipkart_list = scrap_flipkart(q)
            amazon_list = scrap_amazon(q)

            for flipkart_dict in flipkart_list:
                all_data.append(ScrappedData(**flipkart_dict))

            for amazon_dict in amazon_list:
                all_data.append(ScrappedData(**amazon_dict))

            ScrappedData.objects.bulk_create(all_data)

            json_data = json.dumps({'flipkart': flipkart_list, 'amazon': amazon_list})

            return HttpResponse(json_data)

#
# def listing(request):
#     scrap_list = ScrappedData.objects.all()
#     paginator = Paginator(scrap_list, 4)
#
#     page = request.GET.get('page')
#     scraps = paginator.get_page(page)
#
#     return render(request, 'loggedIn.html', {'scraps': scraps})
#








