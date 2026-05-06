from . import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('product/<slug:slug>', views.product_detail, name="product_detail"),
    path('category_products/<slug:slug>', views.category_products, name="category_products"),
]
