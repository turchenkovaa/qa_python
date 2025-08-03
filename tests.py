from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #Проверяем, что у добавленной книги нет жанра
    def test_add_new_book_one_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.books_genre['Что делать, если ваш кот хочет вас убить'] == ''

    #Проверяем, что книге можно присвоить жанр
    def test_set_book_genre_one_book_genre_is_added(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.books_genre['Сияние'] == 'Ужасы'

    #Проверяем, что жанр книги выводится по ее имени
    def test_get_book_genre_one_book_got_genre(self, collector):
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_book_genre('Сияние') == 'Ужасы'
    
    #Проверяем, что выводится список книг опредененного жанра
    def test_get_books_with_specific_genre_two_horror_book(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        result = collector.get_books_with_specific_genre('Ужасы')
        assert result == ['Сияние', 'Оно']

    #Проверяем, что выводится текущий словарь книг
    def test_get_books_genre_of_three_books(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_genre() == {'Что делать, если ваш кот хочет вас убить' : 'Комедии', 'Сияние' : 'Ужасы', 'Оно' : 'Ужасы'}

    #Проверяем, что выводится список книг, подходящих детям
    def test_get_books_for_children_two_books_got_one_book_mult(self):
        collector = BooksCollector()
        collector.add_new_book('Волшебник изумрудного города')
        collector.set_book_genre('Волшебник изумрудного города', 'Мультфильмы')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_for_children() == ['Волшебник изумрудного города']

    #Проверяем, что книгу можно добавить в избранное
    def test_add_book_in_favorites_one_book_added_to_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        assert 'Сияние' in collector.favorites

    #Проверяем, что книгу можно удалить из избранного
    def test_delete_book_from_favorites_was_deleted_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        collector.delete_book_from_favorites('Сияние')
        assert len(collector.favorites) == 0

    #Проверяем, что выводится список избранного
    def test_get_list_of_favorites_books_got_list(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Сияние')
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Сияние')
        collector.add_book_in_favorites('Оно')
        assert collector.get_list_of_favorites_books() == ['Сияние', 'Оно']
