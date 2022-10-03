from http.client import ResponseNotReady
from re import T
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from supers import serializers

@api_view(['GET', 'POST'])
def Supers_list(request):
    if request.method == 'GET':
        super_types_type = request.query_params.get('super_type')
        print(super_types_type)
        queryset = Super.objects.all()
        if super_types_type:
            queryset = queryset.filter(super_type__type=super_types_type)
        else:
            supers = Super.objects.all()
            hero = supers.filter(super_type__type = 'hero')
            villian = supers.filter(super_type__type = 'villian')
            hero_serialized = SuperSerializer(hero,many=True)
            villain_serialized = SuperSerializer(villian,many=True)
            custom_response = {
                'heroes':hero_serialized.data,
                'villains':villain_serialized.data
            }
            return Response(custom_response)

        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def Supers_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


