from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from user import views


urlpatterns = [
    path('signup', views.UserRegister),
]