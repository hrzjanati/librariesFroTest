from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from ..models import Library

def home(request):
    query = request.GET.get('q', '').strip()  # رشته خالی به جای None
    libraries = Library.objects.all()

    if query:  # فقط اگر query غیر تهی باشد فیلتر کن
        libraries = libraries.filter(
            Q(name__icontains=query) |
            Q(required_items__name__icontains=query)
        ).distinct()

    paginator = Paginator(libraries.order_by('id'), 5)  # مرتب سازی برای جلوگیری از هشدار Pagination
    page_number = request.GET.get('page')
    libraries_page = paginator.get_page(page_number)

    context = {
        'libraries': libraries_page,
        'query': query
    }
    return render(request, 'index.html', context)
