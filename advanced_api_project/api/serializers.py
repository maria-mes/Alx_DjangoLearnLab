import datetime
from rest_framework import serializers
from .models import Book, Author

# BookSerializer serializes all fields of the Book model.
# It includes custom validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # Custom validation: publication_year must not exceed current year.
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer serializes the Author model.
# It includes the name field and a nested BookSerializer to dynamically show related books.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer: shows all books written by this author.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]
