
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from ..models import Library, Province

def home(request):
    query = request.GET.get('q', '').strip()
    province_ids = request.GET.get('provinces', '')  # رشته CSV از checkbox

    libraries = Library.objects.all()

    # فیلتر جستجو
    if query:
        libraries = libraries.filter(
            Q(name__icontains=query) |
            Q(required_items__name__icontains=query)
        ).distinct()

    # فیلتر استان‌ها
    if province_ids:
        ids_list = [int(p) for p in province_ids.split(',') if p.isdigit()]
        libraries = libraries.filter(province_id__in=ids_list)

    # pagination
    paginator = Paginator(libraries.order_by('id'), 5)
    page_number = request.GET.get('page')
    libraries_page = paginator.get_page(page_number)

    # گرفتن همه استان‌ها
    provinces = Province.objects.all()

    context = {
        'libraries': libraries_page,
        'query': query,
        'selected_provinces': province_ids.split(',') if province_ids else [],
        'provinces': provinces,
    }

    # اگر AJAX بود، فقط لیست کتابخانه‌ها رو رندر کن
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'library/_libraries_list.html', context)

    # در غیر این صورت کل صفحه
    return render(request, 'index.html', context)