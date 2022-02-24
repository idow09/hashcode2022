from collections import defaultdict
from copy import deepcopy
from typing import List, Dict, Tuple
from yop.utils import *

from yop.objects import ProblemInput, ProblemOutput, Person, Skill


def calc_fitness(person: Person, role: Skill):
    diff = person.skills[role.name].level - role.level
    return diff


def find_candidates(role: Skill, skill2persons, name2busy, t):
    persons: List[Person] = skill2persons[role.name]
    fitness = [calc_fitness(person, role) for person in persons]
    fitness_and_persons = [(f, p) for f, p in zip(fitness, persons) if f >= 0]
    persons_ = [p for _, p in sorted(fitness_and_persons, key=lambda f_and_p: f_and_p[0])]
    persons_ = [person for person in persons_ if name2busy[person.name] is None]
    return persons_


def get_skill2persons(input_problem: ProblemInput):
    skill2persons: Dict[str, List[Person]] = defaultdict(list)
    for person in input_problem.persons:
        for skill in person.skills:
            skill2persons[skill].append(person)
    return skill2persons


class Solver:
    def __init__(self, problem_input: ProblemInput):
        self.problem_input = problem_input
        self.skill2persons = get_skill2persons(self.problem_input)
        self.name2busy = {person.name: None for person in problem_input.persons}
        self.alloc = []
        self.t = 0

    def solve(self) -> ProblemOutput:
        projects = list(self.problem_input.projects.values())
        skill2persons = deepcopy(self.skill2persons)
        project_name2day_and_persons = {}
        for t in range(int(10e4)):
            project_name2day_and_persons_ = self.get_alloc(t, projects, skill2persons)
            project_name2day_and_persons.update(**project_name2day_and_persons_)
            for p in self.name2busy.keys():
                if self.name2busy[p] == 1:
                    self.name2busy[p] = None
                if self.name2busy[p] is not None:
                    self.name2busy[p] -= 1

        return ProblemOutput(project_name2day_and_persons)

    def get_alloc(self, t, projects, skill2persons):
        projects = order_projects_by_priority(projects)
        project_name2day_and_persons = {}
        for project in projects:
            persons = self.attach_persons_to_project(project, skill2persons, self.t)
            if persons is not None:
                project_name2day_and_persons[project.name] = (t, persons)
        return project_name2day_and_persons

    def attach_persons_to_project(self, project, skill2persons, t):
        project_persons = []

        for role in project.roles:
            candidates = find_candidates(role, skill2persons, self.name2busy, t)
            if len(candidates) == 0:
                return None
            candidate = candidates[0]
            project_persons.append(candidate)
            self.name2busy[candidate.name] = project.duration

        if len(project_persons) < len(project.roles):
            return None
        return project_persons
