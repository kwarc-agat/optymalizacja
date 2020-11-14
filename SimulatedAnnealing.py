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

def calculate_path(sequence):
        prev_elem_index = sequence[0]
        total_distance = 0
        for elem_index in sequence:
            distance = MATRIX[prev_elem_index][elem_index]
            prev_elem_index = elem_index
            total_distance += distance

        return total_distance

def random_new_path(sequence):
        a = random.randrange(1, len(sequence)-1, 1)
        b = random.randrange(1, len(sequence)-1, 1)

        while a==b:
            b = random.randrange(1, len(sequence)-1, 1)

        print("a: "+str(a)+"\tb: "+str(b))
        if a < b:
            temp = sequence[a]
            for i in range(a, b):
                sequence[i] = sequence[i+1]
            sequence[b] = temp

        if a > b:
            temp = sequence[a]
            for i in range(a, b, -1):
                sequence[i] = sequence[i-1]
            sequence[b] = temp
        return sequence


def simulated_annealing(x0, T0, Tk, lam):
    x_current = x0
    x_best = x0
    T = T0

    while T > Tk:
            print("-------------NEW ITERATION-----------------")
            x_new = random_new_path(x0.copy())
            x_new_length = calculate_path(x_new)
            print("Best solution:    "+str(x_best))
            print("Current solution:  "+str(x_current))
            print("New solution:     "+str(x_new)+" -> "+str(x_new_length))
           
            if calculate_path(x_best) > calculate_path(x_new):
                x_best = x_new
            
            if calculate_path(x_new) <= calculate_path(x_current):
                x_current = x_new
            else:
                delta = calculate_path(x_new) - calculate_path(x_current)
                p = math.exp(-delta/T)
                z = random.random()
                if z < p:
                    x_current = x_new

            T *= lam

    return calculate_path(x_best)

_, MATRIX, _ = read_problem_from_file("problem_matrix.csv")
print("Whats up: "+ str(calculate_path([0, 4, 2, 1, 3, 5, 6, 7, 8, 0])))