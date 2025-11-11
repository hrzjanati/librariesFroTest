from django.urls import path , include
from .views import home , library_detail
from  main.views.library import  library_list
urlpatterns = [
    path('', home, name='home'),
    path('library/<int:id>/', library_detail, name='library_detail'),
    path('libraries/', library_list, name='library_list'),  # همه کتابخانه‌ها
    path('libraries/province/<int:province_id>/', library_list, name='library_list_by_province'),  # بر اساس استان
    path('chaining/', include('smart_selects.urls')),
]