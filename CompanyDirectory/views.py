from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Address
from . serializers import AddressSerializer
from django.http import Http404
from django.db import models

# from . models import Company
# from . serializers import CompanySerializer




class AddressList(APIView):
    def get(self, request, format=None):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressObject(APIView):
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        pk = request.query_params['companyName']
        address = self.get_object(pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, format=None):
        pk = request.data['companyName']
        address = self.get_object(pk)
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        pk = request.data['companyName']
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CityAddressList(APIView):
    def get(self, request, format=None):
        city = request.query_params['city']
        results = Address.objects.filter(city=city)
        serializer = AddressSerializer(results, many=True)
        return Response(serializer.data)

class CommonPostalCodes(APIView):
    def get(self, request, format=None):
        count = request.query_params['count']
        qs = Address.objects.values('postalCode').annotate(count=models.Count('postalCode')).filter(count__gte = count)
        return Response(qs)

# class CompanyList(APIView):
#     def get(self, request):
#         company1 = Company.objects.all()
#         serializer = CompanySerializer(company1, many=True)
#         return Response(serializer.data)



