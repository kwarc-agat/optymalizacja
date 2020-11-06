import numpy as np
import random
import math

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

    def random_new_path(self):
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
            
            self.random_new_path()
            actualRoute = self.calculate_path()

            if actualRoute < bestRoute:
                bestRoute = actualRoute
                bestSequence = []
                bestSequence = self.sequence

        print("Best sequence: " + str(bestSequence))
        print("Best Route: " + str(bestRoute))

        return bestRoute

class SimulatedAnnealing:
    def __init__(self, start_x, start_t, end_t, lam):
        self.start_x = start_x
        self.current_x = start_x
        self.new_x = start_x
        self.best_x = start_x

        self.start_t = start_t
        self.current_t = start_t
        self.end_t = end_t
        self.lam = lam

    def run(self):
        while self.current_t > self.end_t:
            self.new_x = self.current_x
            self.new_x.random_new_path()
            if self.best_x.calculate_path() > self.current_x.calculate_path():
                self.best_x = self.current_x
            if self.new_x.calculate_path() <= self.current_x.calculate_path():
                self.current_x = self.new_x
            else:
                delta = self.new_x.calculate_path() - self.current_x.calculate_path()
                p = math.exp(-delta/self.current_t)
                z = random.uniform(0,1)
                if z < p:
                    self.current_x = self.new_x
            self.current_t *= self.lam



