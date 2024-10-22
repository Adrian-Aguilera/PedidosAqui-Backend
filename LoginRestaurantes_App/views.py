from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from dotenv import load_dotenv
from asgiref.sync import sync_to_async, async_to_sync
import json
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UsuariosRestaurantesSerializerAutenticado, UsuariosRestaurantesSerializer, UsuariosRestaurantesSerializerInList
from .models import RestaurantesUsuarios


class CotrollerInterface:
    def __init__(self):
        self.usuarios = RestaurantesUsuarios.objects.all()

    def listarUsuarios(self):
        try:
            serializer = UsuariosRestaurantesSerializerInList(self.usuarios, many=True)
            usuarios = serializer.data
            return usuarios
        except Exception as e:
            return f'Error: {str(e)}'

class RestaurantesLoginMethod(APIView):
    '''
        {
            "correo": "res@gmail.com",
            "password": "123"
        }
    '''
    @api_view(['POST'])
    def login(request):
        if request.method == 'POST':
            data = request.data
            correo = data['correo']
            password = data['password']
            try:
                serializer = UsuariosRestaurantesSerializerAutenticado()
                tokensObtenidos = serializer.validate(attrs={'correo': correo, 'password': password})
                return JsonResponse({"data":{
                    "refresh": tokensObtenidos['refresh'],
                    "access": tokensObtenidos['access'],
                    "correo": tokensObtenidos['correo'],
                    "restauranteID": tokensObtenidos['restauranteID'],
                    "nombre": tokensObtenidos['nombre']
                }})
            except Exception as e:
                return JsonResponse({'error': f'Login error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})


    '''
        {
            "nombre":"Restaurante1",
            "correo": "res@gmail.com",
            "password": "123"
        }
    '''
    @api_view(['POST'])
    def CreateCuenta(request):
        if request.method == 'POST':
            data = request.data
            try:
                serializer = UsuariosRestaurantesSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'data': {
                        "status": 200,
                        "mensaje": "Cuenta creada exitosamente",
                    }})
                else:
                    return JsonResponse({'error': 'Error al crear la cuenta'})
            except Exception as e:
                return JsonResponse({'error': f'Create account error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def perfil(request):
        if request.method == 'GET':
            try:
                usuario = RestaurantesUsuarios.objects.get(id=request.user.id)
                serializer = UsuariosRestaurantesSerializerInList(usuario)
                return JsonResponse({'data': serializer.data})
            except Exception as e:
                return JsonResponse({'error': f'Get profile error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def EditarUsuario(request):
        if request.method == 'POST':
            try:
                usuario_id = request.data.get('id')
                try:
                    usuario = RestaurantesUsuarios.objects.get(id=usuario_id)
                except RestaurantesUsuarios.DoesNotExist:
                    return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

                # Serializar y validar los datos de entrada
                serializer = UsuariosRestaurantesSerializerInList(usuario, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'data': {
                        "id": usuario.id,
                        "nombre": serializer.validated_data.get('nombre', usuario.nombre),
                        "correo": serializer.validated_data.get('correo', usuario.correo),
                    }})
                else:
                    return JsonResponse({'error': 'Error al modificar el usuario'})
            except Exception as e:
                return JsonResponse({'error': f'Create account error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def listarUsuarios(request):
        if request.method == 'GET':
            try:
                controllerInterface = CotrollerInterface()
                usuarios = controllerInterface.listarUsuarios()
                return JsonResponse({'data': usuarios})
            except Exception as e:
                return JsonResponse({'error': f'List users error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})