from django.shortcuts import render
from rest_framework import viewsets,authentication,permissions
from .models import Sprint,Task
from .serializers import SprintSerializer,TaskSerializer,UserSerializer
from  django.contrib.auth import get_user_model




User=get_user_model()


class DefaultsMixin(object):
    authentication_classes=(
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permissions_classes=(
        permissions.IsAuthenticated,
    )
    paginate_ty=25
    paginate_by_param='page_size'
    max_paginate_by=100


class SprintViewSet(DefaultsMixin,viewsets.ModelViewSet):
    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer


class TaskViewSet(DefaultsMixin,viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(DefaultsMixin,viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer




