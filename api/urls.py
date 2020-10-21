from django.urls import path

from api import views

app_name = "api"

urlpatterns = [
    path('v1/plataforma_list/', views.PlataformaList.as_view(), name = "plataforma_list"),
    path('v1/plataforma_detail/<int:pk>', views.PlataformaDetail.as_view(), name = "Plataforma_detail"),

    path('v1/desarrollador_list/', views.DesarrolladorList.as_view(), name = "desarrollador_list"),

    path('v1/producto_list/', views.ProductoList.as_view(), name = "producto_list"),
    path('v1/producto_detail/<int:pk>', views.ProductoDetail.as_view(), name = "producto_detail"),

    path('v1/stock_list/', views.StockList.as_view(), name = "stock_list"),
]
