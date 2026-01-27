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
    return render(request, 'relationship
