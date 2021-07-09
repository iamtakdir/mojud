from django.urls import path
from .import views


urlpatterns = [
    path('', views.list_items, name='home'),
    # list of items 
    path('items/', views.list_items, name='list_items'),
    path('total_list/', views.total_list, name='total_list'),

    #  Stock Urls 
    path('add_stock/', views.add_stock_form, name='add_stock'),
    path('update_stock/<str:pk>/', views.Update_stock_form, name="update_stock"),
    path('delete_stock/<str:pk>/', views.delete_stock, name="delete_stock"),
    path('stock_details/<str:pk>/', views.stock_details, name="stock_details"),

    # Supplier urls 
    path('add_sup/', views.add_sup_form, name='add_sup'),

    # category urls
    path('add_category/', views.add_catrgory_form, name='add_category'),
    
    # pyrchase urls
    path('purchase/', views.purches, name="purchase"),

    # sales urls
    path('add_cust/', views.add_cust_form, name='add_cust'),
    path('sale/', views.sale, name="sale"),
    path('total_sale/', views.Total_sale.as_view(), name="total_sale"),
    path('sale_details/<str:pk>/', views.Sale_details.as_view(), name="sale_details"),

    path('logout/', views.logoutuser, name="logout"),

   

    
]

