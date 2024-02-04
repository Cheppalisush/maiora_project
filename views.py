from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import studentserializer


# Create your views here.
@api_view(['POST'])
def addstudent(request):
    serializer= studentserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)