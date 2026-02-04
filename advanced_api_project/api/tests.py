from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", publication_year=2020, author=self.author)
        self.user = User.objects.create_user(username="testuser", password="password")

    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post("/api/books/create/", {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, 201)
