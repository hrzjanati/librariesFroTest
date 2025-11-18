from django.shortcuts import render, get_object_or_404
from main.models import Library

def library_detail(request, id):
    library = get_object_or_404(Library, id=id)
    return render(request, 'library/library_detail.html', {'library': library})
