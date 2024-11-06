from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'price', 'is_available', 'category', 'image']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }