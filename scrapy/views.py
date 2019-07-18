from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.cache import cache
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Model
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.cache import cache_page

from .constants import NON_USER, FLIPKART, AMAZON
from .forms import UserRegisterForm
from .models import User, ScrappedData
from .utils import scrap_amazon, scrap_flipkart
from scrapper import settings
from .tokens import account_activation_token


def create_user(request):
    try:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)

            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = form.save(commit=False)
                user.set_password(password)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                message = render_to_string('acc_active.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

                send_mail("Scrapper Verification", message, settings.local.DEFAULT_FROM_EMAIL, [email])
                # print("exception occured")
                # User.objects.create_user(email, name=name, password=password)
                # return HttpResponse('Please confirm your email address to complete the registration')
                return redirect('/scrapy/login/')

            else:
                return render(request, 'register.html', {'form': form, 'data': request.POST})
    except Exception as e:
        print(e)


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
@cache_page(60 * 15)
def scrap(request):
    if request.method == 'GET':
        cache._cache.flush_all()
        q = request.GET.get('search')
        if q is None:
            return redirect('home')
        q1 = q.replace(' ', '_')
        flipkart_data = cache.get(q1 + 'flipkart')
        amazon_data = cache.get(q1 + 'amazon')

        if not flipkart_data and not amazon_data:
            flipkart_data = ScrappedData.objects.filter(keyword=q, source='flipkart')
            amazon_data = ScrappedData.objects.filter(keyword=q, source='amazon')
            q2 = q.replace(' ', '_')
            cache.set(q2+'flipkart', flipkart_data)
            cache.set(q2+'amazon', amazon_data)
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


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')










