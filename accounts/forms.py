from django import forms 
from .models import Account
from .validators import *

class RegistrationForm(forms.ModelForm):
    
    first_name=forms.CharField(min_length=3,required=True)
    last_name=forms.CharField(min_length=3,required=True)
    phone_number=forms.CharField(min_length=8,)
    email=forms.EmailField(min_length=8)
    password=forms.CharField(min_length=8)
    
    password = forms.CharField ( min_length=8,widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese Contraseña',
        'class': 'form-control',
    }))

    confirm_password = forms.CharField( min_length=8,widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar Contraseña',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ingrese Nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ingrese Apellidos'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Ingrese Teléfono'
        self.fields['email'].widget.attrs['placeholder'] = 'Ingrese Email'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "La contraseña no coincide!"
            )

