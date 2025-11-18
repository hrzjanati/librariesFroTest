
from django.urls import path
from .views import faq_page

urlpatterns = [
    path('', faq_page, name='faq'),
]