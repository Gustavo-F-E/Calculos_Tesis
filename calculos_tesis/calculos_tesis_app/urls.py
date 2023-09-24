from django.urls import path 
from . import views 

 

urlpatterns = [ 

    path('', views.index, name='index'), 
    path('regla_mezclas_teoria/', views.regla_mezclas_teoria, name='regla_mezclas_teoria'), 
    path('regla_mezclas_calculos/', views.regla_mezclas_calculos, name='regla_mezclas_calculos'), 
    path('modelo_microestructura_periodica_teoria/', views.modelo_microestructura_periodica_teoria, name='modelo_microestructura_periodica_teoria'), 
    path('modelo_microestructura_periodica_calculos/', views.modelo_microestructura_periodica_calculos, name='modelo_microestructura_periodica_calculos'), 

] 