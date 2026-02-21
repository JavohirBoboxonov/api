from rest_framework import generics
from .models import Book
from .serializer import *

# Ro'yxatni ko'rish va yangi yaratish uchun
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Bitta obyektni ko'rish, o'chirish va tahrirlash uchun
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer