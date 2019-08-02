from django.urls import path

from .views import HomePageView, charge

urlpatterns = [
    path('', HomePageView.as_view(), name='payment'),
    path('charge/', charge, name='charge'),
]