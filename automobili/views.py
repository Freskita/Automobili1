from django.http import JsonResponse
from .models import Marca, Cliente, Auto, Concessionario, Acquisto
from .serializers import MarcaSerializer, ClienteSerializer, AutoSerializer, ConcessionarioSerializer, AcquistoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def marca_listino(request):

    if request.method == 'GET':
        marche = Marca.objects.all()
        serializer = MarcaSerializer(marche, many=True)
        return JsonResponse({'marca': serializer.data})
    
    if request.method == 'POST':
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
    
    elif request.method == 'PUT': 
        serializer = MarcaSerializer(marche, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def marca_dettaglio(request, id):

    try: 
        Marca.objects.get(pk=id)
    except Marca.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
   

    if request.method == 'GET': 
        serializer = MarcaSerializer(marca_dettaglio)
        return Response(serializer.data)

    elif request.method == 'PUT': 
        serializer = MarcaSerializer(marca_dettaglio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        marca_dettaglio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def clienti_listino(request):

    if request.method == 'GET':
        clienti = Cliente.objects.all()
        serializer = ClienteSerializer(clienti, many=True)
        return JsonResponse({'clienti': serializer.data})

    if request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 

@api_view(['GET', 'POST'])
def auto_listino(request):

    if request.method == 'GET':
        autos = Auto.objects.all()
        serializer = AutoSerializer(autos, many=True)
        return JsonResponse({'autos': serializer.data})
    
    if request.method == 'POST':
        serializer = AutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 

@api_view(['GET', 'POST', ])
def concessionari_listino(request):
    if request.method == 'GET':
        concessionari = Concessionario.objects.all()
        serializer = ConcessionarioSerializer(concessionari, many=True)
        return JsonResponse({'concessionari': serializer.data})
    
    if request.method == 'POST':
        serializer = ConcessionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        

@api_view(['GET', 'POST'])
def acquisti_listino(request):

    if request.method == 'GET':
        acquisti = Acquisto.objects.all()
        serializer = AcquistoSerializer(acquisti, many=True)
        return JsonResponse({'acquisti': serializer.data})
    
    if request.method == 'POST':
        serializer = AcquistoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        

        



