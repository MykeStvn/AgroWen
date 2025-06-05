from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required # Para proteger otras vistas

def login_view(request):
    if request.user.is_authenticated: # Si el usuario ya está logueado, redirigir
        return redirect('/') # O a la página principal del admin

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Opcional: Verificar si el usuario es staff o superusuario
                # if user.is_staff or user.is_superuser:
                login(request, user)
                messages.success(request, '¡Has iniciado sesión correctamente!')
                # Redirige a donde quieras que vaya el admin después del login
                # Por ejemplo, tu home.html o una página de dashboard específica
                next_url = request.GET.get('next') # Para redirigir si venía de una página protegida
                if next_url:
                    return redirect(next_url)
                return redirect('/') # Cambia '/' por tu página principal deseada
                # else:
                #     # Usuario autenticado pero no es admin/staff
                #     # messages.error(request, "No tienes permisos para acceder.")
                #     pass 
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")                
                pass
    else:
        form = LoginForm()
    # Ya no necesitas pasar 'current_form_type' si solo hay login
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/') # Redirigir a tu página de login personalizada
