import os
from algorithms import TravellingSalesManProblem

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    problem_file_path = os.path.join(dir_path, "problem_matrix.csv")
    problem = TravellingSalesManProblem(problem_file_path)
    problem.show_params()
    problem.calculate_path()

if __name__ == "__main__":
    main()

