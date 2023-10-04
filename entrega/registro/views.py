from django.shortcuts import render
from registro.forms import *
from registro.models import *

# Create your views here.

def inicio(request):
    return render(request, 'registro/inicio.html')

def agregarEscribano(request):
    if request.method == "POST":
        
        formulario = EscribanoFormulario(request.POST)
        
        print(formulario)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            
            escribano = Escribano(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
            
            escribano.save()
            
            return render(request, "registro/inicio.html")
    else:
            
        formulario = EscribanoFormulario()
            
            
        
    return render(request, "registro/agregarEscribano.html", {"formulario":formulario})

def agregarDocumento(request):
    if request.method == "POST":
        
        formulario = DocumentoFormulario(request.POST)
        
        print(formulario)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            
            documento = Documento(registro=info["registro"], codigo=info["codigo"], pin=info["pin"], fecha = info["fecha"], observaciones=info["observaciones"])
            
            documento.save()
            
            return render(request, "registro/inicio.html")
    else:
            
        formulario = DocumentoFormulario()
        
    return render(request, "registro/agregarDocumento.html", {"formulario":formulario})

def agregarObservacion(request):
    if request.method == "POST":
        
        formulario = ObservacionFormulario(request.POST)
        
        print(formulario)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            
            observacion = Observacion(documento=info["documento"],tipo=info["tipo"])
            
            observacion.save()
            
            return render(request, "registro/inicio.html")
    else:
            
        formulario = ObservacionFormulario()
        
    return render(request, "registro/agregarObservacion.html", {"formulario":formulario})



def busquedaEscribano(request):
    if request.method == "POST":
        
        formulario = buscarEscribanoForm(request.POST)
        
        print(formulario)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            
            escribanos = Escribano.objects.filter(nombre__icontains=info["nombre"])
            
            return render(request, "registro/listaEscribanos.html", {"escribanos":escribanos})
    else:
            
        formulario = buscarEscribanoForm()
            
    return render(request, "registro/buscar.html", {"formulario":formulario})


def busquedaDocumento(request):
    if request.method == "POST":
        
        formulario = buscarDocumentoForm(request.POST)
        
        print(formulario)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            
            documentos = Documento.objects.filter(codigo=info["codigo"])
            
            return render(request, "registro/listaDocumentos.html", {"documentos":documentos})
    else:
            
        formulario = buscarDocumentoForm()
            
    return render(request, "registro/buscar.html", {"formulario":formulario})

def busquedaObservacion(request):
    if request.method == "POST":
        
        formulario = buscarObservacionForm(request.POST)
        
        print(formulario)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            
            observaciones = Observacion.objects.filter(documento=info["documento"])
            
            return render(request, "registro/listaObservaciones.html", {"observaciones":observaciones})
    else:
            
        formulario = buscarObservacionForm()
            
    return render(request, "registro/buscar.html", {"formulario":formulario})
