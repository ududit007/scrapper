from django.urls import path
from django.views.generic import TemplateView
from .views import create_user


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('register/', TemplateView.as_view(template_name="register.html")),
    path('login/', TemplateView.as_view(template_name="login.html")),
    path('signup/', create_user),
]

