from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'owner', 'date_added')
    search_fields = ('title', 'author')
    list_filter = ('date_added',)