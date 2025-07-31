from django.contrib import admin
from .models import MyLibrary






@admin.register(MyLibrary)
class MylibraryAdmin(admin.ModelAdmin):
    list_display = ('avtor','composition', 'year')
    search_fields = ('avtor','composition', 'year')
    list_filter = ('avtor','composition', 'year')