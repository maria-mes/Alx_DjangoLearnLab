from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.list_authors, name='authors'),
    path('books/', views.list_books, name='books'),
    path('libraries/', views.list_libraries, name='libraries'),
    path('librarians/', views.list_librarians, name='librarians'),
    path('libraries/<int:library_id>/', views.library_detail, name='library_detail'),
]
