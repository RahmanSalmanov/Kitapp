from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Ana sayfa ve kitaplarla ilgili URL'ler
    path("home", views.home, name="home"),  # Ana sayfa (redirect)
    path("index", views.index, name="index"),  # Index sayfası
    path("", views.books, name="books"),  # Kitaplar listesi
    path("books/<int:id>", views.book_details, name="book_details"),  # Kitap detayları

    # Kayıt, giriş ve çıkış URL'leri
    path('register/', views.register, name='register'),  # Kayıt sayfası
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Giriş sayfası
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Çıkış sayfası

    # Sepet işlemleri ile ilgili URL'ler
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),  # Sepete ekleme
    path('cart/', views.view_cart, name='cart'),  # Sepeti görüntüleme
    path('remove_from_cart/<int:book_id>/', views.remove_from_cart, name='remove_from_cart'),  # Sepetten çıkarma
]
