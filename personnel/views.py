from django.shortcuts import render
from .serializers import (DepartmentSerializer,
                        PersonnelSerializer)
from .models import (
    Department,
    Personnel)
from rest_framework.generics import (ListCreateAPIView, 
                                    RetrieveUpdateDestroyAPIView)

class DepartmentListCreateView(ListCreateAPIView):
    queryset= Department.objects.all()
    serializer_class=DepartmentSerializer

class DepartmentRUDview(RetrieveUpdateDestroyAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer    

class PersonnelListCreateView(ListCreateAPIView):
    queryset= Personnel.objects.all()
    serializer_class=PersonnelSerializer

class PersonnelRUDview(RetrieveUpdateDestroyAPIView):
    queryset=Personnel.objects.all()
    serializer_class=PersonnelSerializer    