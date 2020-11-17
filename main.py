import os
from TravellingSalesmanProblem import *
from SimulatedAnnealing import *

dir_path = os.path.dirname(os.path.realpath(__file__))


def main():
    problem_file_path = os.path.join(dir_path, "problem_matrix.csv")
    problem = TravellingSalesmanProblem(problem_file_path)
    problem.show_params()
    problem.calculate_path()
    best_seq_rs, best_len_rs = problem.optimalize()
    print("Random Search results:\n"+str(best_seq_rs)+" = "+str(best_len_rs))
    
    T0 = 1000
    Tk = 0.1
    lam = 0.9995
    best_seq_sa, best_len_sa = simulated_annealing(problem.sequence_init, T0, Tk, lam)
    print("Simulated annealing results:\n"+str(best_seq_sa)+" = "+str(best_len_sa))


if __name__ == "__main__":
    main()
