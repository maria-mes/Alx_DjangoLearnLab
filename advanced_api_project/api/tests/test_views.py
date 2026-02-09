from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from api.models import Author, Book

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="tester", password="pass123")
        self.author = Author.objects.create(name="Alice")
        self.book = Book.objects.create(
            title="Test Book", publication_year=2020, author=self.author
        )

    def test_list_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Book', str(response.data))

    def test_create_book_requires_auth(self):
        response = self.client.post('/books/create/', {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, 403)  # unauthenticated

        self.client.login(username="tester", password="pass123")
        response = self.client.post('/books/create/', {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, 201)

    def test_filter_books(self):
        response = self.client.get('/books/?search=Test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Book', str(response.data))
