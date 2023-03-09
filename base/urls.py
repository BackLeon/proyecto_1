from django.urls import path
from.views import ListaPendientes, DetallleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from .views import Saludo
from . import views

urlpatterns = [path("", ListaPendientes.as_view(), name="tareas"),
               path("saludo/", views.Saludo, name="saludo"),
               path("login/", Logueo.as_view(), name="login"),
               path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
               path("registro/", PaginaRegistro.as_view(), name="registro"),
               path("tarea/<int:pk>", DetallleTarea.as_view(), name="tarea"),
               path("crear-tarea/", CrearTarea.as_view(), name="crear-tarea"),
               path("editar-tarea/<int:pk>", EditarTarea.as_view(), name="editar-tarea"),
               path("eliminar-tarea/<int:pk>", EliminarTarea.as_view(), name="eliminar-tarea")

               ]

