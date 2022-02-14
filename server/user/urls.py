from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from user.views import UserView

userView = UserView

urlpatterns = [
    path('signup', userView.create),
    path('signin', userView.login),
]