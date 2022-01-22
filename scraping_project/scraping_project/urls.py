from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('product.urls')),
]
