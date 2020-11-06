import numpy as np
import random


def read_problem_from_file(file_path):
    line_counter = 0
    matrix_size = 0
    matrix = []
    with open(file_path, "r") as file:
        for line in file:
            if line_counter == 0:
                matrix_size = int(line)
                line_counter += 1
            elif line_counter <= matrix_size:
                row = line.strip().split(' ')
                row = [int(elem) for elem in row]
                matrix.append(row)
                line_counter += 1
            else:
                sequence = line.strip().split(' ')
                sequence = [int(elem) for elem in sequence]

    return matrix_size, np.array(matrix), sequence


class TravellingSalesManProblem:

    def __init__(self, file_path):
        matrix_size, matrix, sequence = read_problem_from_file(file_path)

        self.matrix_size = matrix_size
        self.matrix = matrix
        self.sequence = sequence

    def show_params(self):
        print("Matrix size: "+str(self.matrix_size))
        print(self.matrix)
        print("Sequence: "+str(self.sequence))

    def calculate_path(self):
        prev_elem_index = self.sequence[0]
        total_distance = 0
        for elem_index in self.sequence:
            distance = self.matrix[prev_elem_index][elem_index]
            prev_elem_index = elem_index
            total_distance += distance

        return total_distance

    def optimalize(self):
        """
        losuję 2 pozycje A i B
        usuwam element z A i wstawiam na B
        jeśli długość trasy jest lepsza od najlepszej to ją zapamiętuję
        i tak 10^6 razy
        """
        bestRoute = self.calculate_path()
        print("Original Route: " + str(bestRoute))

        for loop in range(100000):
            a = random.randrange(1, len(self.sequence)-1, 1)
            b = random.randrange(1, len(self.sequence)-1, 1)

            #print("a: " + str(a))
            #print("b: " + str(b))

            if a < b:
                temp = self.sequence[a]
                for i in range(a, b):
                    self.sequence[i] = self.sequence[i+1]
                self.sequence[b] = temp

            if a > b:
                temp = self.sequence[a]
                for i in range(a, b, -1):
                    self.sequence[i] = self.sequence[i-1]
                self.sequence[b] = temp

            actualRoute = self.calculate_path()

            if actualRoute < bestRoute:
                bestRoute = actualRoute
                bestSequence = []
                bestSequence = self.sequence

        print("Best sequence: " + str(bestSequence))
        print("Best Route: " + str(bestRoute))

        return bestRoute

    pass
