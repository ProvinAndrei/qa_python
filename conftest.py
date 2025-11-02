import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def collector_with_books():
    collector = BooksCollector()

    collector.add_new_book("1984")
    collector.add_new_book("Оно")
    collector.add_new_book("Ну погоди!")
    collector.add_new_book("Шерлок Холмс")

    collector.set_book_genre("1984", "Фантастика")
    collector.set_book_genre("Оно", "Ужасы")
    collector.set_book_genre("Ну погоди!", "Мультфильмы")
    collector.set_book_genre("Шерлок Холмс", "Детективы")

    return collector
