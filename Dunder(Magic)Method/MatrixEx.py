class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Can only add Matrix with another Matrix.")

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to be added.")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[7, 8, 9], [10, 11, 12]])

result = m1 + m2
print("Resultant Matrix:")
print(result)
