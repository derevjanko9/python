class Matrix:
    def __init__(self, my_list):
        self.list = my_list

    def __add__(self, other):
        if len(self.list[0]) == len(other[0]) and len(self.list) == len(other):
            for indx in range(len(self.list)):
                for i in range(len(self.list[indx])):
                    self.list[indx][i] += other[indx][i]
        else:
            print(f'такие матрицы складывать нельзя')
        return self

    def __str__(self):
        for item in self.list:
            print(*(f'{digit: < 6}' for digit in item))


list_1 = [[31, 22], [37, 43], [51, 86]]
list_2 = [[15, 22], [37, 43], [51, 86]]
list_3 = [[1, 1], [1, 1], [1, 1]]
matrix_1 = Matrix(my_list=list_1)
matrix_2 = Matrix(my_list=list_2)
matrix_3 = Matrix(my_list=list_3)
matrix_1 + matrix_2.list + matrix_3.list
matrix_1.__str__()
