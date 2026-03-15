if __name__ == "__main__":
    class Clothing:
        def __init__(self, brand: str, size: str) -> None:
            """ Инициализация одежды
                brand: Бренд
                size: Размер
            """
            self._brand = brand  # Инкапсуляция: бренд защищен
            self.size = size

        def get_brand(self) -> str:
            return self._brand

        def wear(self) -> str:
            return f"Wearing {self._brand} clothing"

        def __str__(self) -> str:
            return f"{self._brand} clothing, size {self.size}"

        def __repr__(self) -> str:
            return f"Clothing(brand='{self._brand}', size='{self.size}')"


    class TShirt(Clothing):
        """Класс футболки"""

        def __init__(self, brand: str, size: str, color: str) -> None:

            super().__init__(brand, size)
            self.color = color

        def wear(self) -> str:
            """
            Изменение метода надевания
                str: Процесс надевания футболки
            """
            return f"Putting on {self.color} {self._brand} t-shirt"

        def wash(self) -> str:
            """Унаследованный метод"""
            return f"Wash {self.color} t-shirt in cold water"

        def __str__(self) -> str:
            return f"T-Shirt: {self._brand}, {self.color}, size {self.size}"

        def __repr__(self) -> str:
            return f"TShirt(brand='{self._brand}', size='{self.size}', color='{self.color}')"


    class Jeans(Clothing):
        """Класс джинсов"""

        def __init__(self, brand: str, size: str, length: int) -> None:
            super().__init__(brand, size)
            self.length = length

        def wear(self) -> str:
            """
            Перегрузка метода надевания
                str: Процесс надевания джинсов
            """
            return f"Putting on {self._brand} jeans, length {self.length}"

        def wash(self) -> str:
            """Унаследованный метод"""
            return f"Wash jeans inside out"

        def __str__(self) -> str:
            return f"Jeans: {self._brand}, size {self.size}, length {self.length}"

        def __repr__(self) -> str:
            return f"Jeans(brand='{self._brand}', size='{self.size}', length={self.length})"


    # Write your solution here
    pass
