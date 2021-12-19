from django.contrib.auth.models import Permission
from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .models import Parceiro
from .models import Xmls
from .models import StatusMaquinas
from rest_framework.response import Response
from .serializer import *
from django_filters  import rest_framework as filters
from rest_framework.decorators import action
from rest_framework import status
from django.http import HttpResponse
from django.http import Http404
from datetime import datetime, timedelta

class ParceiroFilter(filters.FilterSet):
    class Meta:
        model = Parceiro
        fields = (
            'cnpj','author','created'
        )        

class OrdensFilter(filters.FilterSet):
    class Meta:
        model = OrderEnvio
        #fields = ({
        #    'data':['gte', 'lte', 'exact', 'gt', 'lt']
        #})
        fields = {
            'data': ['exact']
        }

class CorretoraFilter(filters.FilterSet):
    class Meta:
        model = Corretora
        
        fields = (
            'usuario','created'
        )  
#
class OrdemStatusFilter(filters.FilterSet):
    class Meta:
        model = OrdemStatus
        fields = (
            'corretora_id','ordem_id','status'
        )    

class OrderCompraVendaFilter(filters.FilterSet):
    class Meta:
        model = OrderCompraVenda
        fields = (
            'id','status','created'
        )      

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostViewSet(viewsets.ModelViewSet):
 #  permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(pk=self.request.user.organisation_id)
        self.check_object_permissions(self.request, obj)
        return obj
class ParceiroListView(ListView):
    model = Parceiro

class ParceiroDetailView(DetailView):
    model = Parceiro

class ParceiroViewSet(viewsets.ModelViewSet):
   # permission_classes = [IsAuthenticated]
    queryset = Parceiro.objects.all()
    serializer_class = ParceiroSerializer
    filterset_class = ParceiroFilter

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class XmlsListView(ListView):
    model = Xmls

class XmlsDetailView(DetailView):
    model = Xmls

class XmlsViewSet(viewsets.ModelViewSet):
   # permission_classes = [IsAuthenticated]
    queryset = Xmls.objects.all()
    serializer_class = XmlsSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
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

class StatusMaquinasListView(ListView):
    model = StatusMaquinas

class StatusMaquinasDetailView(DetailView):
    model = StatusMaquinas

class StatusMaquinasViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = StatusMaquinas.objects.all()
    serializer_class = StatusMaquinasSerializer

class XmlsListView(ListView):
    model = Xmls

class XmlsDetailView(DetailView):
    model = Xmls

class OrderEnvioViewSet(viewsets.ModelViewSet):
    futuredate = datetime.now()
    queryset = OrderEnvio.objects.all().filter(data__gte=futuredate)
    serializer_class = OrderEnvioSerializer
  #  filterset_class = OrdensFilter
    
   # queryset.filter(data_at__gte=futuredate)
    

    @action(methods=['get'], detail=False)


    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
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

class CorretoraViewSet(viewsets.ModelViewSet):
    queryset = Corretora.objects.all()
    serializer_class = CorretoraSerializer
    filterset_class = CorretoraFilter

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
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

class OrdemStatusViewSet(viewsets.ModelViewSet):
    queryset = OrdemStatus.objects.all()
    serializer_class = OrdemStatusSerializer
    filterset_class = OrdemStatusFilter

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
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

class EstrategiasViewSet(viewsets.ModelViewSet):
    queryset = Estrategias.objects.all()
    serializer_class = EstrategiasSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
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

class RequicaoEstViewSet(viewsets.ModelViewSet):
    queryset = RequicaoEst.objects.all()
    serializer_class = RequicaoEstSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
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

class OrderCompraVendaViewSet(viewsets.ModelViewSet):
    queryset = OrderCompraVenda.objects.all()
    serializer_class = OrderCompraVendaSerializer
    filterset_class = OrderCompraVendaFilter
    
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
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