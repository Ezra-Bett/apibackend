# from  rest_framework import viewsets
# from .models import Product, UserRegistration
# from .serializer import ProductSerializer, UserRegistrationSerializer

# # Create your views here.
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class UserRegistrationViewSet(viewsets.ModelViewSet):
#     queryset = UserRegistration.objects.all()
#     serializer_class = UserRegistrationSerializer

from django.shortcuts import render
from rest_framework import viewsets
from myapiapp.models import Patient
from myapiapp.serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer