from django.db import models

class ejemplo(models.Model):
    # Tus otros campos de la clase ejemplo...
    edad = models.IntegerField()

class empleado(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()

    # NUEVO MODELO PARA SOLID STATE GAMES

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

 # Mensajes de usuarios
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre