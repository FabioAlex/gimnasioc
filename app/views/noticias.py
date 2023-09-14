from django.shortcuts import render
from .models import Noticia

def index(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/index.html', {'noticias': noticias})
