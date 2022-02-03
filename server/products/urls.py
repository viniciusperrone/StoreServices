from django.urls import re_path, path
from django.urls.resolvers import URLPattern
from products import views

urlpatterns = [
    path('home', views.get, name='home'),
    path('create-product', views.post, name='create-product'),
]