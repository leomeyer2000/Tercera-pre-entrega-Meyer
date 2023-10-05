from django import forms

class EscribanoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    
class DocumentoFormulario(forms.Form):
    registro = forms.CharField(max_length=40)
    codigo = forms.IntegerField()
    pin = forms.IntegerField()
    fecha = forms.DateField()
    
class ObservacionFormulario(forms.Form):
    documento = forms.IntegerField()
    tipo = forms.CharField(max_length=40)

class buscarEscribanoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    
class buscarDocumentoForm(forms.Form):
    codigo = forms.IntegerField()
    
class buscarObservacionForm(forms.Form):
    documento = forms.IntegerField()