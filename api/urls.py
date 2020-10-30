from django.urls import path

from api import views

app_name = "api"

urlpatterns = [
    path('v1/plataforma_list/', views.PlataformaList.as_view(), name = "plataforma_list"),
    path('v1/plataforma_detail/<int:pk>', views.PlataformaDetail.as_view(), name = "Plataforma_detail"),
    path('v2/plataforma_new/', views.PlataformaNew.as_view(), name = "Plataforma_new"),

    path('v1/desarrollador_list/', views.DesarrolladorList.as_view(), name = "desarrollador_list"),
    path('v2/desarrollador_new/', views.DesarrolladorNew.as_view(), name = "Desarrollador_new"),

    path('v1/producto_list/', views.ProductoList.as_view(), name = "producto_list"),
    path('v1/producto_detail/<int:pk>', views.ProductoDetail.as_view(), name = "producto_detail"),
    path('v2/producto_new/', views.ProductoNew.as_view(), name = "Producto_new"),

    path('v1/stock_list/', views.StockList.as_view(), name = "stock_list"),
    path('v2/stock_new/', views.StockNew.as_view(), name = "Stock_new"),
]
