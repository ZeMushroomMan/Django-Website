from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('cart/', views.cart_summary, name='cart_summary'),
    path('add/', views.cart_add, name='cart_add'),
    path('delete/', views.cart_delete, name='cart_delete'),
    path('update/', views.cart_update, name='cart_update'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmed/', views.payment_confirm, name='payment_confirm'),
    path('about/', views.about),
]
