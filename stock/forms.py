from django import forms
from django.forms import formset_factory
from django.db import models
from django.db.models import fields
from .models import Stock,Supplier,Category,Purches,Sale,Customer

class Add_stock_form (forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category','item_name', 'quantity','price','amount', 'supplier']

    

class Add_Sup_form (forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['sup_name','sup_mobile','sup_email','sup_note']

class Add_Category_form (forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']

class PurchesForm(forms.ModelForm):

    def __init__ (self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['stock'].queryset = Stock.objects.filter(is_deleted= False)

    class Meta:
        model = Purches
        fields=['supplier','stock', 'pur_quantity']

Purchase_stock_formset= formset_factory(PurchesForm, extra=1)



class Add_Cust_form (forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class SaleForm(forms.ModelForm):

    def __init__ (self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['stock'].queryset = Stock.objects.filter(is_deleted= False)

    class Meta:
        model = Sale
        fields=['customer','stock', 'sale_quantity']

# Purchase_stock_formset= formset_factory(PurchesForm, extra=1)


        