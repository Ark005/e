from django.urls import path
from cart.views import add_to_cart, remove_from_cart, CartView, decreaseCart
from . views import home, ProductDetail, Home, postFriend, checkNickName,indexView
app_name= 'mainapp'

urlpatterns = [

    path('', home, name='home'),
    path('p', Home.as_view(), name='home'),
    path('product/<slug>/', indexView, name='product'),
    path('cart/', CartView, name='cart-home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('decrease-cart/<slug>', decreaseCart, name='decrease-cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
  
]


