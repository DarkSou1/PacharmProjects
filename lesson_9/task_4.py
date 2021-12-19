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
        print(f'{self.name} машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'машина повернула {self.direction}')

    def show_speed(self, speed):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):  # переопределённый метод
        if self.speed > 60:
            print(f'Превышение скорости!')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'превышение скорости!')


class SportCar(Car):
    pass


class PoliseCar(Car):
    pass


if __name__ == '__main__':
    lexus = TownCar(55, 'green', 'Lexus', is_polise=False)
    lexus.show_speed()
    print(lexus.speed)
    print(lexus.name)
    print(lexus.color)
    print(lexus.is_polise)
    lada = WorkCar(45, 'red', 'Lada', is_polise=False)
    lada.go()
    lada.turn('налево')
    lada.stop()
    lada.show_speed()
    print(Car.count)
