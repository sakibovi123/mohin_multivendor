from django.urls import path

from Cart.views import *
from Cart import views


urlpatterns = [
    path('cartview/', views.cart_details, name="cart_details"),
]