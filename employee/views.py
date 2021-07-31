from rest_framework import viewsets
from employee.serializers import UserSerializer, OrderSerializer, ProjectSerializer
from employee.models import *
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()

