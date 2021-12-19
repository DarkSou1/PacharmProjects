class Stationery(object):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'{self.title} запуск отрисовки')


class Pencil(Stationery):

    def draw(self):
        print(f'{self.title} запуск отрисовки')


class Handle(Stationery):

    def draw(self):
        print(f'{self.title} запуск отрисовки')


if __name__ == '__main__':
    a = Pen('Ручка')
    a.draw()
    b = Pencil('Карандаш')
    b.draw()
    c = Handle('Маркер')
    c.draw()
