from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Catalog

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

def detail(request, catalog_id):
    movie = get_object_or_404(Catalog, pk=catalog_id)
    return render(request, 'catalog/detail.html', {'movie': movie})
