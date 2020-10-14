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
                    sequence = line.split(' ')
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
        print(total_distance)

    def optimalize(self):
        """
        losuję 2 pozycje A i B
        usuwam element z A i wstawiam na B
        jeśli długość trasy jest lepsza od najlepszej to ją zapamiętuję
        i tak 10^6 razy
        """
        pass

    

