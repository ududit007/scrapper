from django.contrib import admin
from django.urls import path, include
from scrapy.views import Home


urlpatterns = [
    path('', Home.as_view()),
    path('scrapy/', include('scrapy.urls')),
    path('admin/', admin.site.urls),
]
