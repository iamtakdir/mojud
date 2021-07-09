from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics , mixins
from rest_framework import viewsets
from .serializers import *
from stock.models import *

# Swaggers 

from rest_framework.permissions import AllowAny
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger import renderers


# Swaggers view class

class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema)


#  using API VIEW

class Item_list_ApiView(APIView):

    def get (self, request, format=None):

        qs = Stock.objects.all()
        serializer = Stock_Serializer(qs, many = True)
        return Response (serializer.data)



#  Using Genarics Api classes with mixins 

class Add_Stock_ApiView(mixins.CreateModelMixin,generics.ListAPIView):

    queryset = Stock.objects.all()
    serializer_class = Stock_Serializer

    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)


#  Using Readymade generics api views to Update Delete Retrive 


class Stock_Details_ApiView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Stock.objects.all()
    serializer_class = Stock_Serializer
    lookup_field = 'pk'



# using Viewsets Supplier


class SupplierViewset(viewsets.ModelViewSet):

    queryset = Supplier.objects.all()
    serializer_class= Supplier_Serializer

class CategoryViewset(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = Category_Serializer



class Purchase_ApiView(viewsets.ModelViewSet):

    queryset = Purches.objects.all()
    serializer_class = Purchase_Serializer

    def perform_create(self, serializer):

        data = serializer.validated_data

        print('--------data---------', data['pur_quantity'])


        
        pur_item = data['pur_quantity']
        stock_item = data['stock']

        print ("=======data", pur_item, stock_item)

        stock = generics.get_object_or_404(Stock, item_name = stock_item)

        stock.quantity += pur_item

        print(stock.quantity)

        

        stock.save()
        serializer.save()


# todos : sales

class CustomerViewset(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class= Customer_Serializer


class Sale_ApiView(viewsets.ModelViewSet):

    queryset = Sale.objects.all()
    serializer_class = Sales_Serializer

    def perform_create(self, serializer):

        data = serializer.validated_data

        print('--------data---------', data['sale_quantity'])


        
        sale_item = data['sale_quantity']
        stock_item = data['stock']

        print ("=======data", sale_item, stock_item)

        stock = generics.get_object_or_404(Stock, item_name = stock_item)

        stock.quantity -= sale_item

        print(stock.quantity)

        

        stock.save()
        serializer.save()