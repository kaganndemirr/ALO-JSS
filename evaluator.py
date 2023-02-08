import copy


class Evaluator:
    total_income = 0

    def evaluate(self, job_dict_arg):
        self.total_income = 0
        local_job_dict = copy.deepcopy(job_dict_arg)
        for job_name, v in local_job_dict.items():
            elapsed_time = v[0]
            process_time = v[1]
            deadline = v[2]
            # tardiness = min(0, deadline - (elapsed_time + process_time))
            tardiness = min(0, deadline - process_time)
            self.total_income += v[4] + min(0, tardiness * v[3])

        return self.total_income