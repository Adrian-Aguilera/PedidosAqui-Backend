from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from dotenv import load_dotenv
from asgiref.sync import sync_to_async, async_to_sync
import json
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UsuariosSerializerAutenticado, UsuariosSerializer
load_dotenv(override=True)

# Create your views here.

class LoginMethod(APIView):
    @api_view(['POST'])
    def login(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            correo = data['correo']
            password = data['password']
            try:
                serializer = UsuariosSerializerAutenticado()
                tokensObtenidos = serializer.validate(attrs={'correo': correo, 'password': password})
                return JsonResponse({"data":{
                    "refresh": tokensObtenidos['refresh'],
                    "access": tokensObtenidos['access'],
                    "correo": tokensObtenidos['correo'],
                    "usuarioID": tokensObtenidos['idUsuario'],
                    "nombre": tokensObtenidos['nombre']
                }})
            except Exception as e:
                return JsonResponse({'error': f'Login error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    def CreateCuenta(request):
        if request.method == 'POST':
            data = request.data
            try:
                serializer = UsuariosSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'data': 'Cuenta creada exitosamente'})
                else:
                    return JsonResponse({'error': 'Error al crear la cuenta'})
            except Exception as e:
                return JsonResponse({'error': f'Create account error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})
class PerfilTokenObtainPairView(TokenObtainPairView):
    serializer_class = UsuariosSerializerAutenticado
