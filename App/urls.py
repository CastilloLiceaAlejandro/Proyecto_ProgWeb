from django.urls import path
from Proyecto import views

app_name = "Proyecto"

urlpatterns = [

    ###                                 Producto                                  ###
    path('listproducto/', views.Lista_Producto.as_view(), name="listproducto"),
    path('detailproducto/<int:pk>/', views.Detail_Producto.as_view(), name = "detail"),
    path('newproducto/', views.New_Producto.as_view(), name = "newproducto"),
    path('updateproducto/<int:pk>/', views.Update_Producto.as_view(), name = "update"),
    path('deleteproducto/<int:pk>/', views.Delete_Producto.as_view(), name = "delete"),

    ###                                Plataforma                                 ###
    path('listplataforma/', views.Lista_Plataforma.as_view(), name="listplataforma"),
    path('detailplataforma/<int:pk>/', views.Detail_Plataforma.as_view(), name = "detailplataforma"),
    path('newplataforma/', views.New_Plataforma.as_view(), name = "newplataforma"),
    path('updateplataforma/<int:pk>/', views.Update_Plataforma.as_view(), name = "updateplataforma"),
    path('deleteplataforma/<int:pk>/', views.Delete_Plataforma.as_view(), name = "deleteplataforma"),
    
]
