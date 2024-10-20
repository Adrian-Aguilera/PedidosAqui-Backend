from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from dotenv import load_dotenv
from asgiref.sync import sync_to_async, async_to_sync
import json
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UsuariosSerializerAutenticado, UsuariosSerializer, UsuariosSerializerInList
from .models import Usuarios
load_dotenv(override=True)


class CotrollerInterface:
    def __init__(self):
        self.usuarios = Usuarios.objects.all()

    def listarUsuarios(self):
        try:
            serializer = UsuariosSerializerInList(self.usuarios, many=True)
            usuarios = serializer.data
            return usuarios
        except Exception as e:
            return f'Error: {str(e)}'
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
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def perfil(request):
        if request.method == 'POST':
            try:
                usuario = Usuarios.objects.get(id=request.user.id)
                serializer = UsuariosSerializerInList(usuario)
                return JsonResponse({'data': serializer.data})
            except Exception as e:
                return JsonResponse({'error': f'Get profile error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['GET'])
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

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def EditarUsuario(request):
        if request.method == 'POST':
            try:
                usuario_id = request.data.get('id')
                try:
                    usuario = Usuarios.objects.get(id=usuario_id)
                except Usuarios.DoesNotExist:
                    return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

                # Serializar y validar los datos de entrada
                serializer = UsuariosSerializerInList(usuario, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'data': {
                        "id": usuario.id,
                        "nombre": serializer.validated_data.get('nombre', usuario.nombre),
                        "correo": serializer.validated_data.get('correo', usuario.correo),
                        "apellido": serializer.validated_data.get('apellido', usuario.apellido),
                    }})
                else:
                    return JsonResponse({'error': 'Error al modificar el usuario'})
            except Exception as e:
                return JsonResponse({'error': f'Create account error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})
class PerfilTokenObtainPairView(TokenObtainPairView):
    serializer_class = UsuariosSerializerAutenticado
