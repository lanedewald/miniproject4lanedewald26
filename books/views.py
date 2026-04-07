from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Book
from .forms import BookForm

# 1. Home Page
def home(request):
    return render(request, 'books/home.html')

# 2. Book List Page
@login_required
def book_list(request):
    user_books = Book.objects.filter(owner=request.user)
    return render(request, 'books/book_list.html', {'books': user_books})

# 3. Book Detail Page
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    return render(request, 'books/book_detail.html', {'book': book})

# 4. Add Book Page (Utilizing a Form)
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

# 5. Register Page
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})