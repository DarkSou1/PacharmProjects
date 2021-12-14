class Car(object):  # базовый класс
    count = 0

    def __init__(self, speed, color, name, is_polise=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise
        Car.count += 1

    def go(self):
        print(f'{self.name} машина поехала')

    def stop(self):
        print(f'{self.name}машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'машина повернула {self.direction}')

    def show_speed(self, speed):
        print()


class TownCar(Car):

    def __init__(self, speed, color, name, is_polise=False):
        super().__init__(speed, color, name, is_polise=False)

    def show_speed(self):  # переопределённый метод
        if self.speed > 60:
            print(f'Превышение скорости!')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_polise=False):
        super().__init__(speed, color, name, is_polise=False)

    def show_speed(self):
        if self.speed > 40:
            print(f'превышение скорости!')


class SportCar(Car):

    def __init__(self, speed, color, name, is_polise=False):
        super().__init__(speed, color, name, is_polise=False)


class PoliseCar(Car):

    def __init__(self, speed, color, name, is_polise=False):
        super().__init__(speed, color, name, is_polise=False)


if __name__ == '__main__':
    a = TownCar(55, 'green', 'Lexus', is_polise=False)
    a.show_speed()
    print(a.speed)
    print(a.name)
    print(a.color)
    print(a.is_polise)
    b = WorkCar(45, 'red', 'Lada', is_polise=False)
    b.go()
    b.turn('налево')
    b.stop()
    b.show_speed()
    print(Car.count)
