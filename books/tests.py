
from django.test import TestCase
from .models import Book

# Testing the model
class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testthing = Book.objects.create(title = "test_book", description="Testing book")
        testthing.save()


    def test_things_model(self):
        thing = Book.objects.get(id=1)
        actual_title = thing.title
        self.assertEqual(actual_title, "test_book")