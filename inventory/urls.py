
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stock.urls')),
    path('users/', include('users.urls')),
    path('api/', include('api.urls'), name='api'),

]