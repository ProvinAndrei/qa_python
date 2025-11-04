import pytest
from main import BooksCollector
from test_data import BOOKS_FOR_FIXTURE


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    for book_name, genre in BOOKS_FOR_FIXTURE.items():
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
    return collector
