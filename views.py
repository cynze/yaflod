from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Family
from .serializers import FamilySerializer


@api_view(['GET', 'POST'])
def family_list(request):
    if request.method == 'GET':
        families = Family.objects.all()
        serializer = FamilySerializer(families, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def family_detail(request, pk):
    try:
        country = Family.objects.get(pk=pk)
    except Family.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FamilySerializer(country)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FamilySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
