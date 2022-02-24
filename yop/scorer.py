from yop.objects import ProblemInput, ProblemOutput, Project, Person


class Scorer:
    def update_skills(self, proj, assignees):
        pass

    def score(self, problem_input: ProblemInput, problem_output: ProblemOutput):
        result = 0
        for proj, assign in problem_output.project_name2day_and_persons.items():
            print("starting project {0} at day {1} for score {2}".format(proj.name, assign[0], proj.score))
            result += proj.score
            self.update_skills(proj, assign[1])

        print("total result is: {0}".format(result))
