# administration/urls.py
from django.urls import path
from . import views
app_name = 'administration'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('productos/', views.productos, name='productos'),
    path('usuarios/', views.usuarios, name='usuarios'),    
    path('crear-producto/', views.crear_producto, name='crear_producto'),
    path('producto/<int:producto_id>/', views.ver_producto, name='ver_producto'),
    path('producto/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('producto/<int:producto_id>/cambiar-estado/', views.cambiar_estado_producto, name='cambiar_estado_producto'),
]