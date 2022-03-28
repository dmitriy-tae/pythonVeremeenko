print('\nПРАКТИЧЕСКОЕ ЗАДАНИЕ №1 *************************************')
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def m_1(self):
        print(f'{self.matrix[0]}')
        print(f'{self.matrix[1]}')
        print(f'{self.matrix[2]}')
    def __str__(self):
        print('\nНовая матрица - результат сложения двух предыдущих матриц:\n')
        for list_in_list in self.matrix:
            print(list_in_list, end='')
            print('')
        return ''
    def __add__(self, other):
        num_row = range(len(self.matrix))
        for element_m1 in num_row:
            num_row_other = range(len(other.matrix[element_m1]))
            for element_m2 in num_row_other:
                self.matrix[element_m1][element_m2] = self.matrix[element_m1][element_m2] + other.matrix[element_m1][element_m2]
        print(Matrix.__str__(self))
        return ''
matrix_1 = Matrix([[3, 5, 3], [2, 4, 6], [1, 6, 8]])
print('\nПервая матрица\n')
matrix_1.m_1()
matrix_2 = Matrix([[3, 8, 5], [3, 6, 4], [-1, 5, 6]])
print('\nВторая матрица\n')
matrix_2.m_1()
print(matrix_1.__add__(matrix_2))



print('\nПРАКТИЧЕСКОЕ ЗАДАНИЕ №2 *************************************')
print('Расчёт суммарного расхода ткани на производство одежды\n')
from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        if size < 30:
            print('Мы делаем пальто не менее 30-го размера')
            print('Поэтому рассчитаем расход ткани для 30-го размера')
            self.size = 30
        elif size > 60:
            print('Мы делаем пальто не более 60-го размера')
            print('Поэтому рассчитаем расход ткани для 60-го размера')
            self.size = 60
        else:
            self.__size = size
    def info(self):
        return f'инфа {self.__size}'
    @abstractmethod
    def coat(self):
        print('Расход ткани для пошивки пальто')
    @abstractmethod
    def suit(self):
        print('Расход ткани для пошивки костюма')
    @abstractmethod
    def total(self):
        print('Общий расход ткани')

class Clothes_2(Clothes):
    def coat(self):
        result_coat = int((self.size / 6.5 + 0.5) * 100) / 100
        print(f'Расход ткани для пошивки пальто = {result_coat}')
    def suit(self):
        # сделал не в метрах, а в сантиметрах, поэтому значение уменьшил в 100 раз
        # иначе, как мне показалось, будет слишклом много ткани
        # для этого в формулу добавил "/100"
        result_suit = int(2 * self.height + 0.3) / 100   #- сделал не в метрах, а в сантиметрах, поэтому значение уменьшил в 100 раз
        print(f'Расход ткани для пошивки костюма = {result_suit}')
    def total(self):
        total_suit = (int((self.size / 6.5 + 0.5) * 100) / 100) + (int(2 * self.height + 0.3) / 100)
        print(f'Общий расход ткани = {total_suit}')
a = int(input('Введите размер пальто: '))
b = int(input('Введите свой рост в сантиметрах для пошивки костюма: '))
cl_1 = Clothes_2(a, b)
cl_1.coat()
cl_1.suit()
cl_1.total()



print('\nПРАКТИЧЕСКОЕ ЗАДАНИЕ №3 *************************************')
print('Работа с органическими клетками\n')
class Cell:
    def __init__(self, num_of_cells):
        self.num_of_cells = int(num_of_cells)
    def __add__(self, other):
        sum_cells = self.num_of_cells + other.num_of_cells
        print('\nСумма ячеек двух клеток =', sum_cells)
        return ''
    def __mul__(self, other):
        mul_cells = self.num_of_cells * other.num_of_cells
        print('Произведение количества ячеек двух клеток =', mul_cells)
        return ''
    def __truediv__(self, other):
        div_cells = self.num_of_cells // other.num_of_cells
        print('Целочисленное деление количества ячеек двух клеток =', div_cells)
        return ''
    def __sub__(self, other):
        difference_cells = self.num_of_cells - other.num_of_cells
        if difference_cells <= 0:
            print('Операция вычитания двух ячеек клеток невозможна, так как разница ячеек меньше или равна нулю\n')
        if difference_cells > 0:
            print('Разность количества ячеек двух клеток =', difference_cells, '\n')
        return ''
    def make_order(self, rows):
        result = 'Ячейки клетки по рядам\n\n'
        for i in range(int(self.num_of_cells / rows)):
            result += 'cel ' * rows + '\n'
        result += 'cel ' * (self.num_of_cells % rows)
        print(result)
        return ''
one = Cell(int(input('Введите количество ячеек первой клетки: ')))
two = Cell(int(input('Введите количество ячеек второй клетки: ')))
print(one + two)
print(one * two)
print(one / two)
print(one - two)
print(one.make_order(5))
print(two.make_order(5))
print('end')