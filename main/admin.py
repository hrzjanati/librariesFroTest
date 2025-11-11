from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Library, RequiredItem

# admin.py
from django import forms
from django.contrib import admin
from django.contrib import admin
from .models import Library, RequiredItem, Book

class RequiredItemInline(admin.TabularInline):
    model = RequiredItem
    extra = 1
    autocomplete_fields = ['book']  # این باعث میشه وقتی تایپ کنی کتاب‌ها پیشنهاد داده بشه

class LibraryAdmin(admin.ModelAdmin):
    inlines = [RequiredItemInline]
    list_display = ('name', 'province', 'city', 'street_detail', 'date_of_create')
    search_fields = ('name', 'street_detail')
    list_filter = ('province', 'city')
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Library, LibraryAdmin)