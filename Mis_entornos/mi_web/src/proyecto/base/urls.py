from django.urls import path
#from .import views
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, PaginaRegistro
from django.urls import path
from . import views

#urlpatterns = [path('',views.lista_pendientes,name='pendientes')]

urlpatterns = [path('',ListaPendientes.as_view(),name='tareas'),
               path('login/',Logueo.as_view(), name ='login'),
               path('registro/',PaginaRegistro.as_view(), name ='registro'),
               path('logout/', views.LogoutView.as_view(), name='logout'),
               path('tarea/<int:pk>',DetalleTarea.as_view(),name='tarea'),
               path('crear-tarea/',CrearTarea.as_view(),name='crear-tarea'),
               path('editar-tarea/<int:pk>',EditarTarea.as_view(),name='editar-tarea'),
               path('eliminar-tarea/<int:pk>',EliminarTarea.as_view(),name='eliminar-tarea'),]

