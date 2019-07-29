from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from .views import Activate, Signup, Logout, Scrap, Login, Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', TemplateView.as_view(template_name="register.html"), name='register'),
    path('login/', TemplateView.as_view(template_name="login.html"), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login_user/', Login.as_view(), name='login_user'),
    path('logout/', Logout.as_view(), name='logout'),
    path('scrap/', Scrap.as_view(), name='scrap'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        Activate.as_view(), name='activate')
]
