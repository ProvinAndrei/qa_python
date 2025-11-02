import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('book_name, should_be_added', [
        ('Нормальная книга', True),
        ('К', True),
        ('Книга с ровно сорок символов в названиии', True),
        ('', False),
        ('Очень очень очень длинное название книги - больше сорока символов', False),
    ])
    def test_add_new_book_adds_book_without_genre(self, book_name, should_be_added, collector):
        collector.add_new_book(book_name)

        if should_be_added:
            assert book_name in collector.get_books_genre()
            assert collector.get_book_genre(book_name) == ""
        else:
            assert book_name not in collector.get_books_genre()

    def test_set_book_genre_sets_genre_for_existing_book(self, collector):
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")

        assert collector.get_book_genre("1984") == "Фантастика"

    def test_get_book_genre_returns_correct_genre(self, collector_with_books):
        genre = collector_with_books.get_book_genre("1984")
        assert genre == "Фантастика"

        assert collector_with_books.get_book_genre("Несуществующая книга") is None

    def test_get_books_with_specific_genre_returns_filtered_books(self, collector_with_books):
        fantasy_books = collector_with_books.get_books_with_specific_genre("Фантастика")

        assert fantasy_books == ["1984"]

        assert collector_with_books.get_books_with_specific_genre("Роман") == []

    def test_get_books_genre_returns_current_dictionary(self, collector_with_books):
        books_dict = collector_with_books.get_books_genre()

        assert isinstance(books_dict, dict)
        assert "1984" in books_dict
        assert "Оно" in books_dict
        assert "Ну погоди!" in books_dict
        assert books_dict["1984"] == "Фантастика"

    def test_get_books_for_children_returns_books_without_age_rating(self, collector_with_books):
        children_books = collector_with_books.get_books_for_children()

        assert "Ну погоди!" in children_books
        assert "1984" in children_books
        assert "Оно" not in children_books
        assert "Шерлок Холмс" not in children_books

    def test_add_book_in_favorites_adds_existing_book(self, collector):

        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")

        favorites = collector.get_list_of_favorites_books()
        assert "Гарри Поттер" in favorites

    def test_delete_book_from_favorites_removes_book(self, collector):

        collector.add_new_book("Маленький принц")
        collector.add_book_in_favorites("Маленький принц")

        collector.delete_book_from_favorites("Маленький принц")

        favorites = collector.get_list_of_favorites_books()
        assert "Маленький принц" not in favorites

    def test_get_list_of_favorites_books_returns_favorites_list(self, collector):

        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.add_book_in_favorites("Книга1")
        collector.add_book_in_favorites("Книга2")

        favorites = collector.get_list_of_favorites_books()

        assert isinstance(favorites, list)
        assert "Книга1" in favorites
        assert "Книга2" in favorites
        assert len(favorites) == 2
