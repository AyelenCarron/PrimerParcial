import unittest
from models import Book, Magazine,LibraryItem
from utils import count_items, find_by_title



class TestLibrary(unittest.TestCase):
    def test_book_checkout(self):
        b = Book("Test", 1, "Author", 123)
        self.assertIn("Test", b.checkout("User"))

    def test_magazine_checkout(self):
        m = Magazine("Test Mag", 2, 10)
        self.assertIn("Test Mag", m.checkout("User"))

    def test_count(self):
        items = [Book("A", 1, "X", 100), Magazine("B", 2, 1)]
        counts = count_items(items)
        self.assertEqual(counts["book"], 1)
        self.assertEqual(counts["magazine"], 1)

    def test_find(self):
        items = [Book("Python", 1, "X", 100)]
        result = find_by_title(items, "python")
        self.assertEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()