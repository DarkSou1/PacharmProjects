import time


class TrafficLight:
    __color = 'красный', 'жёлтый', 'зелёный'

    @classmethod
    def running(cls):
        for i in cls.__color:
            if i == 'красный':
                print(f'{i} горит!')
                time.sleep(7)
            elif i == 'жёлтый':
                print(f'{i} горит!')
                time.sleep(2)
            else:
                print(f'{i} горит!')
                time.sleep(10)


if __name__ == '__main__':
    a = TrafficLight()
    print(a.running())
