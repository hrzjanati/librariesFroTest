from django.shortcuts import render, get_object_or_404
from main.models import Library , Province

def library_detail(request, id):
    library = get_object_or_404(Library, id=id)
    return render(request, 'library_detail.html', {'library': library})


def library_list(request, province_id=None):
    provinces = Province.objects.all()
    if province_id:
        libraries = Library.objects.filter(province_id=province_id)
    else:
        libraries = Library.objects.all()

    context = {
        'provinces': provinces,
        'libraries': libraries,
        'selected_province': province_id,
    }
    return render(request, 'library/library_list.html', context)