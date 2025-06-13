from django.contrib import admin
from .models import Categoria, Producto, Proveedor, UserProfile
    
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(UserProfile)


