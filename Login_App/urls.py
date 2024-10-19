from django.urls import path
from .views import LoginMethod

urlpatterns = [
    path('login/', LoginMethod.login, name='login'),
    path('create/', LoginMethod.CreateCuenta, name='create'),
]