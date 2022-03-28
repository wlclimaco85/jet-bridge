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


class ConfiguracoesFilter(filters.FilterSet):
    class Meta:
        model = Configuracoes
        fields = (
            'corretora_id','created'
        )  

class ParceiroFilter(filters.FilterSet):
    class Meta:
        model = Parceiro
        fields = (
            'cnpj','author','created'
        )  

class RobosFilter(filters.FilterSet):
    class Meta:
        model = Robos
        fields = (
            'descricao','version','nome'
        )       

class OrdensFilter(filters.FilterSet):
    class Meta:
        model = OrderEnvio
        fields = {
            'id': ['lt']
        }

class CorretoraFilter(filters.FilterSet):
    class Meta:
        model = Corretora
        
        fields = (
            'usuario','id'
        )  
#
class OrdemStatusFilter(filters.FilterSet):
    class Meta:
        model = OrdemStatus
        fields = (
            'corretora_id','ordem_id','status'
        )   

class OrdemZeradaFilter(filters.FilterSet):
    class Meta:
        model = OrdemZerada
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
    queryset = OrderEnvio.objects.all()
    serializer_class = OrderEnvioSerializer

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

class RobosViewSet(viewsets.ModelViewSet):
    queryset = Robos.objects.all()
    serializer_class = RobosSerializer
    filterset_class = RobosFilter

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


class ConfiguracoesViewSet(viewsets.ModelViewSet):
    queryset = Configuracoes.objects.all()
    serializer_class = ConfiguracoesSerializer
    filterset_class = ConfiguracoesFilter

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

