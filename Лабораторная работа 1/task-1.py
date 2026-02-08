# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class ServiceSubscription:
    """Класс, описывающий цифровую подписку"""

    def __init__(self, plan_name: str, monthly_fee: float, is_active: bool = True):
        """
        Инициализация подписки

        :param plan_name: Название тарифного плана
        :param monthly_fee: Ежемесячная стоимость (не может быть отрицательной)
        :param is_active: Статус активности подписки

        # Валидация
        if monthly_fee < 0:
            raise ValueError("Стоимость подписки не может быть отрицательной")
        if not plan_name.strip():
            raise ValueError("Название тарифного плана не может быть пустым")
        """
        self.plan_name = plan_name
        self.monthly_fee = monthly_fee
        self.is_active = is_active

    def upgrade_plan(self, new_plan: str, new_fee: float) -> str:
        """
        Смена тарифного плана на более дорогой

        :param new_plan: Название нового плана
        :param new_fee: Новая стоимость (должна быть выше текущей)
        :return: Название нового установленного плана

        # новая цена должна быть выше текущей
        >>> sub = ServiceSubscription("Basic", 9.99)
        >>> sub.upgrade_plan("Premium", 19.99)
        'Premium'
        >>> sub.plan_name
        'Premium'
        >>> sub.monthly_fee
        19.99
        """
        # Валидация для метода
        if new_fee <= self.monthly_fee:
            raise ValueError("Новая стоимость должна быть выше текущей")
        if not new_plan.strip():
            raise ValueError("Название нового плана не может быть пустым")

        self.plan_name = new_plan
        self.monthly_fee = new_fee
        return self.plan_name

    def cancel_subscription(self) -> bool:
        """
        Отмена подписки

        :return: Новый статус активности (False)

        >>> sub = ServiceSubscription("Premium", 19.99, is_active=True)
        >>> sub.cancel_subscription()
        False
        >>> sub.is_active
        False
        """
        self.is_active = False
        return self.is_active


class DigitalBook:
    """Класс, описывающий электронную книгу"""

    def __init__(self, title: str, total_pages: int, current_page: int = 1):
        """
        Инициализация книги

        :param title: Название книги
        :param total_pages: Общее количество страниц (должно быть > 0)
        :param current_page: Текущая страница (не может быть > total_pages)

        # Валидация
        if total_pages <= 0:
            raise ValueError("В книге должна быть хотя бы одна страница")
        if not (1 <= current_page <= total_pages):
            raise ValueError(f"Текущая страница ({current_page}) вне диапазона книги (1-{total_pages})")
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        """
        self.title = title
        self.total_pages = total_pages
        self.current_page = current_page

    def turn_page(self, forward: bool = True) -> int:
        """
        Перелистывание страницы

        :param forward: Если True - вперед, False - назад
        :return: Номер новой страницы.

        # страница не может выйти за пределы книги
        >>> book = DigitalBook("Python Guide", 100, 10)
        >>> book.turn_page(forward=True)
        11
        >>> book.current_page
        11
        >>> book.turn_page(forward=False)
        10
        >>> book.current_page
        10
        >>> book_at_start = DigitalBook("First Page", 50, 1)
        >>> book_at_start.turn_page(forward=False) # Нельзя перелистнуть назад с первой страницы
        1
        >>> book_at_end = DigitalBook("Last Page", 50, 50)
        >>> book_at_end.turn_page(forward=True) # Нельзя перелистнуть вперед с последней страницы
        50
        """
        if forward:
            if self.current_page < self.total_pages:
                self.current_page += 1
        else: # backward
            if self.current_page > 1:
                self.current_page -= 1
        return self.current_page

    def jump_to_page(self, page_number: int) -> int:
        """
        Переход на конкретную страницу

        :param page_number: Целевая страница
        :return: Новая текущая страница

        # Валидация: page_number должен быть в пределах от 1 до total_pages
        >>> book = DigitalBook("Python Guide", 100, 10)
        >>> book.jump_to_page(50)
        50
        >>> book.current_page
        50
        >>> book.jump_to_page(1)
        1
        >>> book.jump_to_page(101) # Попытка перейти на несуществующую страницу
        Traceback (most recent call last):
            ...
        ValueError: Целевая страница вне диапазона книги (1-100).
        """
        # Валидация для метода
        if not (1 <= page_number <= self.total_pages):
            raise ValueError(f"Целевая страница вне диапазона книги (1-{self.total_pages}).")
        self.current_page = page_number
        return self.current_page

class BankAccount:
    """Класс, описывающий банковский счет (нематериальная сущность)"""

    def __init__(self, owner: str, balance: float, currency: str):
        """
        Инициализация счета

        :param owner: Имя владельца
        :param balance: Текущий баланс. Не может быть отрицательным при открытии
        :param currency: Трехбуквенный код валюты (например, 'RUB', 'USD')

        # Валидация
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        if len(currency) != 3 or not currency.isalpha():
            raise ValueError("Код валюты должен состоять из 3-х буквенных символов")
        if not owner.strip():
            raise ValueError("Имя владельца не может быть пустым")
        """
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def deposit(self, amount: float) -> float:
        """
        Пополнение счета

        :param amount: Сумма пополнения (должна быть > 0)
        :return: Новый баланс после пополнения

        # Валидация: сумма пополнения должна быть положительной
        >>> account = BankAccount("Иван", 1000.0, "RUB")
        >>> account.deposit(500.0)
        1500.0
        >>> account.balance
        1500.0
        >>> account.deposit(0) # Попытка пополнить нулевой суммой
        Traceback (most recent call last):
            ...
        ValueError: Сумма пополнения должна быть положительной
        """
        # Валидация для метода
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")

        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Снятие наличных со счета

        :param amount: Сумма снятия (должна быть > 0 и не превышать баланс)
        :return: Сумма, которая была снята

        # Валидация: сумма снятия должна быть положительной и не превышать текущий баланс
        >>> account = BankAccount("Петр", 2000.0, "USD")
        >>> account.withdraw(300.0)
        300.0
        >>> account.balance
        1700.0
        >>> account.withdraw(2500.0) # Попытка снять больше, чем есть на балансе
        Traceback (most recent call last):
            ...
        ValueError: Недостаточно средств на счете или сумма снятия некорректна
        >>> account.withdraw(0)
        Traceback (most recent call last):
            ...
        ValueError: Недостаточно средств на счете или сумма снятия некорректна
        """
        # Валидация для метода
        if amount <= 0 or amount > self.balance:
            raise ValueError("Недостаточно средств на счете или сумма снятия некорректна")

        self.balance -= amount
        return amount


if __name__ == "__main__":
    doctest.testmod(verbose=True)
