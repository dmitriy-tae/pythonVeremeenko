print('\nПРАКТИЧЕСКОЕ ЗАДАНИЕ №1 *************************************')
print('Светофор\n')
import time
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        print(f'{self.__color[0]} сигнал светофора - 7 секунд')
        time.sleep(7)
        print(f'{self.__color[1]} сигнал светофора - 2 секунды')
        time.sleep(2)
        print(f'{self.__color[2]} сигнал светофора - 2 секунды')
        time.sleep(2)
trLight_1 = TrafficLight()
trLight_1.running()


print('\nПРАКТИЧЕСКОЕ ЗАДАНИЕ №2 *************************************')
print('Дорога\n')
class Road:
    def __init__(self, length, width):
        self._l = length
        self._w = width
    def mass(self):
        r = int(self._l * self._w * 25 * 5 / 1000)
        print(f'Длина дороги = {self._l} метров')
        print(f'Ширина дороги = {self._w} метров')
        print(f'Масса асфальта, необходимого для покрытия всей дороги = {r} тонн')
road_1 = Road(5000, 20)
road_1.mass()


print('\nПРАКТИЧЕСКОЕ ЗАДАНИЕ №3 *************************************')
print('Работник\n')
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}
class Position(Worker):
    def get_full_name(self):
        print(f'- полное имя сотрудника: {self.s} {self.n}')
    def get_total_income(self):
        print('- доход сотрудника с учетом премии: ', self._income['wage'] + self._income['bonus'], 'рублей')
employee_1 = Position('Дмитрий', 'Веремеенко', 'маркетолог', 100000, 30000)
print('Экземпляр класса Position №1')
employee_1.get_full_name()
employee_1.get_total_income()
print('Проверка атрибутов:', '    name:', employee_1.n,'    surname:', employee_1.s,'    position:', employee_1.p, '    wage:', employee_1._income['wage'], '    bonus:', employee_1._income['bonus'])

employee_2 = Position('Иван', 'Иванов', 'программист', 200000, 50000)
print('\nЭкземпляр класса Position №2')
employee_2.get_full_name()
employee_2.get_total_income()
print('Проверка атрибутов:', '    name:', employee_2.n,'    surname:', employee_2.s,'    position:', employee_2.p, '    wage:', employee_2._income['wage'], '    bonus:', employee_2._income['bonus'])

print('\nПРАКТИЧЕСКОЕ ЗАДАНИЕ №4 *************************************')
print('Машина\n')
class Car:
    def __init__(self, speed, color, name, direction, speed_now):
        self.s = speed
        self.c = color
        self.n = name
        self.is_police = {'direction': direction, 'speed_now': speed_now}
    def go(self):
        if self.is_police['speed_now'] > 0:
            print('Машина поехала')
    def stop(self):
        if self.is_police['speed_now'] == 0:
            print('Машина стоит')
    def turn(self):
        if self.is_police['speed_now'] > 0:
            print('Машина двигается', self.is_police['direction'])
    def show_speed(self):
        if self.is_police['speed_now'] > 0:
            print('В настоящий момент машина двигается со скоростью', self.is_police['speed_now'], 'км/час')
class TownCar(Car):
    name = 'TownCar'
    def show_speed(self):
        if self.is_police['speed_now'] > 0:
            print('В настоящий момент машина двигается со скоростью', self.is_police['speed_now'], 'км/час')
        if self.is_police['speed_now'] > 60:
            print('что превышает максимально допустимую скорость = 60 км/ч')
car_1 = TownCar('180 км/ч', 'красный', 'KIA SPORTAGE', 'прямо', 70)
print(car_1.name)
print('Цвет:', car_1.c)
print('Максимальная скорость:', car_1.s)
car_1.go()
car_1.stop()
car_1.turn()
car_1.show_speed()
class SportCar(Car):
    name = '\nSportCar'
car_2 = SportCar('250 км/ч', 'желтый', 'Audi R8', 'направо', 40)
print(car_2.name)
print('Цвет:', car_2.c)
print('Максимальная скорость:', car_2.s)
car_2.go()
car_2.stop()
car_2.turn()
car_2.show_speed()
class WorkCar(Car):
    name = '\nWorkCar'
    def show_speed(self):
        if self.is_police['speed_now'] > 0:
            print('В настоящий момент машина двигается со скоростью', self.is_police['speed_now'], 'км/час')
        if self.is_police['speed_now'] > 40:
            print('что превышает максимально допустимую скорость = 40 км/ч')
car_3 = WorkCar('110 км/ч', 'зеленый', 'КамАЗ-5490', 'прямо', 80)
print(car_3.name)
print('Цвет:', car_3.c)
print('Максимальная скорость:', car_3.s)
car_3.go()
car_3.stop()
car_3.turn()
car_3.show_speed()
class PoliceCar(Car):
    name = '\nPoliceCar'
car_4 = WorkCar('220 км/ч', 'белый', 'Хонда', 'прямо', 0)
print(car_4.name)
print('Цвет:', car_4.c)
print('Максимальная скорость:', car_4.s)
car_4.go()
car_4.stop()
car_4.turn()
car_4.show_speed()


print('\nПРАКТИЧЕСКОЕ ЗАДАНИЕ №5 *************************************\n')

class Stationery:
    title = 'КАНЦЕЛЯРСКАЯ ПРИНАДЛЕЖНОСТЬ\n'
    def __init__(self, color):
        self.c = color
    def draw(self):
        print(f'Запуск отрисовки:')
draw_start = Stationery('')
print(draw_start.title)
draw_start.draw()

class Pen(Stationery):
    def draw(self):
        print(f'- рисуем ручкой, цвет ручки {self.c}')
draw_pen = Pen('синий')
draw_pen.draw()

class Pencil(Stationery):
    def draw(self):
        print(f'- рисуем карандашом, цвет карандаша {self.c}')
draw_pencil = Pencil('красный')
draw_pencil.draw()

class Handle(Stationery):
    def draw(self):
        print(f'- отрисовка handle, цвет {self.c}')
draw_handle = Handle('зеленый')
draw_handle.draw()