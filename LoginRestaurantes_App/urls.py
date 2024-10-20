from django.urls import path
from .views import RestaurantesLoginMethod

urlpatterns = [
    path('login/', RestaurantesLoginMethod.login, name='login'),
    path('crear/', RestaurantesLoginMethod.CreateCuenta, name='create'),
]