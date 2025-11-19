from django import forms
from .models import ContactMessage
import re

def persian_to_english_number(input_str):
    persian_nums = "۰۱۲۳۴۵۶۷۸۹"
    english_nums = "0123456789"
    translation_table = str.maketrans(persian_nums, english_nums)
    return input_str.translate(translation_table)

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "email", "subject", "message"]

    phone_regex = re.compile(r'^09\d{9}$')  # دقیقا 11 رقم

    phone = forms.CharField(
        max_length=11,  # این باعث می‌شود بیشتر از 11 رقم وارد نشود
        widget=forms.TextInput(attrs={
            "placeholder": "شماره همراه",
            "maxlength": "11"  # محدودیت در HTML
        })
    )

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "")
        phone = persian_to_english_number(phone)  # تبدیل اعداد فارسی به انگلیسی

        if not self.phone_regex.match(phone):
            raise forms.ValidationError("شماره همراه معتبر نیست. باید با 09 شروع شود و دقیقاً 11 رقم باشد.")
        return phone