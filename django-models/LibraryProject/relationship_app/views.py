from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic.detail import DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from .models import Library, Author, Book, Librarian, UserProfile


# --- Role check helpers ---
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# --- Permission-protected book views ---
@permission_required('relationship_app.can_add_book')
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def change_book(request, book_id):
    return render(request, 'relationship_app/change_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    return render(request, 'relationship_app/delete_book.html')


# --- Role-based views ---
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# --- Authentication views ---
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('authors')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# --- Library and author/book views ---
def library_detail(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, 'relationship_app/library_detail.html', {'library': library})

def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'relationship_app/authors.html', {'authors': authors})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def list_libraries(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/libraries.html', {'libraries': libraries})


# --- Class-based view for library detail ---
class LibraryDetailView(View):
    def get(self, request, library_id):
        library = get_object_or_404(Library, id=library_id)
        return render(request, 'relationship_app/library_detail.html', {'library': library})
