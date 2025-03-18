
from django.shortcuts import render, redirect
from .models import Post
from .forms import AutorForm, PostForm, ComentarioForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'blog/agregar_autor.html', {'form': form})

def buscar_post(request):
    query = request.GET.get('q')
    resultados = Post.objects.filter(titulo__icontains=query) if query else None
    return render(request, 'blog/buscar.html', {'resultados': resultados, 'query': query})
