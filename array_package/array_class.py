class Array:

    def __init__(self, arr):
        self.arr = arr

    def display(self):
        print("Array elements are:", self.arr)

    def find_sum(self):
        print("Sum of elements =", sum(self.arr))

    def find_max(self):
        print("Maximum element =", max(self.arr))

    def find_min(self):
        print("Minimum element =", min(self.arr))

    def search(self, key):
        if key in self.arr:
            print(key, "found in array")
        else:
            print(key, "not found in array")

    def sort_array(self):
        self.arr.sort()
        print("Sorted array:", self.arr)

    # ---------------- MATRIX OPERATIONS ---------------- #

    def matrix_add(self, A, B):
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                row.append(A[i][j] + B[i][j])
            result.append(row)
        print("Matrix Addition Result:", result)

    def matrix_subtract(self, A, B):
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                row.append(A[i][j] - B[i][j])
            result.append(row)
        print("Matrix Subtraction Result:", result)

    def matrix_multiply(self, A, B):
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                sum_val = 0
                for k in range(len(B)):
                    sum_val += A[i][k] * B[k][j]
                row.append(sum_val)
            result.append(row)
        print("Matrix Multiplication Result:", result)

    def matrix_transpose(self, A):
        result = []
        for i in range(len(A[0])):
            row = []
            for j in range(len(A)):
                row.append(A[j][i])
            result.append(row)
        print("Matrix Transpose Result:", result)

    def dot_product(self, A, B):
        if len(A) != len(B):
            print("Dot product not possible (different sizes)")
            return

        result = 0
        for i in range(len(A)):
            result += A[i] * B[i]

        print("Dot Product =", result)

    def matrix_range(self, A):
        maximum = A[0][0]
        minimum = A[0][0]

        for row in A:
            for value in row:
                if value > maximum:
                    maximum = value
                if value < minimum:
                    minimum = value

        print("Matrix Maximum =", maximum)
        print("Matrix Minimum =", minimum)
        print("Matrix Range (max - min) =", maximum - minimum)

    def replace_diagonal(self, A):
        if len(A) != len(A[0]):
            print("Diagonal replacement only possible for square matrix!")
            return

        new_val = int(input("Enter value to replace all diagonal elements: "))

        for i in range(len(A)):
            A[i][i] = new_val

        print("Matrix after replacing diagonal:")
        for row in A:
            print(row)
