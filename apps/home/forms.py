from django import forms
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Prueba

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Nombre', required=True, max_length=20, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nombre',
            'id': 'exampleFormControlInput1'            
        }
    ))
    email=forms.CharField(label='Email', required=True, max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'nombre@ejemplo.com',
            'id': 'exampleFormControlInput1',
            'pattern': "^[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{2,5}$"           
        }
    ))
    curp=forms.CharField(label='Curp', required=True, max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'CURP',
            'id': 'exampleFormControlInput1',
            'pattern': "^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$"          
        }
    ))
    contenido=forms.CharField(label='Contenido', required=False, max_length=400, widget=forms.Textarea(
        attrs={
            'placeholder': 'Escribe tu mensaje...',
            'rows': '3'
        }
    ))
    img = forms.ImageField(required=False)

class FormularioPrueba(forms.Form):
    img = forms.ImageField()
    nombre = forms.CharField()
        