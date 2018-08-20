from rest_framework import serializers
from models import FixedDataTable

class FixedDataTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=FixedDataTable
        fields=('name','category')