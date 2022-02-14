from django.urls import re_path, path
from django.urls.resolvers import URLPattern
from products.views import ProductsView

productsView = ProductsView

urlpatterns = [
    path('home', productsView.get),
    path('create/<str:id>', productsView.create),
    path('update/<str:id>', productsView.update),
    path('delete/<str:id>', productsView.delete),
]