document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('productoForm');
    const modal = document.getElementById('crud-modal');
    const modalToggle = document.querySelector('[data-modal-toggle="crud-modal"]');
    const closeButton = document.querySelector('[data-modal-toggle="crud-modal"] svg').parentElement;

    // Función para cerrar el modal
    function closeModal() {
        modal.classList.add('hidden');
    }

    // Event listeners para el modal
    modalToggle.addEventListener('click', () => {
        modal.classList.remove('hidden');
    });

    closeButton.addEventListener('click', closeModal);

    // Manejar el envío del formulario
    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        const formData = new FormData();
        formData.append('nombre', document.getElementById('name').value);
        formData.append('descripcion', document.getElementById('description').value);
        formData.append('precio', document.getElementById('price').value);
        formData.append('stock', document.getElementById('stock').value);
        formData.append('categoria', document.getElementById('category').value);
        
        const proveedorSelect = document.getElementById('proveedor');
        if (proveedorSelect.value) {
            formData.append('proveedor', proveedorSelect.value);
        }
        
        const imagenInput = document.getElementById('file_input');
        if (imagenInput.files.length > 0) {
            formData.append('imagen', imagenInput.files[0]);
        }

        try {
            const response = await fetch('/administration/crear-producto/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });

            const data = await response.json();

            if (data.status === 'success') {
                showNotification('Producto creado exitosamente', 'success');
                setTimeout(function() {
                    closeModal();
                    form.reset();
                    window.location.reload();
                }, 1500);
            } else {
                showNotification(data.message || 'Error al crear el producto', 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            showNotification('Error al crear el producto', 'error');
        }
    });

    // Función para cambiar estado del producto
    window.cambiarEstadoProducto = async function(productoId) {
        try {
            const result = await Swal.fire({
                title: '¿Estás seguro?',
                text: "¿Deseas cambiar el estado de este producto?",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sí, cambiar estado',
                cancelButtonText: 'Cancelar'
            });

            if (result.isConfirmed) {
                const response = await fetch(`/administration/producto/${productoId}/cambiar-estado/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                });

                const data = await response.json();

                if (data.status === 'success') {
                    showNotification('Estado del producto actualizado exitosamente', 'success');
                    setTimeout(() => window.location.reload(), 1500);
                } else {
                    showNotification(data.message, 'error');
                }
            }
        } catch (error) {
            console.error('Error:', error);
            showNotification('Error al cambiar el estado del producto', 'error');
        }
    };
});

// Función para obtener el token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Función para mostrar notificaciones
function showNotification(message, type) {
    const notification = document.createElement('div');
    notification.className = `fixed top-4 right-4 p-4 rounded-lg ${
        type === 'success' ? 'bg-green-500' : 'bg-red-500'
    } text-white z-50`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}
