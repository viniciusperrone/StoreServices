from django.urls import re_path
from django.urls.resolvers import URLPattern
from users import views

urlpatterns = [
    re_path(r'^register', views.UserView)
]
