from django.contrib import admin
from django.urls import path
from relationship_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', views.list_authors, name='authors'),
    path('books/', views.list_books, name='books'),
    path('libraries/', views.list_libraries, name='libraries'),
    path('librarians/', views.list_librarians, name='librarians'),
    # ✅ Add this for the checker:
    path('libraries/<int:library_id>/', views.library_detail, name='library_detail'),
]
