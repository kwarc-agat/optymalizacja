import os
from TravellingSalesmanProblem import *
from SimulatedAnnealing import *

dir_path = os.path.dirname(os.path.realpath(__file__))


def main():
    problem_file_path = os.path.join(dir_path, "problem_matrix.csv")
    problem = TravellingSalesmanProblem(problem_file_path)
    problem.show_params()
    problem.calculate_path()
    #problem.optimalize()
    T0 = 1000
    Tk = 0.1
    lam = 0.9995
    sa_solution = simulated_annealing(problem.sequence, T0, Tk, lam)
    print("Best path: "+str(sa_solution))



if __name__ == "__main__":
    main()
