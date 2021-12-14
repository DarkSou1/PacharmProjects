# Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными; protected
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
class Road:

    def mass_asphalt(self, lenght, width, depth):
        self._lenght = lenght
        self._width = width
        self._depth = depth

    def calc_asphalt(self):
        calc = self._lenght * self._width * 25 * self._depth
        calc = calc // 1000
        print(f'{self._lenght} м * {self._width} м * 25 кг *{self._depth} = {calc} т')


if __name__ == '__main__':
    a = Road()
    a.mass_asphalt(20, 5000, 5)
    a.calc_asphalt()