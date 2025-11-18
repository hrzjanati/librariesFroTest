from django import template

register = template.Library()


def int_to_farsi(num):
    farsi_digits = "۰۱۲۳۴۵۶۷۸۹"
    return "".join(farsi_digits[int(d)] if d.isdigit() else d for d in str(num))


@register.filter
def rial_to_toman(value):
    try:
        value = int(value)
    except:
        return value

    # تبدیل ریال به تومان
    toman = value // 10

    # خلاصه‌سازی
    if toman >= 1_000_000_000:
        result = f"{toman / 1_000_000_000:.1f} میلیارد"
    elif toman >= 1_000_000:
        result = f"{toman / 1_000_000:.0f} میلیون"
    elif toman >= 1_000:
        result = f"{toman / 1_000:.0f} هزار"
    else:
        result = f"{toman:,}"

    # تبدیل به فارسی
    result_farsi = int_to_farsi(result)

    return f"{result_farsi} تومان"