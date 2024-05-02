from django.urls import path
from restaurant.views import ajoutTypeRestaurant, ajoutRestaurant

urlpatterns = [
    path('ajoutTypeRestaurant/', ajoutTypeRestaurant.as_view(), name='ajoutTypeRestaurant'),
    path('ajoutRestaurant/', ajoutRestaurant.as_view(), name='ajoutRestaurant'),
]