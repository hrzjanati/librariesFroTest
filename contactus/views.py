from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import ContactMessage

@csrf_exempt
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

        # HTML برای toast + پاک کردن فرم و محو شدن بعد ۵ ثانیه
        return HttpResponse("""
            <div id="toast" class="fixed top-4 right-4 bg-green-500 text-white px-4 py-2 rounded shadow-md">
                پیام شما با موفقیت ارسال شد!
            </div>
            <script>
                const form = document.currentScript.closest('form');
                form.reset();  // پاک کردن فیلدها
                setTimeout(() => {
                    const toast = document.getElementById('toast');
                    if(toast) toast.remove();  // محو کردن toast بعد از ۵ ثانیه
                }, 5000);
            </script>
        """)

    return render(request, "contactus.html")