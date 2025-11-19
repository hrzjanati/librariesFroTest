from django.shortcuts import render
from .models import ContactMessage
from .forms import ContactUsForm
import requests

BOT_TOKEN = "8178056523:AAG1roNPcFSacGrNhtpMXpiu90xAQhnXxhs"
CHAT_IDS = ["82041680", "86437587"]

def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            # ذخیره در دیتابیس
            ContactMessage.objects.create(
                name=cd['name'],
                phone=cd['phone'],
                email=cd['email'],
                subject=cd['subject'],
                message=cd['message']
            )

            # ارسال به تلگرام
            text = f"📩 پیام جدید:\n\nنام: {cd['name']}\nشماره: {cd['phone']}\nایمیل: {cd['email']}\nموضوع: {cd['subject']}\nپیام: {cd['message']}"
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            for chat_id in CHAT_IDS:
                requests.post(url, data={"chat_id": chat_id, "text": text})

            # پاسخ HTMX → فقط فرم با toast موفقیت
            form = ContactUsForm()  # فرم خالی بعد از موفقیت
            return render(request, "contactus/contactus_form.html", {"form": form, "success_message": "پیام شما با موفقیت ارسال شد!"})

        # اگر فرم invalid است → فقط فرم با ارورها برگردانده شود
        return render(request, "contactus/contactus_form.html", {"form": form})

    # GET → صفحه اصلی
    form = ContactUsForm()
    return render(request, "contactus/contactus.html", {"form": form})