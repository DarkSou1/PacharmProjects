class Worker:
    worker_count = 0

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
        Worker.worker_count += 1


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def total_income(self):
        print(f'{sum(self._income.values())} т. р')


if __name__ == '__main__':
    a = Position('Ivan', 'Ivanov', 'Pilot', {'wage': 50, 'bonus': 10})
    a.get_full_name()
    a.total_income()