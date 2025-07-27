# from rest_framework import serializers
# from .models import Product, UserRegistration
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserRegistration
#         fields = '__all__'

from rest_framework import serializers
from myapiapp.models import Patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['patient_id','last_name','first_name','blood']