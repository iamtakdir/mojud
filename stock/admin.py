from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Category)

admin.site.register(Stock)
admin.site.register(Purches)
admin.site.register(Customer)
admin.site.register(Sale)