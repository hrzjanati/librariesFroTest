from django.contrib import admin

# Register your models here.
# admin.py

from django import forms
from django.contrib import admin
from .models import Library, RequiredItem, Book

# فرم سفارشی برای Library
class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = "__all__"
        widgets = {
            # فقط سال رو انتخاب می‌کنه (ماه و روز پیش‌فرض می‌شن)
            'date_of_year': forms.SelectDateWidget(years=range(1900, 2030))
        }

# Inline برای RequiredItem
class RequiredItemInline(admin.TabularInline):
    model = RequiredItem
    extra = 1
    autocomplete_fields = ['book']

# Admin سفارشی برای Library
class LibraryAdmin(admin.ModelAdmin):
    form = LibraryForm  # فرم سفارشی رو استفاده می‌کنه
    inlines = [RequiredItemInline]
    list_display = ('name', 'province', 'city', 'street_detail', 'date_of_year')
    search_fields = ('name', 'street_detail')
    list_filter = ('province', 'city')

# Admin برای Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['name']

# ثبت Library در ادمین
admin.site.register(Library, LibraryAdmin)