                # Домашнее задание по теме "Логирование"


import unittest
import logging
from runner import Runner  # Предполагаю, что ваш класс Runner находится в файле runner.py

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    filename='runner_tests.log',  # Имя файла для записи логов
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class RunnerTest(unittest.TestCase):

    def test_run(self):
        try:
            r1 = Runner(123)  # Передаем неверный тип данных для имени
        except Exception as e:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.exception(e)

    def test_walk(self):
        try:
            r1 = Runner("Вася", -5)  # Передаем отрицательное значение скорости
            r1.walk()
        except Exception as e:
            logging.warning("Неверная скорость для Runner")
            logging.exception(e)

if __name__ == "__main__":
    unittest.main()