
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from ..models import Library, Province

def home(request):
    query = request.GET.get('q', '').strip()

    # اول سعی کن همه مقادیر provinces رو به‌صورت لیست بگیریم
    provinces_list = request.GET.getlist('provinces')  # -> ['3','7','8']
    # همون‌طور که قبلاً ممکن بود CSV هم بفرستی: ?provinces=3,7,8
    if not provinces_list:
        provinces_csv = request.GET.get('provinces', '')
        provinces_list = provinces_csv.split(',') if provinces_csv else []

    # پاک‌سازی و نگه داشتن فقط اعدادی که عددی هستند
    ids = [int(p) for p in provinces_list if str(p).isdigit()]

    libraries = Library.objects.all()

    # فیلتر جستجو
    if query:
        libraries = libraries.filter(
            Q(name__icontains=query) |
            Q(required_items__book__name__icontains=query)  # اگر فیلد مرتبط با کتاب اینه
        ).distinct()

    # فیلتر استان‌ها (چندتایی)
    if ids:
        libraries = libraries.filter(province_id__in=ids)

    # pagination
    paginator = Paginator(libraries.order_by('id'), 5)
    page_number = request.GET.get('page')
    libraries_page = paginator.get_page(page_number)

    provinces = Province.objects.all()

    context = {
        'libraries': libraries_page,
        'query': query,
        'selected_provinces': [str(i) for i in ids],  # برای template به‌صورت رشته
        'provinces': provinces,
    }

    # اگر AJAX یا HTMX هست، فقط partial برگردون
    if request.htmx:
        return render(request, "library_list.html", context)

    return render(request, 'index.html', context)

# main/apps.py
from django.apps import AppConfig
import threading
class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        from main.bot import start_bot  # فانکشنی که بات رو run می‌کنه

        # فقط یکبار اجرا شود
        thread = threading.Thread(target=start_bot, daemon=True)
        thread.start()