class Cage(object):
    # дальше идут перегрузки методов
    def __init__(self, count_cell):
        self.count_cell = count_cell

    def __str__(self):
        return f'Object Cage, with free cell = {self.count_cell}'

    def __add__(self, other):
        # на сколько я понял суть, то что всё dunder с математическими операциями
        # методы должны возврящать новый экземпляр класса
        return Cage(self.count_cell + other.count_cell)

    def __sub__(self, other):
        if self.count_cell - other.count_cell > 0:
            return Cage(self.count_cell - other.count_cell)
        else:
            raise ValueError('разность меньше нуля')

    def __mul__(self, other):
        return Cage(self.count_cell * other.count_cell)

    def __floordiv__(self, other):
        return Cage(self.count_cell // other.count_cell)

    def make_order(self, number_cells):
        result = []  # результирующий список
        while self.count_cell > 0:  # реализовал через цикл while так как другого способа пока не придумал
            if self.count_cell > number_cells:
                res = "*" * number_cells
            else:
                res = "*" * self.count_cell
            self.count_cell = self.count_cell - number_cells
            result.append(res)
        return '\n'.join(result)


if __name__ == '__main__':
    a = Cage(10)
    b = Cage(2)
    c = a + b
    print(c)
    c = a - b
    print(c)
    c = a * b
    print(c)
    c = a // b
    print(c)
    print(a.make_order(6))
