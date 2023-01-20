from alo import ALO
from evaluator import Evaluator

job_dict = {
        "A": [14, 24, 36, 25, 500],
        "B": [12, 18, 40, 40, 700],
        "C": [4, 15, 75, 30, 60],
        "D": [12, 11, 50, 40, 900],
        "E": [0, 13, 90, 30, 400],
        "F": [8, 17, 60, 40, 800]
}

evaluator = Evaluator()
alo = ALO(job_dict, evaluator)
initial_solution = alo.create_initial_solution_randomly()

max_iter = 1000
alo.solve(initial_solution, max_iter)
