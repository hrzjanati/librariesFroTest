from django.db import models

# Create your models here.
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Library(models.Model):
        name = models.CharField(max_length=255)
        province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
        city = ChainedForeignKey(
            City,
            chained_field="province",
            chained_model_field="province",
            show_all=False,
            auto_choose=True,
            sort=True,
            on_delete=models.SET_NULL,
            null=True
        )
        street_detail = models.CharField(max_length=255)  # خیابان، میدان و جزئیات
        date_of_create = models.DateField()

        def __str__(self):
            return self.name


class Book(models.Model):
    CATEGORY_CHOICES = [
        # ادبیات داستانی
        ('رمان ایرانی و خارجی', 'رمان ایرانی و خارجی'),
        ('داستان کوتاه', 'داستان کوتاه'),
        ('شعر', 'شعر'),
        # ادبیات غیرداستانی
        ('تاریخی', 'تاریخی'),
        ('فلسفی', 'فلسفی'),
        ('روانشناسی', 'روانشناسی'),
        ('خودیاری و توسعه فردی', 'خودیاری و توسعه فردی'),
        ('علمی (علوم پایه، تکنولوژی)', 'علمی (علوم پایه، تکنولوژی)'),
        ('تاریخ ادبیات', 'تاریخ ادبیات'),
        ('تاریخ معاصر', 'تاریخ معاصر'),
        # موضوعات تخصصی
        ('علوم (پزشکی، مهندسی، حقوق و ...)', 'علوم (پزشکی، مهندسی، حقوق و ...)'),
        ('هنر (سینما، موسیقی، نقاشی)', 'هنر (سینما، موسیقی، نقاشی)'),
        # کودک و نوجوان
        ('داستان‌های مصور', 'داستان‌های مصور'),
        ('کتاب‌های آموزشی', 'کتاب‌های آموزشی'),
        ('کتاب‌های علمی تخیلی و فانتزی', 'کتاب‌های علمی تخیلی و فانتزی'),
        # سایر
        ('کتاب‌های مذهبی و دینی', 'کتاب‌های مذهبی و دینی'),
        ('کتاب‌های آشپزی و خانه‌داری', 'کتاب‌های آشپزی و خانه‌داری'),
        ('کتاب‌های سفر و جهانگردی', 'کتاب‌های سفر و جهانگردی'),
        ('کتاب‌های مرجع (دیکشنری، دانشنامه)', 'کتاب‌های مرجع (دیکشنری، دانشنامه)'),
        ('سایر', 'سایر'),
    ]
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class RequiredItem(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='required_items')
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        related_name='required_items',
        null=True,  # یا default=some_book_id
        blank=True
    )
    number_of_required = models.PositiveIntegerField(default=1)
    given_number = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.book)

