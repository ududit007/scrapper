from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from .views import create_user, login_user, logout_user, scrap, home, activate
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('register/', TemplateView.as_view(template_name="register.html")),
    path('login/', TemplateView.as_view(template_name="login.html")),
    path('signup/', create_user, name='signup'),
    path('login_user/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout'),
    path('scrap/', scrap, name='scrap'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate')
]

