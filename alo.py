import random
import copy
import logging

from evaluator import Evaluator


logging.basicConfig(level=logging.INFO)


def update_job_list(initial_solution_arg):
    local_job_dict = copy.deepcopy(initial_solution_arg)
    local_job_dict_copy = copy.deepcopy(initial_solution_arg)
    dict_list = list(local_job_dict.items())
    dict_list_copy = list(local_job_dict_copy.items())
    i = 0
    while i < len(dict_list):
        k = i
        if i != 0:
            j = i - 1
            while k < len(dict_list):
                # dict_list[k][1][0] = dict_list[j][1][1] + dict_list[k][1][0]
                dict_list[k][1][1] = dict_list[j][1][1] + dict_list_copy[k][1][1]
                k += 1
        i += 1

    return dict(dict_list)


def roulette_wheel(size):
    rand = random.random()
    index = 0
    val = 0.5
    while (not (rand > val)) and index < size - 1:
        index += 1
        val = val / 2

    return index


def shuffle_dict(dict_arg):
    dict_list = list(dict_arg.items())
    random.shuffle(dict_list)
    return dict(dict_list)


class ALO:
    job_dict = {}
    evaluator = Evaluator()

    def __init__(self, job_dict_arg, evaluator_arg):
        self.job_dict = job_dict_arg
        self.evaluator = evaluator_arg

    def create_initial_solution_randomly(self):
        initial_solution = copy.deepcopy(self.job_dict)
        shuffled_initial_solution = shuffle_dict(initial_solution)
        shuffled_initial_solution_updated = update_job_list(shuffled_initial_solution)
        return shuffled_initial_solution_updated

    def solve(self, initial_solution_arg, max_iter):
        elite_income = self.evaluator.evaluate(initial_solution_arg)
        logging.info("Initial Solution Income = {}".format(elite_income))
        best_job_order = copy.deepcopy(initial_solution_arg)
        logging.info("Initial Solution Order = " + ', '.join(str(key) for key, value in best_job_order.items()))

        ant_solution = copy.deepcopy(self.job_dict)

        i = 1
        while i <= max_iter:
            integer_list = self.roulette_wheel_selection()
            wheeled_list = []
            local_job_dict = copy.deepcopy(self.job_dict)
            local_job_list = list(local_job_dict.items())
            for integer in integer_list:
                wheeled_list.append(local_job_list[integer])

            ant_lion_solution = dict(wheeled_list)
            ant_lion_solution = update_job_list(ant_lion_solution)

            local_ant_solution = copy.deepcopy(ant_solution)
            shuffled_ant_solution = shuffle_dict(local_ant_solution)
            shuffled_ant_solution = update_job_list(shuffled_ant_solution)

            if self.evaluator.evaluate(shuffled_ant_solution) > self.evaluator.evaluate(ant_lion_solution):
                ant_lion_solution = copy.deepcopy(shuffled_ant_solution)

            if self.evaluator.evaluate(ant_lion_solution) > elite_income:
                best_job_order = copy.deepcopy(ant_lion_solution)
                elite_income = self.evaluator.evaluate(ant_lion_solution)
                logging.info("Elite Income Has Changed = " + str(elite_income) + ", iteration = " + str(i))
                logging.info("Best Job Order Has Changed = " + ', '.join(str(key) for key, value in best_job_order.items()) + ", iteration = " + str(i))

            i += 1

    def roulette_wheel_selection(self):
        integer_list = []
        while len(integer_list) != len(list(self.job_dict)):
            index = roulette_wheel(len(list(self.job_dict)))
            if index not in integer_list:
                integer_list.append(index)

        return integer_list

    

