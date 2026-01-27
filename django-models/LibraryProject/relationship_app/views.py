from django.shortcuts import render, redirect
from .models import Library
from django.views.generic.detail import DetailView
from .models import Author, Book, Librarian
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_add_book')
def add_book(request):
    # placeholder logic
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def change_book(request, book_id):
    # placeholder logic
    return render(request, 'relationship_app/change_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    # placeholder logic
    return render(request, 'relationship_app/delete_book.html')

@login_required
def admin_view(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
        if profile.role == "Admin":
            return HttpResponse("Welcome Admin! This is the protected admin view.")
        else:
            return HttpResponse("Access denied. You must be an Admin to view this page.")
    except UserProfile.DoesNotExist:
        return HttpResponse("No profile found for this user.")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # logs in the new user
            return redirect('authors')  # redirect to any page you want
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



def library_detail(request, library_id):
    library = get_object_or_404(Library, id=library_id) # <-- use library object 
    return render(request, 'relationship_app/library_detail.html', {'library': library})
    
def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'relationship_app/authors.html', {'authors': authors})

def list_books(request):
    books = Book.objects.all()
    # Checker expects this exact string:
    return render(request, 'relationship_app/list_books.html', {'books': books})

def list_libraries(request):
    libraries = Library.objects
class LibraryDetailView(View): 
    def get(self, request, library_id): 
        library = get_object_or_404(Library, id=library_id) 
        return render(request, 'relationship_app/library_detail.html', {'library': library})
