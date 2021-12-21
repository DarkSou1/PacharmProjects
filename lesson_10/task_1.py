class Matrix(object):

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        str_matrix = [' '.join(list(map(str, row))) + '\n' for row in self.matrix_list]
        return ''.join(str_matrix)

    def __add__(self, other):
        sum_marix = [[col_1 + col_2 for (col_1, col_2) in zip(row_1, row_2)]
                     for (row_1, row_2) in zip(self.matrix_list, other.matrix_list)]
        return Matrix(sum_marix)


if __name__ == '__main__':
    a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    print(a)
    c = a + b
    print(c)
