import numpy as np
import random
import math
import os


#def read_problem_from_file(file_path):
#    line_counter = 0
#    matrix_size = 0
#    matrix = []
#    with open(file_path, "r") as file:
#        for line in file:
#            if line_counter == 0:
#                matrix_size = int(line)
#                line_counter += 1
#            elif line_counter <= matrix_size:
#                row = line.strip().split(' ')
#                row = [int(elem) for elem in row]
#                matrix.append(row)
#                line_counter += 1
#            else:
#                sequence = line.strip().split(' ')
#                sequence = [int(elem) for elem in sequence]

#    return matrix_size, np.array(matrix), sequence

def read_problem_from_file(file_path):  # to jest ta nowa funkcja czytająca plik. 
                                        # dodaje pierwszy wiersz i kolumnę zerową do odczytanej macierzy
    line_counter = 0
    machines = -1
    tasks = -1
    matrix = []
    with open(file_path, "r") as file:
        for line in file:
            if line_counter == 0:
                row = line.strip().split(' ')
                tasks = int(row[0])
                machines = int(row[1])
                first_row = np.zeros((1, machines))
                matrix.append(first_row)
                line_counter += 1
            else:
                row = line.strip().split(' ')
                row = [int(elem) for elem in row]
                row = np.insert(row, 0, 0, axis=0)
                matrix.append(row)
                line_counter += 1
    
    return machines, tasks, np.array(matrix)


# def calculate_path(sequence):
#         prev_elem_index = sequence[0]
#         total_distance = 0
#         for elem_index in sequence:
#             distance = MATRIX[prev_elem_index][elem_index]
#             prev_elem_index = elem_index
#             total_distance += distance
#
#         return total_distance

#def calculate_path(sequence):
#    prev_elem_index = sequence[0]
#    total_distance_1 = 0
#    total_distance_2 = 0
#    count_zeros = 1

#    for elem_index in sequence:
#        if count_zeros == 1 or count_zeros == 2:
#            distance = MATRIX[prev_elem_index][elem_index]
#            prev_elem_index = elem_index
#            total_distance_1 += distance
#            if elem_index == 0:
#                count_zeros += 1
#        if count_zeros == 3:
#            distance = MATRIX[prev_elem_index][elem_index]
#            prev_elem_index = elem_index
#            total_distance_2 += distance

#    if total_distance_1 >= total_distance_2:
#        total_distance = total_distance_1
#    else:
#        total_distance = total_distance_2

#    return total_distance

def calculate_schedule(pi): # to jest ta nowa funkcja, chyba zgodnie z tym co narysował
    n = TASKS
    m = MACHINES
    p = TIME_MATRIX

    pi = np.insert(pi, 0, 0, axis=0)    # bo pi(0)=0
    C = np.zeros([n+1, m+1], dtype=int)
    
    for j in range(1, n+1):
        for k in range(1, m+1):
            C[j][k] = max(C[j][k-1], C[j-1][k])+p[pi[j]][k]

    C_max = C[n][m]
    return C_max


def random_new_path(sequence):
    #a = random.randrange(1, len(sequence) - 1, 1)
    #b = random.randrange(1, len(sequence) - 1, 1)
    a = random.randrange(0, len(sequence), 1)   # tu zmiana żeby brało wszystkie liczby w sequence
    b = random.randrange(0, len(sequence), 1)   # poprzednio na pierwszym i ostatnim miejscu musiało zostać 0

    while a == b:
        b = random.randrange(1, len(sequence) - 1, 1)

    #print("a: " + str(a) + "\tb: " + str(b))
    if a < b:
        temp = sequence[a]
        for i in range(a, b):
            sequence[i] = sequence[i + 1]
        sequence[b] = temp

    if a > b:
        temp = sequence[a]
        for i in range(a, b, -1):
            sequence[i] = sequence[i - 1]
        sequence[b] = temp
    return sequence


#def simulated_annealing(x0, T0, Tk, lam):
#    x_current = x0
#    x_best = x0
#    T = T0

#    while T > Tk:
#        #print("-------------NEW ITERATION-----------------")
#        x_new = random_new_path(x_current.copy())
#        x_new_length = calculate_path(x_new)
#        #print("Best solution:    " + str(x_best))
#        #print("Current solution:  " + str(x_current))
#        #print("New solution:     " + str(x_new) + " -> " + str(x_new_length))

#        if calculate_path(x_best) > calculate_path(x_new):
#            x_best = x_new

#        if calculate_path(x_new) <= calculate_path(x_current):
#            x_current = x_new
#        else:
#            delta = calculate_path(x_new) - calculate_path(x_current)
#            p = math.exp(-delta / T)
#            z = random.random()
#            if z < p:
#                x_current = x_new

#        T *= lam

#    return calculate_path(x_best)

def simulated_annealing(T0, Tk, lam):   # to co wyżej, tylko zamiast calculate_path jest calculate_schedule
                                        # i x0 nie jest agrumentem funkcji
    x0 = list(range(1,TASKS+1))
    x_current = x0
    x_best = x0
    T = T0

    while T > Tk:
        #print("-------------NEW ITERATION-----------------")
        x_new = random_new_path(x_current.copy())
        x_new_length = calculate_schedule(x_new)
        #print("Best solution:    " + str(x_best))
        #print("Current solution:  " + str(x_current))
        #print("New solution:     " + str(x_new) + " -> " + str(x_new_length))

        if calculate_schedule(x_best) > calculate_schedule(x_new):
            x_best = x_new
            #print("New best: "+str(x_best))
            print("Best time: "+str(calculate_schedule(x_best)))

        if calculate_schedule(x_new) <= calculate_schedule(x_current):
            x_current = x_new
        else:
            delta = calculate_schedule(x_new) - calculate_schedule(x_current)
            p = math.exp(-delta / T)
            z = random.random()
            if z < p:
                x_current = x_new

        T *= lam

    return calculate_schedule(x_best)


#_, MATRIX, _ = read_problem_from_file("t.csv")
#print("Whats up: " + str(calculate_path([0, 1, 2, 3, 4, 0, 5, 6, 7, 8, 0])))
dir_path = os.path.dirname(os.path.realpath(__file__))
problem_file_path = os.path.join(dir_path, "zad3-dane\\NEH9.DAT")
MACHINES, TASKS, TIME_MATRIX = read_problem_from_file(problem_file_path)
