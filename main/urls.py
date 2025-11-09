from django.urls import path
from .views import home, library_detail

urlpatterns = [
    path('', home, name='home'),
    path('library/<int:id>/', library_detail, name='library_detail'),
]
