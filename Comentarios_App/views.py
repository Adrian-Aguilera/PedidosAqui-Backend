from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializer import ComentariosRestaurantesSerializer, ComentariosRestaurantesToolsSerializer, ComentariosMenusSerializer, ComentariosMenusToolsSerializer
from .models import ComentariosRestaurantes, ComentariosMenus
class ComentariosRestaurantesView(APIView):
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def ComentariosRestaurantesCrear(request):
        if request.method == 'POST':
            try:
                ''''La respuesta tiene que mandar el id del restaurante y el comentario'''
                data = request.data
                print(data)
                serializer = ComentariosRestaurantesSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'data':{
                        "restaurante": serializer.data['restaurante'],
                        "usuario": serializer.data['usuario'],
                        "comentario": serializer.data['comentario'],
                        "fecha": serializer.data['fecha'],
                        "puntaje": serializer.data['puntaje']
                    }})
                else:
                    return JsonResponse({'error': 'Error al crear el comentario'})
            except Exception as e:
                return JsonResponse({'error': f'Comentarios restaurantes error: {str(e)}'})

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def ComentariosRestaurantesListar(request, id=None):
        if request.method == 'GET':
            try:
                if id:
                    ''' Listar los comentarios de un usuario '''
                    comentarios = ComentariosRestaurantes.objects.filter(restaurante=id)
                else:
                    comentarios = ComentariosRestaurantes.objects.all()
                serializer = ComentariosRestaurantesToolsSerializer(comentarios, many=True)
                if len(serializer.data) == 0:
                    return JsonResponse({'data': None})
                return JsonResponse({'data': serializer.data})
            except Exception as e:
                return JsonResponse({'error': f'List comentarios restaurantes error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

class ComentariosMenusView(APIView):
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def ComentariosMenusCrear(request):
        if request.method == 'POST':
            try:
                ''''La respuesta tiene que mandar el id del restaurante y el comentario'''
                data = request.data
                print(data)
                serializer = ComentariosMenusSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'data':{
                        "menu": serializer.data['menu'],
                        "usuario": serializer.data['usuario'],
                        "comentario": serializer.data['comentario'],
                        "fecha": serializer.data['fecha'],
                        "puntaje": serializer.data['puntaje']
                    }})
                else:
                    return JsonResponse({'error': serializer.errors})
            except Exception as e:
                return JsonResponse({'error': f'Comentarios Menus error: {str(e)}'})

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def ComentariosMenusListar(request, id=None):
        if request.method == 'GET':
            try:
                if id:
                    ''' Listar los comentarios de un usuario '''
                    comentariosOfMenu = ComentariosMenus.objects.filter(restaurante=id)
                else:
                    comentariosOfMenu = ComentariosMenus.objects.all()
                serializer = ComentariosMenusToolsSerializer(comentariosOfMenu, many=True)
                if len(serializer.data) == 0:
                    return JsonResponse({'data': None})
                return JsonResponse({'data': serializer.data})
            except Exception as e:
                return JsonResponse({'error': f'List comentarios Menus error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})