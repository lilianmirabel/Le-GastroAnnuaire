from django.urls import path
from restaurant.views import ajoutTypeRestaurant

urlpatterns = [
    path('ajoutTypeRestaurant/', ajoutTypeRestaurant.as_view(), name='ajoutTypeRestaurant'),
]