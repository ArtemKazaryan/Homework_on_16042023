

# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ, ЕСЛИ ПОТРЕБУЕТСЯ  !!!!!!


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

# Решение:

class Fraction:
    count_obj = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.decimal_view = self.numerator / self.denominator
        Fraction.count_obj += 1
        print(f'Создана {self.count_obj}-я дробь: {self.numerator}/{self.denominator}.'
              f' Её десятичное значение равно: {self.decimal_view}')

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
print('Задание 1. Вывод результатов на экран:')
print()
fraction1 = Fraction(4, 5).decimal_view
fraction2 = Fraction(1, 2).decimal_view
print()
Fraction.summ(fraction1, fraction2)
Fraction.subtract(fraction1, fraction2)
Fraction.multiplic(fraction1, fraction2)
Fraction.division(fraction1, fraction2)
print()
Fraction.count_ex()
print()
print()


# Задание 2
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий.
# Также класс должен считать количество подсчетов температуры и
# возвращать это значение с помощью статического метода.

# Решение:

class TempConv:
    temp_counts_num = 0
    def __init__(self, value):
        self.value = value
        TempConv.temp_counts_num += 1

    @staticmethod
    def get_temp_counts_num():
        print(f'Подсчётов температуры произведено: {TempConv.temp_counts_num}')

    @staticmethod
    def to_Faringate(arg):
        res = arg * 1.8 + 32
        print(f'Конвертация: {arg} гр.C => {round(res, 2)} гр.F')
        return res

    @staticmethod
    def to_Celsius(arg):
        res = (arg - 32) / 1.8
        print(f'Конвертация: {arg} гр.F => {round(res, 2)} гр.C ')
        return res

print()
print('Задание 2. Вывод результатов на экран:')
print()
from_Cels_temp1 = TempConv(10).value
from_Cels_temp2 = TempConv(15).value
from_Faring_temp1 = TempConv(41).value
from_Faring_temp2 = TempConv(30).value

TempConv.to_Faringate(from_Cels_temp1)
TempConv.to_Faringate(from_Cels_temp2)
TempConv.to_Celsius(from_Faring_temp1)
TempConv.to_Celsius(from_Faring_temp2)
print()
TempConv.get_temp_counts_num()
print()
print()



# Задание 3
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

# Решение:

class MetricConvSI_EMS_SI:
    @staticmethod
    def сm_to_inch(cm):
        print(f'Конвертация: {cm} см = {round(cm / 2.54, 2)} дюймов')
        return round(cm / 2.54, 2)

    @staticmethod
    def inch_to_сm(inch):
        print(f'Конвертация: {inch} дюймов = {round(inch * 2.54, 2)} см')
        return round(inch * 2.54, 2)

    @staticmethod
    def m_to_foot(m):
        print(f'Конвертация: {m} метров = {round(m * 3.28, 2)} фт')
        return round(m * 3.28, 2)
    @staticmethod
    def foot_to_m(foot):
        print(f'Конвертация: {foot} фт = {round(foot / 3.28, 2)} метров')
        return round(foot / 3.28, 2)

    @staticmethod
    def km_to_mile(km):
        print(f'Конвертация: {km} км = {round(km / 1.61, 2)} миль')
        return round(km / 1.61, 2)

    @staticmethod
    def mile_to_km(mile):
        print(f'Конвертация: {mile} миль = {round(mile * 1.61, 2)} км')
        return round(mile * 1.61, 2)

    @staticmethod
    def kg_to_pound(kg):
        print(f'Конвертация: {kg} кг = {round(kg * 2.2, 2)} фунт')
        return round(kg * 2.2, 2)

    @staticmethod
    def pound_to_kg(pound):
        print(f'Конвертация: {pound} фунт = {round(pound / 2.2, 2)} кг')
        return round(pound / 2.2, 2)


print()
print('Задание 3. Вывод результатов на экран:')
print()
MetricConvSI_EMS_SI.сm_to_inch(25.4)
MetricConvSI_EMS_SI.inch_to_сm(10)
MetricConvSI_EMS_SI.m_to_foot(10)
MetricConvSI_EMS_SI.foot_to_m(32.8)
MetricConvSI_EMS_SI.km_to_mile(1.61)
MetricConvSI_EMS_SI.mile_to_km(1)
MetricConvSI_EMS_SI.kg_to_pound(10)
MetricConvSI_EMS_SI.pound_to_kg(22)
print()