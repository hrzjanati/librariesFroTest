from django.urls import path , include
from .views import home , library_detail, send_message

urlpatterns = [
    path('', home, name='home'),
    path('library/<int:id>/', library_detail, name='library_detail'),
    path('chaining/', include('smart_selects.urls')),
    path("send-message/", send_message, name="send_message"),
]