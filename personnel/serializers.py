from rest_framework import serializers
from .models import Department, Personnel

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'name',
        )

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = (
            'first_name',
            'last_name',
            'title',
        )


