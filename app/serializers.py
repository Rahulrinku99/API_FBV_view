from rest_framework import serializers
from app.models import *

class EmplyoeeMS(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

