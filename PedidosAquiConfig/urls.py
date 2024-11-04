"""
URL configuration for PedidosAquiConfig project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#añadiendo las urls al documentacion swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API de Pedidos Aqui",
      default_version='v1',
      description="Documentación de la API para Pedidos Aqui",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="adrian.aguilera23@itca.edu.sv"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginMethods/api/', include('Login_App.urls')),
    path('restaurantesLoginMethods/api/', include('LoginRestaurantes_App.urls')),
    path('restaurantesMethods/api/', include('Restaurantes_App.urls')),
    path('pedidosMethods/api/', include('Pedidos_App.urls')),
    path('comentariosMethods/api/', include('Comentarios_App.urls')),

    #rutas para obtener tokens con direccion al modelo Users por defecto de django:
    path('tokens/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokens/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #rutas de swagger:
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
