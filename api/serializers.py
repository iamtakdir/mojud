from rest_framework import serializers
from stock.models import *



class Stock_Serializer(serializers.ModelSerializer):

    class Meta:
        model= Stock
        fields = ['category','item_name','quantity','price','supplier','last_updated','timestamp']

        


class Supplier_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Supplier
        fields = '__all__'


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = '__all__'



class Purchase_Serializer(serializers.ModelSerializer):

    def __init__ (self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['stock'].queryset = Stock.objects.filter(is_deleted= False)

    class Meta:
        model = Purches
        fields=['supplier','stock', 'pur_quantity']
    



class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields = '__all__'

        

class Sales_Serializer(serializers.ModelSerializer):

    def __init__ (self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['stock'].queryset = Stock.objects.filter(is_deleted= False)

    class Meta:
        model = Sale
        fields=['customer','stock', 'sale_quantity']