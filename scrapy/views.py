import json

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.cache import cache
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import ScrappedSerializer, UserSerializer

from .constants import NON_USER, FLIPKART, AMAZON
from .forms import UserRegisterForm
from .models import User, ScrappedData
from .utils import scrap_amazon, scrap_flipkart, scrap_flipkart2
from .tokens import account_activation_token
from rest_framework.authentication import SessionAuthentication


class Signup(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        current_site = get_current_site(self.request)
        message = render_to_string('acc_active.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        send_mail(
            "Scrapper Verification", message, settings.DEFAULT_FROM_EMAIL,
            [user.email], fail_silently=True
        )
        Response({'msg': "Your account has been activated"})


class Login(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            data = {
                'url': reverse('home', request=request)
            }

            return Response(data)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Logout(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print(request.user)
        logout(request)

        return redirect('home')


class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'loggedIn.html')

        return render(request, 'home.html')


class Scrap(RetrieveAPIView):
    serializer_class = ScrappedSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        q = request.query_params.get('search')
        q1 = q.replace(' ', '_')
        flipkart_queryset = cache.get(q1 + 'flipkart')
        amazon_queryset = cache.get(q1 + 'amazon')
        if not flipkart_queryset and not amazon_queryset:
            flipkart_queryset = ScrappedData.objects.filter(keyword=q, source='flipkart')
            amazon_queryset = ScrappedData.objects.filter(keyword=q, source='amazon')
            q2 = q.replace(' ', '_')
            cache.set(q2 + 'flipkart', flipkart_queryset)
            cache.set(q2 + 'amazon', amazon_queryset)

        if not flipkart_queryset and not amazon_queryset:
            all_data = []
            flipkart_list = scrap_flipkart(q)
            if not flipkart_list:
                flipkart_list = scrap_flipkart2(q)
            amazon_list = scrap_amazon(q)
            # print(flipkart_list, amazon_list)
            # if not flipkart_list and not amazon_list:
            #     return redirect('home')

            for flipkart_dict in flipkart_list:
                all_data.append(ScrappedData(**flipkart_dict))

            for amazon_dict in amazon_list:
                all_data.append(ScrappedData(**amazon_dict))

            ScrappedData.objects.bulk_create(all_data)

            flipkart_queryset = ScrappedData.objects.filter(keyword=q, source='flipkart')

            amazon_queryset = ScrappedData.objects.filter(keyword=q, source='amazon')

        flipkart_data = self.serializer_class(flipkart_queryset, many=True).data
        amazon_data = self.serializer_class(amazon_queryset, many=True).data
        # flipkart_data = json.dumps(flipkart_data)
        # amazon_data = json.dumps(amazon_data)
        # paginator_flipkart = Paginator(flipkart_data, 2)
        # paginator_amazon = Paginator(amazon_data, 2)
        # page_flipkart = request.GET.get('page_flipkart')
        # page_amazon = request.GET.get('page_amazon')
        # data_list_flipkart = paginator_flipkart.get_page(page_flipkart)
        # data_list_amazon = paginator_amazon.get_page(page_amazon)

        return Response({'data_list_flipkart': flipkart_data, 'data_list_amazon': amazon_data, 'q': q})

# class Scrap(View):
#
#     decorator_list = [login_required, cache_page(60*60*24)]
#     @method_decorator(decorator_list)
#     def get(self, request):
#         if request.method == 'GET':
#             # cache._cache.flush_all()
#             q = request.GET.get('search')
#             if q is None:
#                 return redirect('home')
#             q1 = q.replace(' ', '_')
#             flipkart_data = cache.get(q1 + 'flipkart')
#             amazon_data = cache.get(q1 + 'amazon')
#
#             if not flipkart_data and not amazon_data:
#                 flipkart_data = ScrappedData.objects.filter(keyword=q, source='flipkart')
#                 amazon_data = ScrappedData.objects.filter(keyword=q, source='amazon')
#                 q2 = q.replace(' ', '_')
#                 cache.set(q2+'flipkart', flipkart_data)
#                 cache.set(q2+'amazon', amazon_data)
#             if not flipkart_data and not amazon_data:
#                 all_data = []
#                 flipkart_list = scrap_flipkart(q)
#                 if not flipkart_list:
#                     flipkart_list = scrap_flipkart2(q)
#                 amazon_list = scrap_amazon(q)
#                 print(flipkart_list,amazon_list)
#                 if not flipkart_list and not amazon_list:
#                     return redirect('home')
#
#                 for flipkart_dict in flipkart_list:
#                     all_data.append(ScrappedData(**flipkart_dict))
#
#                 for amazon_dict in amazon_list:
#                     all_data.append(ScrappedData(**amazon_dict))\
#
#                 ScrappedData.objects.bulk_create(all_data)
#
#                 flipkart_data = ScrappedData.objects.filter(keyword=q, source='flipkart')
#                 amazon_data = ScrappedData.objects.filter(keyword=q, source='amazon')
#
#             paginator_flipkart = Paginator(flipkart_data, 2)
#             paginator_amazon = Paginator(amazon_data, 2)
#             page_flipkart = request.GET.get('page_flipkart')
#             page_amazon = request.GET.get('page_amazon')
#             data_list_flipkart = paginator_flipkart.get_page(page_flipkart)
#             data_list_amazon = paginator_amazon.get_page(page_amazon)
#
#             return render(request, 'loggedIn.html', {'data_list_flipkart': data_list_flipkart, 'data_list_amazon': data_list_amazon,'q': q})


class Activate(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs.get('uidb64')))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, kwargs.get('token')):
            user.is_active = True
            user.save()
            return Response({'msg': 'Thank you for your email confirmation. Now you can login your account.'})
        else:
            return HttpResponse('Activation link is invalid!')










