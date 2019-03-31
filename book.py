"""Created by Bob Zwolinski on 2019-03-18."""

import enum

PAGE_THICKNESS = 0.002
HARD_COVER_THICKNESS = 0.25
SOFT_COVER_THICKNESS = 0.004


class CoverType(enum.Enum):
    HARDCOVER = 0
    SOFTCOVER = 1


class Book(object):

    def __init__(self, title, author):
        # Store title as a tuple of lower case strings without spaces.
        self.__title = Book.TransformTitle(title)
        self.__author = tuple(author)
        self.__edition = None
        self.__pages = None
        self.__cover_type = None

    @staticmethod
    def TransformTitle(title):
        """Returns a title string as lower case title words in a tuple."""
        return tuple(title.lower().split(" "))

    def GetTitle(self):
        """Returns the raw title."""
        return self.__title

    def GetTitleFormatted(self):
        """Returns the title as a string of spaced, capitalized words."""
        capitalized = []
        for word in self.__title:
            capitalized.append(str(word).capitalize())
        return ' '.join(capitalized)
        
    def GetAuthor(self):
        """Returns the raw author."""
        return self.__author

    def GetAuthorAsString(self):
        """Returns the author as a name string."""
        first = self.__author[0] + " " if len(self.__author[0]) else ""
        middle = self.__author[1]
        last = " " + self.__author[2] if len(self.__author[1]) else self.__author[2]
        return ''.join((first, middle, last))

    def GetEdition(self):
        return self.__edition

    def SetEdition(self, edition):
        self.__edition = edition

    def GetPages(self):
        return self.__pages

    def SetPages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            raise ValueError("pages cannot be unset or zero")

    def GetCoverType(self):
        return self.__cover_type

    def SetCoverType(self, cover_type):
        self.__cover_type = cover_type

    def GetThickness(self):
        """Returns the thickness of the book."""
        if self.GetPages() is None or self.GetPages() == 0:
            return 0.0
        pages_thickness = self.GetPages() * PAGE_THICKNESS
        cover_thickness = 0.0
        if self.__cover_type == CoverType.HARDCOVER:
            cover_thickness = 2 * HARD_COVER_THICKNESS
        elif self.__cover_type == CoverType.SOFTCOVER:
            cover_thickness = 2 * SOFT_COVER_THICKNESS
        else:
            raise Exception("unknown or unset CoverType")
        return cover_thickness + pages_thickness

    def __eq__(self, other):
        """Implements == operator."""
        return self.__title == other.GetTitle() and self.__author == other.GetAuthor()




