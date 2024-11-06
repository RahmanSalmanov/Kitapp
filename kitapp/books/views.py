from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import *
from django.shortcuts import render, redirect
from .forms import BookForm
# Home view, kök URL'yi sepet sayfasına yönlendiriyor
def home(request):
    return redirect('cart')  # Kullanıcıyı 'cart' sayfasına yönlendirir

# Ana sayfa
def index(request):
    return render(request, "book/index.html")  # Index sayfasını render eder

# Kitaplar listesi
def books(request):
    books = Book.objects.all()  # Bütün kitabları alır
    categories = Category.objects.all()  # Bütün kateqoriyaları alır
    return render(request, "book/books.html", {'books': books, 'categories': categories})

# Kitap detayları
def book_details(request, id):
    return render(request, "book/book-details.html", {
        "id": id
    })  # Kitap detaylarını render eder

# Sepet görüntüleme view
def view_cart(request):
    """Sepeti görüntülemek için kullanılacak view."""
    cart = request.session.get('cart', [])  # Sepeti oturumda alıyoruz
    books_in_cart = Book.objects.filter(id__in=cart)  # Sepetteki kitapları veritabanından alıyoruz
    
    # Toplam fiyatı hesapla
    total_price = sum(book.price for book in books_in_cart)
    
    return render(request, 'cart.html', {'books': books_in_cart, 'total_price': total_price})

# Kitap ekleme view (sepete)
def add_to_cart(request, book_id):
    """Sepete kitap eklemek için kullanılacak view."""
    cart = request.session.get('cart', [])
    cart.append(book_id)
    request.session['cart'] = cart  # Sepeti session'a kaydet
    return redirect('cart')  # Sepete yönlendir

# Kitap çıkarma view (sepetten)
def remove_from_cart(request, book_id):
    """Sepetten kitap çıkarmak için kullanılacak view."""
    cart = request.session.get('cart', [])
    if book_id in cart:
        cart.remove(book_id)
        request.session['cart'] = cart  # Güncellenmiş sepeti session'a kaydet
    return redirect('cart')  # Sepet sayfasına yönlendir

# Kullanıcı kayıt view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Kullanıcıyı giriş yaptır
            return redirect('home')  # Ana sayfaya yönlendir
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books')  # Kitab siyahısı səhifəsinə yönləndirir
    else:
        form = BookForm()
    return render(request, 'book/add_book.html', {'form': form})
