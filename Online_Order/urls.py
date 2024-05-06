from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:restaurant_id>/menu/', views.menu_list, name='menu_list'),
    path('restaurants/<int:restaurant_id>/order/', views.place_order, name='place_order'),
]
