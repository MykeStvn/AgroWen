from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Producto, Categoria, UserProfile, Proveedor
from .forms import ProductoForm
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@login_required
def dashboard(request):
    messages.success(request, '¡Bienvenido al Panel de Administración!')
    context = {
        'users': User.objects.all()
    }
    return render(request, 'dashboard.html', context)

@login_required
def productos(request):
    context = {
        'productos': Producto.objects.all(),
        'categorias': Categoria.objects.all(),
        'proveedores': Proveedor.objects.all()
    }
    return render(request, 'productos.html', context)

@login_required
def usuarios(request):
    context = {
        'usuarios': User.objects.all(),        
        'perfiles': UserProfile.objects.all(),
    }
    return render(request, 'usuarios.html', context)

@login_required
@csrf_exempt
def crear_producto(request):
    if request.method == 'POST':
        try:
            # Manejar datos del formulario
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            precio = request.POST.get('precio')
            stock = request.POST.get('stock')
            categoria_id = request.POST.get('categoria')
            proveedor_id = request.POST.get('proveedor')
            
            # Validar datos requeridos
            if not all([nombre, descripcion, precio, stock, categoria_id]):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Todos los campos son requeridos'
                }, status=400)
            
            # Obtener objetos relacionados
            categoria = Categoria.objects.get(id=categoria_id)
            proveedor = Proveedor.objects.get(id=proveedor_id) if proveedor_id else None
            
            # Crear el producto
            producto = Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                stock=stock,
                categoria=categoria,
                proveedor=proveedor
            )
            
            # Manejar la imagen si existe
            if 'imagen' in request.FILES:
                producto.imagen = request.FILES['imagen']
                producto.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Producto creado exitosamente',
                'producto': {
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio': str(producto.precio),
                    'categoria': producto.categoria.nombre,
                    'proveedor': producto.proveedor.nombre if producto.proveedor else None,
                    'imagen_url': producto.imagen.url if producto.imagen else None
                }
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

@login_required
@csrf_exempt
def ver_producto(request, producto_id):
    try:
        producto = get_object_or_404(Producto, id=producto_id)
        return JsonResponse({
            'status': 'success',
            'producto': {
                'id': producto.id,
                'nombre': producto.nombre,
                'descripcion': producto.descripcion,
                'precio': str(producto.precio),
                'stock': producto.stock,
                'categoria': producto.categoria.nombre,
                'proveedor': producto.proveedor.nombre if producto.proveedor else 'No asignado',
                'imagen_url': producto.imagen.url if producto.imagen else None,
                'estado': producto.estado,
                'fecha_creacion': producto.fecha_creacion.strftime('%d/%m/%Y %H:%M'),
                'fecha_actualizacion': producto.fecha_actualizacion.strftime('%d/%m/%Y %H:%M')
            }
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@login_required
@csrf_exempt
def editar_producto(request, producto_id):
    if request.method == 'POST':
        try:
            producto = get_object_or_404(Producto, id=producto_id)
            
            # Actualizar campos
            producto.nombre = request.POST.get('nombre', producto.nombre)
            producto.descripcion = request.POST.get('descripcion', producto.descripcion)
            producto.precio = request.POST.get('precio', producto.precio)
            producto.stock = request.POST.get('stock', producto.stock)
            
            # Actualizar relaciones
            categoria_id = request.POST.get('categoria')
            if categoria_id:
                producto.categoria = Categoria.objects.get(id=categoria_id)
            
            proveedor_id = request.POST.get('proveedor')
            if proveedor_id:
                producto.proveedor = Proveedor.objects.get(id=proveedor_id)
            
            # Actualizar imagen si se proporciona una nueva
            if 'imagen' in request.FILES:
                producto.imagen = request.FILES['imagen']
            
            producto.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Producto actualizado exitosamente',
                'producto': {
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio': str(producto.precio),
                    'categoria': producto.categoria.nombre,
                    'proveedor': producto.proveedor.nombre if producto.proveedor else None,
                    'imagen_url': producto.imagen.url if producto.imagen else None
                }
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

@login_required
@csrf_exempt
def cambiar_estado_producto(request, producto_id):
    if request.method == 'POST':
        try:
            producto = get_object_or_404(Producto, id=producto_id)
            producto.estado = not producto.estado
            producto.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Estado del producto actualizado exitosamente',
                'estado': producto.estado
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)



