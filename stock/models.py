from datetime import timezone
from django.db import models



# Create your models here.

class Category (models.Model):
    cat_name= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.cat_name


class Supplier (models.Model):
    sup_name = models.CharField(max_length=200, null=True,)
    sup_mobile = models.CharField(max_length=200, null=True, blank=True)
    sup_email = models.CharField(max_length=200, null=True, blank=True)
    sup_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.sup_name

class Stock( models.Model):
    id = models.AutoField(primary_key=True)
    category =models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True)
    item_name = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(null=True, blank=True,default= 0)
    amount = models.FloatField(null=True, blank=True,default= 0)
    supplier= models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True,blank=True)
    last_updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    timestamp= models.DateTimeField(auto_now_add=True,auto_now=False,)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        itemname=str(self.item_name)
        return itemname


class Purches (models.Model):
    id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey (Supplier,on_delete=models.CASCADE)
    stock = stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, related_name='purchasestock')
    pur_quantity = models.IntegerField( default=0)



class Customer (models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Sale (models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stock = stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, related_name='salestock')
    sale_quantity = models.IntegerField()
    
    def __str__(self) -> str:
            return str(self.customer)




