from django.urls import path

from proyecto import views

app_name = "proyecto"

urlpatterns = [
 path('list/',views.List.as_view(), name="list"),
]
