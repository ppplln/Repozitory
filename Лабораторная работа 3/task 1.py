class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        "Название книги (только для чтения)."
        return self._name

    @property
    def author(self) -> str:
        """Автор книги (только для чтения)."""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
class PaperBook(Book):
    """Класс бумажной книги, наследующийся от Book."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем сеттер для проверки

    @property
    def pages(self) -> int:
        """Количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, "
                f"pages={self.pages!r})")


class AudioBook(Book):
    """Класс аудиокниги, наследующийся от Book"""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Продолжительность аудиокниги в часа"""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float(value)

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность: {self.duration} ч."

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, "
                f"duration={self.duration!r})")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    print("\n" + "=" * 50)
    print("Тестирование классов:")
    print("=" * 50)

    # Создание экземпляров
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
    audio_book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 12.5)

    print(f"Бумажная книга (str): {paper_book}")
    print(f"Бумажная книга (repr): {repr(paper_book)}")
    print(f"Аудиокнига (str): {audio_book}")
    print(f"Аудиокнига (repr): {repr(audio_book)}")

    # Проверка неизменяемости name и author
    print("\nПроверка неизменяемости базовых атрибутов:")
    try:
        paper_book.name = "Новое название"
    except AttributeError as e:
        print(f"Нельзя изменить name: {e}")

    try:
        audio_book.author = "Новый автор"
    except AttributeError as e:
        print(f"Нельзя изменить author: {e}")

    # Проверка валидации pages
    print("\nПроверка валидации pages:")
    try:
        paper_book.pages = -100
    except ValueError as e:
        print(f"Отрицательное значение: {e}")

    try:
        paper_book.pages = 100.5
    except TypeError as e:
        print(f"Нецелое значение: {e}")

    # Корректное изменение pages
    paper_book.pages = 1500
    print(f"pages успешно изменено на: {paper_book.pages}")

    # Проверка валидации duration
    print("\nПроверка валидации duration:")
    try:
        audio_book.duration = -5.5
    except ValueError as e:
        print(f"Отрицательное значение: {e}")

    try:
        audio_book.duration = "10.5"
    except TypeError as e:
        print(f"Нечисловое значение: {e}")

    # Корректное изменение duration
    audio_book.duration = 15.75
    print(f"duration успешно изменено на: {audio_book.duration}")