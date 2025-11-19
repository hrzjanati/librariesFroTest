from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

BOT_TOKEN = "8178056523:AAG1roNPcFSacGrNhtpMXpiu90xAQhnXxhs"
CHAT_IDS = ["82041680", "86437587"]

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        book_name = request.POST.get("book")
        library_name = request.POST.get("library")
        number_of_required  = request.POST.get("number_of_required")

        text = f"📚 کتاب انتخاب شد:\n\nکتاب: {book_name}\nکتابخانه: {library_name}  \n تعداد موردنیاز:{number_of_required}"

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        for chat_id in CHAT_IDS:
            requests.post(url, data={"chat_id": chat_id, "text": text})

        # برگرداندن HTML برای toast
        return HttpResponse(
            f'<div class="bg-green-500 text-white px-4 py-2 rounded shadow-md">ارسال شد به ادمین تلگرام!</div>'
        )
    return JsonResponse({"error": "invalid request"})