from django.contrib import admin
from django.urls import path, include
from scrapy.views import home
# from .views import hello
#from django.conf.urls import include, url


urlpatterns = [
    path('', home),
    path('scrapy/', include('scrapy.urls')),
    path('admin/', admin.site.urls),
]
