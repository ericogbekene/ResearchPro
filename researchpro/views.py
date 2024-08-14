from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Department, Project, Writer, HireWriter
from .serializers import DepartmentSerializer, ProjectSerializer, WriterSerializer, HireWriterSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class HireWriterViewSet(viewsets.ModelViewSet):
    queryset = HireWriter.objects.all()
    serializer_class = HireWriterSerializer