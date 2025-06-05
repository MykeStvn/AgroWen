from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def accordion(request):
    return render(request, 'accordion.html')

def carousel(request):
    return render(request, 'carousel.html')

def collapse(request):
    return render(request, 'collapse.html')

def dial(request):
    return render(request, 'dial.html')

def dismiss(request):
    return render(request, 'dismiss.html')

def modal(request):
    return render(request, 'modal.html')

def drawer(request):
    return render(request, 'drawer.html')

def dropdown(request):
    return render(request, 'dropdown.html')

def popover(request):
    return render(request, 'popover.html')

def tooltip(request):
    return render(request, 'tooltip.html')

def tabs(request):
    return render(request, 'tabs.html')

def input_counter(request):
    return render(request, 'input-counter.html')

def datepicker(request):
    return render(request, 'datepicker.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
