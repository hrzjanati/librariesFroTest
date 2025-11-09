from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Library, RequiredItem

class RequiredItemInline(admin.TabularInline):
    model = RequiredItem
    extra = 1

class LibraryAdmin(admin.ModelAdmin):
    inlines = [RequiredItemInline]
    list_display = ('name', 'location', 'date_of_create')
    search_fields = ('name', 'location')

admin.site.register(Library, LibraryAdmin)
