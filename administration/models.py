from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    estado = models.BooleanField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.nombre} - {self.telefono}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='static/img/productos/', null=True, blank=True)
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.BooleanField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.proveedor:
            return f"{self.nombre} - {self.proveedor.nombre}"
        else:
            return self.nombre

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen_perfil = models.ImageField(upload_to='static/img/usuarios/', null=True, blank=True)
    # Otros campos adicionales que quieras agregar
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"

