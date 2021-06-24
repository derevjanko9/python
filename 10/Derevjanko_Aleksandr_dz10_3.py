class Cell:
    def __init__(self, number_cell):
        self.number_cell = number_cell

    def __add__(self, other):
        cell = Cell(self.number_cell + other)
        return cell

    def __sub__(self, other):
        if self.number_cell > other:
            cell = Cell(self.number_cell - other)
            return cell
        else:
            print('уменьшение невозможно')

    def __mul__(self, other):
        cell = Cell(self.number_cell * other)
        return cell

    def __floordiv__(self, other):
        cell = Cell(self.number_cell // other)
        return cell

    def make_order(self, row):
        number = self.number_cell // row
        result = ''
        for i in range(1, number + 1):
            result += '*' * row
            result += '\n'
        result_ = '*' * (self.number_cell % row)
        return f'{result} {result_}'


cell_1 = Cell(17)
cell_2 = Cell(25)
print((cell_1.__add__(cell_2.number_cell)).make_order(5))
cell_1.__sub__(cell_2.number_cell)
print((cell_1.__mul__(cell_2.number_cell)).make_order(5))
print((cell_2.__floordiv__(cell_1.number_cell)).make_order(5))