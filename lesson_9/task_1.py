import time


class TrafficLight:
    __color = {'красный': 7, 'жёлтый': 3, 'зелёный': 10}

    @classmethod
    def running(cls):
        for color, slep in cls.__color.items():
            print(f'{color} горит!')
            time.sleep(slep)


if __name__ == '__main__':
    a = TrafficLight()
    a.running()
