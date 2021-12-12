from django.contrib.auth.models import Permission
from django.contrib import admin
from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import MyUser
from rest_framework.response import Response
from .serializer import *
from django_filters  import rest_framework as filters
from rest_framework.decorators import action
from rest_framework import status
from django.http import HttpResponse
from django.http import Http404

class UserFilter(filters.FilterSet):
    class Meta:
        model = MyUser
        fields = {
            'email': ['icontains'],
        }

class UserListView(ListView):
    model = MyUser

class UserDetailView(DetailView):
    model = MyUser

class UserViewSet(viewsets.ModelViewSet):
  #  permission_classes = [IsAuthenticated]
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('last_login').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        