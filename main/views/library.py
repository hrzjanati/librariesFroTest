from django.shortcuts import render, get_object_or_404
from main.models import Library , Province

def library_detail(request, id):
    library = get_object_or_404(Library, id=id)
    return render(request, 'library_detail.html', {'library': library})


def library_list(request, province_id=None):
    provinces = Province.objects.all()
    province_ids = request.GET.get('provinces', '')

    libraries = Library.objects.all()
    if province_ids:
        ids_list = [int(i) for i in province_ids.split(',') if i.isdigit()]
        libraries = libraries.filter(province_id__in=ids_list)
    elif province_id:
        libraries = libraries.filter(province_id=province_id)

    context = {
        'provinces': provinces,
        'libraries': libraries,
        'selected_provinces': province_ids.split(',') if province_ids else [],
    }

    # اگر AJAX هست فقط partial HTML کتابخانه‌ها برگرده
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'library/_libraries_list.html', {'libraries': libraries})

    return render(request, 'library/library_list.html', context)