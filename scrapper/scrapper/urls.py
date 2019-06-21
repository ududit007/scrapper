from django.contrib import admin
from django.urls import path, include
# from .views import hello
#from django.conf.urls import include, url


urlpatterns = [
    path('scrapy/', include('scrapy.urls')),
    path('admin/', admin.site.urls),
]
