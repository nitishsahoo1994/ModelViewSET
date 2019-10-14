from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from restapp.models import Employee
from restapp.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class =EmployeeSerializer
    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]