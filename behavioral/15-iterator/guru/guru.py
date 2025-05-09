from __future__ import annotations

from collections.abc import Iterator, Iterable
from typing import Any

"""
To create an iterator in Python, there are two ABSTRACT classes from the
built-in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in the iterator.
"""


class AlphabeticalOrderIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms. These classes
    store the current traversal position at all times.
    """

    """
    `_position` attribute stores the current traversal position. An iterator may
    have a lot of other fields for storing iteration state, especially when it
    is supposed to work with a particular kind of collection.
    """
    _position: int = None

    """
    This attribute indicates the traversal direction.
    """
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False):
        self.collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.
        """

        try:
            value = self.collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    """
    Concrete Collections provide one or several methods for retrieving fresh
    iterator instances, compatible with the collection class.
    """

    def __init__(self, collection: list[Any] | None = None):
        self._collection = collection or []

    def __getitem__(self, index: int):
        return self._collection[index]

    def __iter__(self):
        """
        The __iter__() method returns the iterator object itself, by default we
        return the iterator in ascending order.
        """

        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    # The client code may or may not know about the Concrete Iterator or
    # Collection classes, depending on the level of indirection you want to keep
    # in your program.
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")

# Straight traversal:
# First
# Second
# Third
#
# Reverse traversal:
# Third
# Second
# First
