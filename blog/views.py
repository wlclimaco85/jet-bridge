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
from django.db import connection

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
            'id': ['lt']
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
            'id','ordem_id','ticket','status','created','corretora_id'
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
    start_date =  datetime(futuredate.year, futuredate.month, futuredate.day, 9, 00, 32, 11)
    end_date = datetime(futuredate.year, futuredate.month, futuredate.day, 19, 00, 32, 11)
    queryset = OrderEnvio.objects.filter(data__range=(start_date, end_date))
    #queryset = OrderEnvio.objects.raw('SELECT id,name,pages FROM app_books WHERE pages=')# OrderEnvio.objects.filter(data__range=(start_date, end_date))
   # queryset = OrderEnvio.objects.all()#.filter(data__gte=futuredate)
    serializer_class = OrderEnvioSerializer
    filterset_class = OrdensFilter
    
   # queryset.filter(data_at__gte=futuredate)
    

    @action(methods=['get'], detail=False)

    def my_custom_sql(self, request):
        return OrderEnvio.objects.raw('SELECT id,name,pages FROM app_books WHERE pages='+request.id)



    def newest(self, request):
        newest = self.get_queryset().order_by('data').last()
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
   # futuredate = datetime.now()
   # start_date =  datetime(futuredate.year, futuredate.month, futuredate.day, 9, 00, 32, 11)
   #end_date = datetime.now()
   # queryset = OrdemStatus.objects.filter(data__range=(start_date, end_date))
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

class CustonResponse001ViewSet(viewsets.ModelViewSet):
    # queryset = CustonResponse001.objects.raw("SELECT corretora_id_id, ordem_id_id FROM Blog_ordercompravenda WHERE ordem_id_id is not null and status not in ('E','Z','D')")
    
    #queryset = CustonResponse001.objects.all()
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    
    
    from collections import namedtuple
    c = connection.cursor()
    try:
        c.execute("SELECT R.corretora_id_id as corretora_id, R.ordem_id_id as ordem_id ,R.STATUS as status, gg.nome as corretora FROM Blog_ordercompravenda R LEFT JOIN BLOG_ORDERENVIO O ON (R.ordem_id_id = O.ID) LEFT JOIN BLOG_REQUICAOEST E ON (R.ordem_id_id = E.ordem_id_id) LEFT JOIN BLOG_ESTRATEGIAS Gg ON (E.estr_id_id = Gg.id)     WHERE GG.NOME IS NOT NULL and r.id = 618 order by r.data_compra")
        row = dictfetchall(c)
    finally:
        c.close()
    
    queryset = row
    serializer_class = CustonResponse001Serializer
    def dictfetchall3(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def get_queryset(self):
        from collections import namedtuple
       # cc = connection.cursor()
        
        id = self.request.query_params.get('id_parada')
        latitude= self.request.query_params.get('corretora_id')
        radius = self.request.query_params.get('status')
        estrategia = self.request.query_params.get('estrategia')
        from collections import namedtuple
        cc = connection.cursor()
       # try:
        quert = "SELECT R.corretora_id_id as corretora_id, R.ordem_id_id as ordem_id ,R.STATUS as status, gg.nome as corretora FROM Blog_ordercompravenda R LEFT JOIN BLOG_ORDERENVIO O ON (R.ordem_id_id = O.ID) LEFT JOIN BLOG_REQUICAOEST E ON (R.ordem_id_id = E.ordem_id_id) LEFT JOIN BLOG_ESTRATEGIAS Gg ON (E.estr_id_id = Gg.id)     WHERE GG.NOME IS NOT NULL "
        if(id):
            quert = quert + "and r.id = "+id
        if(latitude):
            quert = quert + "and r.corretora_id_id = "+latitude
        if(radius):
            quert = quert + "and r.STATUS = '"+radius+"'"
        
        if(radius):
            quert = quert + "and gg.nome = '"+estrategia+"'"

        quert = quert + " order by r.data_compra"
        cc.execute(quert)
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cc.description]
        aa = [
            dict(zip(columns, row))
            for row in cc.fetchall()
        ]
        queryset = aa
      #  finally:
        cc.close()
       # queryset = row #Model.objects.filter(location__distance_lte=(location, D(m=distance))).distance(location).order_by('distance')

        return queryset

    def dictfetchall4(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
   # def my_custom_sql():
    #    from django.db import connection, transaction

     #   c = connection.cursor()
      #  try:
       #     c.execute("SELECT R.corretora_id_id as corretora_id, R.ordem_id_id ,R.STATUS, gg.nome FROM Blog_ordercompravenda R LEFT JOIN BLOG_ORDERENVIO O ON (R.ordem_id_id = O.ID) LEFT JOIN BLOG_REQUICAOEST E ON (R.ordem_id_id = E.ordem_id_id) LEFT JOIN BLOG_ESTRATEGIAS Gg ON (E.estr_id_id = Gg.id)     WHERE GG.NOME IS NOT NULL  order by r.data_compra")
        #    row = c.fetchall
        #finally:
         #   c.close()


        # Data modifying operation - commit required
      #  cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
       # transaction.commit_unless_managed()

        # Data retrieval operation - no commit required
        #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        

        #return row
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    @action(methods=['get'], detail=True)
    def newest(self, request):
        
        id_parada = request.GET.get("id_parada", "")
        c = connection.cursor()
        try:
            c.execute("SELECT R.corretora_id_id as corretora_id, R.ordem_id_id as ordem_id ,R.STATUS as status, gg.nome as corretora FROM Blog_ordercompravenda R LEFT JOIN BLOG_ORDERENVIO O ON (R.ordem_id_id = O.ID) LEFT JOIN BLOG_REQUICAOEST E ON (R.ordem_id_id = E.ordem_id_id) LEFT JOIN BLOG_ESTRATEGIAS Gg ON (E.estr_id_id = Gg.id)     WHERE GG.NOME IS NOT NULL and r.id = 620 order by r.data_compra")
            row = dictfetchall(c)
        finally:
            c.close()
        newest = row #OrderCompraVenda.objects.raw("SELECT R.id, R.corretora_id_id, R.ordem_id_id ,R.STATUS, gg.nome FROM Blog_ordercompravenda R LEFT JOIN BLOG_ORDERENVIO O ON (R.ordem_id_id = O.ID) LEFT JOIN BLOG_REQUICAOEST E ON (R.ordem_id_id = E.ordem_id_id) LEFT JOIN BLOG_ESTRATEGIAS Gg ON (E.estr_id_id = Gg.id)     WHERE GG.NOME IS NOT NULL  order by r.data_compra" ).order_by('corretora_id_id').last()
        CustonResponse001.columns['id','corretora_id', 'ordem_id', 'status','corretora']
        #newest = self.get_queryset().order_by('corretora_id_id').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)