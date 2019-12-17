from django import forms
from .models import Autor

class Autor(forms.ModelForm):
    class Nome:
        model = nome_autor
        fields = 'nome'