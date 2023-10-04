from django.urls import path
from registro import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('agregarDocumento', views.agregarDocumento, name="agregarDocumento"),
    path('agregarEscribano', views.agregarEscribano, name="agregarEscribano"),
    path('agregarObservacion', views.agregarObservacion, name="agregarObservacion"),
    path('buscarEscribano', views.busquedaEscribano, name="buscarEscribano"),
    path('buscarDocumento', views.busquedaDocumento, name="buscarDocumento"),
    path('buscarObservacion', views.busquedaObservacion, name="buscarObservacion"),
]