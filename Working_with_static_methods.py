

# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ  !!!!!!


# Домашняя работа на 16.04.2023.


# Модуль 10. Объектно-ориентированное
# программирование
#
# Тема: Статические методы

# Задание 1
# Доделать задание 4 от урока за 08.04.2023, которое звучит так:
# Создайте класс "Дробь". Необходимо хранить в полях класса: числитель
# и знаменатель. Можно не делать реализацию методов класса для ввода данных,
# вывода данны и реализацию доступа к отдельным полям через методы класса.
# Также создайте методы класса для выполнения арифметических операций (сложение,
# вычитание, умножение, деление и т.д.)
# К уже реализованному классу «Дробь» добавьте статический метод,
# который при вызове возвращает количество созданных объектов класса «Дробь».
#
# Решение:

class Fraction:
    count_obj = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.float_view = self.numerator / self.denominator
        Fraction.count_obj += 1
        print(f'Создана {self.count_obj}-я дробь: {self.numerator}/{self.denominator}. Её десятичное значение равно: {self.float_view}')

    @staticmethod
    def count_ex():
        print(f'Экземпляров класса {Fraction.__name__} создано: {Fraction.count_obj}')

    @staticmethod
    def summ(fract1, fract2):
        print(f'Сумма двух дробей равна {fract1 + fract2}')
        return fract1 + fract2

    @staticmethod
    def subtract(fract1, fract2):
        print(f'Разность двух дробей равна {round(fract1 - fract2, 3)}')
        return fract1 - fract2

    @staticmethod
    def multiplic(fract1, fract2):
        print(f'Произведение двух дробей равно {round(fract1 * fract2, 3)}')
        return round(fract1 * fract2, 3)

    @staticmethod
    def division(fract1, fract2):
        print(f'Частное от деления двух дробей равно {round(fract1 / fract2, 3)}')
        return round(fract1 / fract2, 3)

print()
fraction1 = Fraction(4, 5)
fraction2 = Fraction(1, 2)
print()
Fraction.summ(fraction1.float_view, fraction2.float_view)
Fraction.subtract(fraction1.float_view, fraction2.float_view)
Fraction.multiplic(fraction1.float_view, fraction2.float_view)
Fraction.division(fraction1.float_view, fraction2.float_view)
print()
Fraction.count_ex()











# @staticmethod
# def summ():
#     Fraction

# def subtraction(self):
    #
    # def multiplication(self):
    #
    # def division(self):

#
#
#
# Задание 2
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры и
# возвращать это значение с помощью статического метода.
#
#
#
# Задание 3
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.