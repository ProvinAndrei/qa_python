import pytest
from test_data import TEST_BOOK_NAMES, GENRES


class TestBooksCollector:

    @pytest.mark.parametrize('book_name', TEST_BOOK_NAMES["VALID"])
    def test_add_new_book_with_valid_name(self, book_name, collector):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
        assert collector.get_book_genre(book_name) == ""

    @pytest.mark.parametrize('book_name', TEST_BOOK_NAMES["INVALID"])
    def test_add_new_book_with_invalid_name_not_added(self, book_name, collector):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_add_duplicate_book_not_added(self, collector):
        book_name = TEST_BOOK_NAMES["SINGLE"][5]
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert list(collector.get_books_genre().keys()).count(book_name) == 1

    def test_set_book_genre(self, collector):
        book_name = TEST_BOOK_NAMES["SINGLE"][0]
        genre = GENRES["WITHOUT_AGE_RATING"][0]
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_book_genre_returns_correct_genre(self, collector):
        book_name = TEST_BOOK_NAMES["SINGLE"][0]
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ""
        assert collector.get_book_genre("Несуществующая") is None

    def test_get_books_with_specific_genre(self, collector):
        book_name = TEST_BOOK_NAMES["SINGLE"][0]
        valid_genre = GENRES["WITHOUT_AGE_RATING"][0]
        invalid_genre = GENRES["INVALID"][0]
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, valid_genre)
        fantasy_books = collector.get_books_with_specific_genre(valid_genre)
        invalid_genre_books = collector.get_books_with_specific_genre(invalid_genre)
        assert book_name in fantasy_books
        assert invalid_genre_books == []

    def test_get_books_genre(self, collector):
        book_name = TEST_BOOK_NAMES["SINGLE"][0]
        collector.add_new_book(book_name)
        books_dict = collector.get_books_genre()
        assert book_name in books_dict
        assert books_dict[book_name] == ""

    def test_get_books_for_children(self, collector):
        child_book = TEST_BOOK_NAMES["SINGLE"][1]
        adult_book = TEST_BOOK_NAMES["SINGLE"][2]
        child_genre = GENRES["WITHOUT_AGE_RATING"][1]
        adult_genre = GENRES["WITH_AGE_RATING"][0]
        collector.add_new_book(child_book)
        collector.add_new_book(adult_book)
        collector.set_book_genre(child_book, child_genre)
        collector.set_book_genre(adult_book, adult_genre)
        children_books = collector.get_books_for_children()
        assert child_book in children_books
        assert adult_book not in children_books

    def test_add_book_in_favorites(self, collector):
        book_name = TEST_BOOK_NAMES["SINGLE"][0]
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name in favorites
        assert favorites.count(book_name) == 1

    def test_delete_book_from_favorites(self, collector):
        book_name = TEST_BOOK_NAMES["SINGLE"][0]
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name not in favorites

    def test_get_list_of_favorites_books_book_list_equal(self, collector):
        book1 = TEST_BOOK_NAMES["SINGLE"][3]
        book2 = TEST_BOOK_NAMES["SINGLE"][4]
        collector.add_new_book(book1)
        collector.add_new_book(book2)
        collector.add_book_in_favorites(book1)
        collector.add_book_in_favorites(book2)
        list_of_favorites_books = collector.get_list_of_favorites_books()
        assert set(list_of_favorites_books) == set(collector.favorites)
