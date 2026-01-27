from django.shortcuts import render
from .models import Author, Book, Library, Librarian

def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'relationship_app/authors.html', {'authors': authors})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/books.html', {'books': books})

def list_libraries(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/libraries.html', {'libraries': libraries})

def list_librarians(request):
    librarians = Librarian.objects.all()
    return render(request, 'relationship_app/librarians.html', {'librarians': librarians})
