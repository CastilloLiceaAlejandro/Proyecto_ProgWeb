from django.urls import path
from Proyecto import views

app_name = "Proyecto"

urlpatterns = [
    path('list/', views.Lista_Producto.as_view(), name="list"),
    path('detail/<int:pk>/', views.Detail_Producto.as_view(), name = "detail"),
    path('newproducto/', views.New_Producto.as_view(), name = "newproducto"),
    path('update/<int:pk>/', views.Update_Producto.as_view(), name = "update"),
    path('delete/<int:pk>/', views.Delete_Producto.as_view(), name = "delete"),
]
