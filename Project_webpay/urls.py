from typing import ValuesView
from django.contrib import admin
from django.urls import path
from Project_webpay import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #PAGINA PRINCIPAL
    path('', views.index),

    path('producto1/', views.producto1),  
    #DIRECCION PARA PAGO
    path('webpay-plus-create',views.webpay_plus_create),
    #RESUMEN DE LA COMPRA
    path('commit-pay/',views.commitpay),

]
