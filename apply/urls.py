from django.urls import path, include
from . import views
from apply import views



urlpatterns = [
    path("apply/",views.apply, name = "apply"),
    path("miPagina/", views.pagina, name="miWeb"),
    path("index/", views.index, name = "miWeb"),
    path('', views.inicio, name='inicio'),
    path('marcas/', views.marcas, name='marcas'),
    path('juegos/', views.Juegos, name='Juegos'),
    path('collecciones/', views.collecciones, name='collecciones'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login, name='login'),
    path("cerrar-sesion/", views.cerrar_sesion, name="cerrar_sesion"),


     path("login/", views.login, name="login"),

    

   
    path("registro/", views.registro, name="registro"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("usuarios/agregar/", views.agregar_usuario, name="agregar_usuario"),
    path(
        "usuarios/editar/<int:id>/",
        views.editar_usuario,
        name="editar_usuario"
    ),
    path(
        "usuarios/eliminar/<int:id>/",
        views.eliminar_usuario,
        name="eliminar_usuario"
    ),
    path("logout/", views.cerrar_sesion, name="logout"),

    path(
    "cerrar-sesion/",
    views.cerrar_sesion,
    name="cerrar_sesion"



    
),

path('agregar-carrito/', views.agregar_carrito, name='agregar_carrito'),

path('carrito/', views.carrito, name='carrito'),

path('eliminar-carrito/<str:producto_id>/', views.eliminar_carrito, name='eliminar_carrito'),

path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),

]

