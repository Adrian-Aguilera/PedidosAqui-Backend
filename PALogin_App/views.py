from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from dotenv import load_dotenv
from asgiref.sync import sync_to_async, async_to_sync
import json
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UsuariosSerializer
load_dotenv(override=True)

# Create your views here.

class LoginMethod(APIView):
    permission_classes = [IsAuthenticated]
    @api_view(['POST'])
    def login(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            correo = data['email']
            password = data['password']
            try:
                serializer = UsuariosSerializer()
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

class PerfilTokenObtainPairView(TokenObtainPairView):
    serializer_class = UsuariosSerializer
