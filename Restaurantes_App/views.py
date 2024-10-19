from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from dotenv import load_dotenv
from asgiref.sync import sync_to_async, async_to_sync
import json
load_dotenv(override=True)
# Create your views here.

class RestaurantesMethods(APIView):
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def restaurantesListar(request):
        if request.method == 'GET':
            try:
                return JsonResponse({'data': 'Listado de restaurantes'})
            except Exception as e:
                return JsonResponse({'error': f'List restaurants error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})