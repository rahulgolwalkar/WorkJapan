from rest_framework import serializers
from . models import Address
# from . models import Company

# class CompanySerializer(serializers.ModelSerializer):
#     address = serializers.StringRelatedField(many=True, allow_null=True)
#     class Meta:
#         model = Company
#         # fields = ('name', 'description')
#         fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'