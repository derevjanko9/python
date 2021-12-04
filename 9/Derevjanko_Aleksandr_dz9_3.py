class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        dict_1 = {'wage': wage, 'bonus': bonus}
        self._income = dict_1


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return f'{total_income}'


position_1 = Position('Александр', 'Пупкин', 'инженер', 30000, 1000)
print(position_1.name)
print(position_1.surname)
print(position_1.position)
print(position_1.get_full_name())
print(position_1.get_total_income())
