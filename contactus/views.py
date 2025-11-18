from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage
import requests

BOT_TOKEN = "8178056523:AAG1roNPcFSacGrNhtpMXpiu90xAQhnXxhs"
CHAT_ID = "82041680"

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # ذخیره در دیتابیس
        ContactMessage.objects.create(
            name=name,
            phone=phone,
            email=email,
            subject=subject,
            message=message
        )

        # ارسال همزمان به تلگرام
        text = f"📩 پیام جدید از فرم ارتباط با ما:\n\nنام: {name}\nشماره: {phone}\nایمیل: {email}\nموضوع: {subject}\nپیام: {message}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text})

        # HTML برای toast + پاک کردن فرم
        return HttpResponse("""
            <div class="fixed top-4 right-4 bg-green-500 text-white px-4 py-2 rounded shadow-md">
                پیام شما با موفقیت ارسال شد!
            </div>
            <script>
                const form = document.currentScript.closest('form');
                form.reset();
            </script>
        """)

    return render(request, "contactus/contactus.html")