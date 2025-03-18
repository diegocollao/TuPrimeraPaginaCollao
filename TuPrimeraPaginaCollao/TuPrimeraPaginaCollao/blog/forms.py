from django import forms
from .models import Autor, Post, Comentario

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['post', 'nombre', 'texto']
