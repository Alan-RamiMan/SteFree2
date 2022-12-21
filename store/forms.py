from django import forms
from .models import Contacto


# Este formulario se debe immportar en las Views y luego enviar al template 
class ContactoForms (forms.ModelForm):
    class Meta:
        model=Contacto
        # fields=["nombre","email","tipo_cosulta","mensaje","avisos"]
        fields='__all__'
        
        