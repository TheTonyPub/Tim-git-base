class FactorialCalculator:
    """
    Класс для вычисления факториала с кэшированием результатов.
    """

    def __init__(self):
        self._cache = {0: 1, 1: 1}

    def calculate(self, n):
        """
        Вычисляет факториал числа n итеративно с кэшированием.

        Args:
            n: неотрицательное целое число

        Returns:
            n! (произведение всех чисел от 1 до n)

        Raises:
            TypeError: если n не является целым числом
            ValueError: если n отрицательное
        """
        if not isinstance(n, int):
            raise TypeError("Аргумент должен быть целым числом")
        if n < 0:
            raise ValueError("Факториал определён только для неотрицательных чисел")

        # Проверяем кэш
        if n in self._cache:
            return self._cache[n]

        # Находим ближайшее кэшированное значение
        start = max(self._cache.keys())
        result = self._cache[start]

        # Вычисляем недостающие значения
        for i in range(start + 1, n + 1):
            result *= i
            self._cache[i] = result

        return result

    def clear_cache(self):
        """Очищает кэш."""
        self._cache = {0: 1, 1: 1}


# Простая функция-обёртка для удобства
def factorial(n):
    """Простая функция для вычисления факториала."""
    calculator = FactorialCalculator()
    return calculator.calculate(n)


if __name__ == "__main__":
    calc = FactorialCalculator()

    # Тестирование
    test_cases = [0, 1, 5, 10, 15, 20]
    for test in test_cases:
        result = calc.calculate(test)
        print(f"{test}! = {result}")

    # Демонстрация кэширования
    import time

    print("\nТест производительности:")
    start_time = time.time()
    calc.calculate(1000)
    first_call = time.time() - start_time

    start_time = time.time()
    calc.calculate(1000)
    second_call = time.time() - start_time

    print(f"Первый вызов: {first_call:.6f} секунд")
    print(f"Второй вызов (из кэша): {second_call:.6f} секунд")