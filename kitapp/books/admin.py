# admin.py

from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price', 'is_available', 'category', 'is_home')  # 'is_home' burada eklendi

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
