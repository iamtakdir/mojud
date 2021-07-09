from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from .import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework.routers import DefaultRouter



schema_view = get_schema_view(
    openapi.Info(
        title="Enventory API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'supplier', views.SupplierViewset, basename='supplier'),
router.register(r'category', views.CategoryViewset, basename='category'),
router.register(r'purchase', views.Purchase_ApiView, basename='purchase'),
router.register(r'customer', views.CustomerViewset, basename='customer'),
router.register(r'sale', views.Sale_ApiView, basename='sale'),


urlpatterns=[
    # path('',views.SwaggerSchemaView.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('items/', views.Item_list_ApiView.as_view(), name='item-list' ),
    path('stock/', views.Add_Stock_ApiView.as_view(), name='add_stock_api' ),
    path('stock/<str:pk>/', views.Stock_Details_ApiView.as_view(), name='details_stock_api' ),

    # path('purchase/', views.Purchase_ApiView.as_view(), name='purchase_api')

]+router.urls