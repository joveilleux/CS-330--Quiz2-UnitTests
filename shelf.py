"""Shelf Class Implementation. Created by Bob Zwolinski on 2019-03-18."""
import book

# All measurements are in inches.
DEFAULT_SHELF_LENGTH = 72.0
DEFAULT_SHELF_WIDTH = 12.0
DEFAULT_SHELF_HEIGHT = 12.0


class Shelf(object):
    """Functions as a library shelf that stores books."""
    def __init__(self, length=DEFAULT_SHELF_LENGTH, width=DEFAULT_SHELF_WIDTH, height=DEFAULT_SHELF_HEIGHT):
        # All attributes are private.
        self.__height = height
        self.__length = length
        self.__width = width
        self.__available_capacity = length
        self.__books = {}  # maps title to Book

    def AddBook(self, book):
        """Adds a book to the shelf if there is room."""
        thickness = book.GetThickness();
        if self.__available_capacity >= thickness:
            self.__books[book.GetTitle()] = book
            self._ReduceCapacity(thickness)
        else:
            raise RuntimeError("Add failed: No space available on shelf.")

    def RemoveBook(self, title):
        """Removes a book from the shelf if it resides on the shelf."""
        stored_title = book.Book.TransformTitle(title)
        if stored_title in self.__books:
            stored_book = self.__books[stored_title]
            thickness = stored_book.GetThickness()
            del self.__books[stored_title]
            self._IncreaseCapacity(thickness)
        else:
            raise RuntimeError("Removal failed: Book not found in shelf.")

    def GetBookCount(self):
        """Returns the number of books on the shelf."""
        return len(self.__books)

    def GetInitialCapacity(self):
        """Returns the initial capacity of the shelf."""
        return self.__length

    def GetAvailableCapacity(self):
        """Returns the space remaining on the shelf to store books."""
        return self.__available_capacity

    def _ReduceCapacity(self, thickness):
        """Reduces shelf capacity (after a book is added)."""
        self.__available_capacity -= thickness

    def _IncreaseCapacity(self, thickness):
        """Increases shelf capacity (after a book removed)."""
        self.__available_capacity += thickness
