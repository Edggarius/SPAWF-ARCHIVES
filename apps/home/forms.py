from django import forms

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
    contenido=forms.CharField(label='Contenido', max_length=400, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu mensaje...',
            'id': 'exampleFormControlTextarea1',
            'rows': '3'
        }
    ))