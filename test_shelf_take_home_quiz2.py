"""CS330 Spring 2019: Quiz 2 (take home)."""

import unittest
import shelf
import book

# Steps to consider when writing any unit test:
# 1) Create an instance of the object whose behavior you want to test.
# 2) Ensure that the instance is initialized appropriately to exhibit the behavior need to meet the test objective.
# 3) Use the TestCase methods (self.assertXXXXX()) to show the test objective is met.
# 4) Verify object state before and after (where needed) to show that test actions affect the object's state.
# 5) Run your test class the same way you'd run any Python program.

# PyUnit Docs: https://docs.python.org/3/library/unittest.html


class TestShelf(unittest.TestCase):
    """Tests Shelf behavior."""

    def setUp(self):
        """Create instances of Shelf and Book class to ultilize in unit tests"""
        self.test_shelf = shelf.Shelf(72,12,12)
        self.test_book = book.Book("Anne of Green Gables", ("L", "M", "Montgomery"))
        self.test_book.SetPages(460)
        self.test_book.SetCoverType(book.CoverType.HARDCOVER)
    # Write unit tests for these Shelf class methods and behaviors:

    def testMakeShelfInstance(self):
        """Tests that the Shelf constructor returns an instance of the Shlef class."""
        self.assertIsInstance(self.test_shelf, shelf.Shelf)

    def test_AddBook(self):
        """Tests that a book is successfully added to a shelf."""
        book_count_before = self.test_shelf.GetBookCount()
        self.test_shelf.AddBook(self.test_book)
        book_count_after = self.test_shelf.GetBookCount()
        self.assertEqual(book_count_after, book_count_before + 1)

    def test_RemoveBook(self):
        """Tests that a book is successfully removed from a shelf."""
        self.test_shelf.AddBook(self.test_book)
        book_count_before = self.test_shelf.GetBookCount()
        self.test_shelf.RemoveBook("Anne of Green Gables")
        book_count_after = self.test_shelf.GetBookCount()
        self.assertEqual(book_count_after, book_count_before - 1)


    def test_AddBook_reduces_shelf_capacity(self):
        """Tests that shelf capacity is reduced after adding a book."""
        capacity_before = self.test_shelf.GetAvailableCapacity()
        self.test_shelf.AddBook(self.test_book)
        capacity_after = self.test_shelf.GetAvailableCapacity()
        self.assertGreater(capacity_before, capacity_after)


    def test_RemoveBook_increases_shelf_capacity(self):
        """Tests that shelf capacity is increased after removing a book."""
        self.test_shelf.AddBook(self.test_book)
        capacity_before = self.test_shelf.GetAvailableCapacity()
        self.test_shelf.RemoveBook("Anne of Green Gables")
        capacity_after = self.test_shelf.GetAvailableCapacity()
        self.assertLess(capacity_before, capacity_after)

    # Extra Credit
    def test_shelf_space_exhausted(self):
        """Tests that an exception is raised when adding a book to a shelf with insufficient space."""
        self.test_shelf2 = shelf.Shelf(1,1,1)
        with self.assertRaises(RuntimeError):
            self.test_shelf2.AddBook(self.test_book)

