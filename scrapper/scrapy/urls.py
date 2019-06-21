from django.urls import path
from django.views.generic import TemplateView
from .views import IndexView


urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('', TemplateView.as_view(template_name="index.html")),
    path('register/', TemplateView.as_view(template_name="register.html")),
    path('login/', TemplateView.as_view(template_name="login.html")),
]