class OrdemZeradaViewSet(viewsets.ModelViewSet):
    queryset = OrdemZerada.objects.all()
    serializer_class = OrdemZeradaSerializer
    filterset_class = OrdemZeradaFilter
    
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
  #  c = connection.cursor()
 #   try:
      #  c.execute("SELECT R.corretora_id_id as corretora_id, R.ordem_id_id as ordem_id ,R.STATUS as status, gg.nome as corretora FROM Blog_ordercompravenda R LEFT JOIN BLOG_ORDERENVIO O ON (R.ordem_id_id = O.ID) LEFT JOIN BLOG_REQUICAOEST E ON (R.ordem_id_id = E.ordem_id_id) LEFT JOIN BLOG_ESTRATEGIAS Gg ON (E.estr_id_id = Gg.id)     WHERE GG.NOME IS NOT NULL and r.id = 618 order by r.data_compra")
      #  row = dictfetchall(c)
  #  finally:
  #      c.close()
    
   # queryset = row
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
        quert = " SELECT R.CORRETORA_ID_ID as corretora_id, R.ordem_id_id as ordem_id ,R.TIPO,R.STATUS,R.SIMBOLO, R.PRECO_COMPRA,R.PRECO_VENDA, R.DATA_COMPRA, DATA_VENDA,R.CREATED, R.STATUS,R.TICKET,R.TIPO,  R.PRECO_LOSS, R.PRECO_GAIN "
        quert = quert + "	FROM Blog_ordercompravenda R "
        quert = quert + "	LEFT JOIN BLOG_ORDERENVIO O ON (R.ordem_id_id = O.ID) "
        quert = quert + "	WHERE R.CORRETORA_ID_ID IS NOT NULL "
        if(id):
            quert = quert + "and r.id = "+id
        if(latitude):
            quert = quert + "and r.corretora_id_id = "+latitude
        if(radius):
            quert = quert + "and r.STATUS = '"+radius+"'"

        quert = quert + " order by r.ordem_id_id, r.id DESC"
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
        #CustonResponse001.columns['id','corretora_id', 'ordem_id', 'status','corretora']
        #newest = self.get_queryset().order_by('corretora_id_id').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class CustonResponse002ViewSet(viewsets.ModelViewSet):

    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    
    
    from collections import namedtuple
    
    serializer_class = CustonResponse002Serializer
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
        futuredate = datetime.now();
        corretora_id = self.request.query_params.get('corretora_id')
        dataInicio = self.request.query_params.get('dataInicio')
        dataFim = self.request.query_params.get('dataFim')
        status = self.request.query_params.get('status')
        estrategia = self.request.query_params.get('estrategia')
        orderId = self.request.query_params.get('orderId')
        requsicaoId = self.request.query_params.get('requsicaoId')
        from collections import namedtuple
        cc = connection.cursor()
       # try:
        quert = "SELECT O.ID, O.SIMBOLO,O.VALOR,O.DATA,O.TIPO,O.CREATED,O.UPDATED,O.PERIODO FROM BLOG_ORDERENVIO O  "
        quert = quert + "WHERE not exists (select * from blog_ORDEMSTATUS r where r.ordem_id_id = O.ID "
        if(corretora_id):
            quert = quert + "AND R.CORRETORA_ID_ID = "+corretora_id+")"
        else:
            quert = quert + ")"
        quert = quert + " AND O.DATA > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40'";
        quert = quert + " order by O.id DESC"
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
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class CustonResponse003ViewSet(viewsets.ModelViewSet):
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    
    
    from collections import namedtuple

    serializer_class = CustonResponse002Serializer
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
        
        corretora_id = self.request.query_params.get('corretora_id')
        dataInicio = self.request.query_params.get('dataInicio')
        dataFim = self.request.query_params.get('dataFim')
        status = self.request.query_params.get('status')
        estrategia = self.request.query_params.get('estrategia')
        orderId = self.request.query_params.get('orderId')
        requsicaoId = self.request.query_params.get('requsicaoId')
        from collections import namedtuple
        cc = connection.cursor()
       # try:
        quert = "SELECT O.ID, O.SIMBOLO,O.VALOR,O.DATA,O.TIPO,O.CREATED,O.UPDATED,O.PERIODO FROM BLOG_ORDERENVIO O  "
        quert = quert + "WHERE exists (select * from blog_ORDEMSTATUS r where r.ordem_id_id = O.ID "
        if(corretora_id):
            quert = quert + "AND R.CORRETORA_ID_ID = "+corretora_id+")"
        else:
            quert = quert + ")"
        quert = quert + " order by O.id DESC"
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
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class CustonResponse004ViewSet(viewsets.ModelViewSet):
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    
    
    from collections import namedtuple

    serializer_class = CustonResponse004Serializer
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
        
        corretora_id = self.request.query_params.get('corretora_id')
        dataInicio = self.request.query_params.get('dataInicio')
        dataFim = self.request.query_params.get('dataFim')
        status = self.request.query_params.get('status')
        estrategia = self.request.query_params.get('estrategia')
        orderId = self.request.query_params.get('orderId')
        requsicaoId = self.request.query_params.get('requsicaoId')
        from collections import namedtuple
        cc = connection.cursor()
       # try:
        futuredate = datetime.now()
        start_date =  datetime(futuredate.year, futuredate.month, futuredate.day, 0, 32, 11)
        quert = "SELECT O.ID, O.SIMBOLO,O.VALOR,O.DATA,O.TIPO,O.CREATED,O.UPDATED,O.PERIODO FROM BLOG_ORDERENVIO O  "
        quert = quert + "WHERE not exists (select * from blog_ORDEMSTATUS r where r.ordem_id_id = O.ID "
        if(corretora_id):
            quert = quert + "AND R.CORRETORA_ID_ID = "+corretora_id+")"
        else:
            quert = quert + ")"
        quert = quert +  " AND O.data > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' order by O.id DESC"
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
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


