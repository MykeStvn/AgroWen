# forms.py
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'proveedor','imagen']
        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'})
        }


