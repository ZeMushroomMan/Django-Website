from django.urls import path

from . import views

app_name='store'

urlpatterns = [
    path('products/',views.products, name='products'),
    path('', views.home),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list')
]