class CustonResponse005ViewSet(viewsets.ModelViewSet):
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    
    
    from collections import namedtuple

    serializer_class = CustonResponse005Serializer
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
        
        corretora_id = self.request.query_params.get('corretora_id')
        dataInicio = self.request.query_params.get('dataInicio')
        dataFim = self.request.query_params.get('dataFim')
        status = self.request.query_params.get('status')
        estrategia = self.request.query_params.get('estrategia')
        orderId = self.request.query_params.get('orderId')
        requsicaoId = self.request.query_params.get('requsicaoId')
        from collections import namedtuple
        cc = connection.cursor()
       # try:
        futuredate = datetime.now()
        start_date =  datetime(futuredate.year, futuredate.month, futuredate.day, 0, 32, 11)
        quert = "SELECT C.ID AS ID ,C.USUARIO AS USUARIO, " 
        quert = quert +  "	(SELECT COUNT(O.*) FROM BLOG_ORDERENVIO O  "  
        quert = quert +  "		WHERE NOT EXISTS (SELECT * FROM BLOG_ORDEMSTATUS R WHERE R.ORDEM_ID_ID = O.ID AND R.CORRETORA_ID_ID = C.ID ) " 
        quert = quert +  "		AND O.DATA > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40') as ordem_abertas_hoje, " 
        quert = quert +  "	(SELECT COUNT(O.*) FROM BLOG_ORDERENVIO O  "  
        quert = quert +  "		WHERE NOT EXISTS (SELECT * FROM BLOG_ORDEMSTATUS R WHERE R.ORDEM_ID_ID = O.ID AND R.CORRETORA_ID_ID = C.ID )) as ordem_abertas_total, " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.STATUS = 'A' AND O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as order_state_started , " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.STATUS = 'B' AND O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as order_state_placed , " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.STATUS = 'C' AND O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as order_state_canceled , " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.STATUS = 'D' AND O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as order_state_partial , " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.STATUS = 'E' AND O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as order_state_filled , " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.STATUS = 'F' AND O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as order_state_rejected , " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.STATUS = 'G' AND O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as order_state_expired , " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.STATUS = 'H' AND O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as order_state_request_add , " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.STATUS = 'I' AND O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as order_state_request_modify, " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.STATUS = 'J' AND O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as order_state_request_cancel , " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.STATUS = 'Z' AND O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as ordem_erro,  " 
        quert = quert +  "	(SELECT COUNT(*) FROM BLOG_ORDERCOMPRAVENDA O WHERE O.CORRETORA_ID_ID = C.ID AND O.CREATED > '"+ str(futuredate.year)+"-"+str(futuredate.month)+"-"+str(futuredate.day)+" 00:38:40' ) as ordem_dia   " 
        quert = quert +  "FROM BLOG_CORRETORA C  " 
        quert = quert +  "ORDER BY ID DESC " 
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
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class CustonResponse006ViewSet(viewsets.ModelViewSet):
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    
    
    from collections import namedtuple
    c = connection.cursor()

    serializer_class = CustonResponse006Serializer
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
        requsicaoId = self.request.query_params.get('requsicaoId')
        from collections import namedtuple
        cc = connection.cursor()
       # try:

        quert = " SELECT T.ORDEM_ID_ID, e.NOME,E.DESCRICAO FROM BLOG_ESTRATEGIAS E LEFT JOIN BLOG_REQUICAOEST T ON (E.ID = T.ESTR_ID_ID )"
        if(requsicaoId):
            quert = quert +  " WHERE T.ORDEM_ID_ID = "+requsicaoId+"	"  
        
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
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class CustonResponse007ViewSet(viewsets.ModelViewSet):
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    
    
    from collections import namedtuple

    serializer_class = CustonResponse007Serializer
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

        from collections import namedtuple
        cc = connection.cursor()
       # try:

        corretora_id = self.request.query_params.get('corretora_id')
        from collections import namedtuple
        cc = connection.cursor()
       # try:
        quert = "SELECT O.ID, O.CORRETORA_ID_ID AS CORRETORA_ID, O.TICKET,O.SIMBOLO, O.ORDEM_ID_ID AS QTDCONTRATOS, O.TICKET AS POSITIONID, O.STATUS, O.TIPO,O.ORDEM_ID_ID FROM BLOG_ORDERCOMPRAVENDA O "
        quert = quert + " WHERE O.ORDEM_ID_ID IN (SELECT ORDEM_ID_ID FROM BLOG_ORDEMZERADA Z WHERE Z.STATUS = 'Z') "
        if (corretora_id):
            quert = quert + " AND O.CORRETORA_ID_ID = "+corretora_id+" "
        
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
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class CustonResponse008ViewSet(viewsets.ModelViewSet):
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    
    from collections import namedtuple

    serializer_class = CustonResponse008Serializer
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

        from collections import namedtuple
        cc = connection.cursor()
       # try:

        corretora_id = self.request.query_params.get('corretora_id')
        from collections import namedtuple
        cc = connection.cursor()
       # try:
        quert = 'SELECT id, "urlPrincipal" , "dataConf", "loteWin", "loteWdo", "loteB3", "gainDiario", "lossDiario", "lossWin", "gainWin", "lossWdo", "gainWdo", "seguranca","segurancaWDO","lossB3", "gainB3", created, updated, corretora_id_id, robo_id_id'
        quert = quert + " FROM public.blog_configuracoes "
        if (corretora_id):
            quert = quert + " WHERE ID = (SELECT MAX(ID) AS MAIOR_DATA  FROM public.blog_configuracoes " 
            quert = quert + 'WHERE CORRETORA_ID_ID = ' +  corretora_id
            quert = quert + " ) "
            quert = quert + " AND CORRETORA_ID_ID = " +  corretora_id
        
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
    
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
