from collections import defaultdict
from typing import List, Dict
from yop.utils import *

from yop.objects import ProblemInput, ProblemOutput, Person, Skill


def calc_fitness(person: Person, role: Skill):
    diff = person.skills[role.name].level - role.level
    return diff


def find_candidates(role: Skill, skill2persons, name2availability):
    persons: List[Person] = skill2persons[role.name]
    fitness = [calc_fitness(person, role) for person in persons]
    fitness_and_persons = [(f, p) for f, p in zip(fitness, persons) if f >= 0]
    persons_ = [p for _, p in sorted(fitness_and_persons, key=lambda f_and_p: f_and_p[0])]
    persons_ = [person for person in persons_ if name2availability[person.name]]
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
        self.name2availability = {person.name: True for person in problem_input.persons}

    def solve(self) -> ProblemOutput:
        projects = order_projects_by_priority(list(self.problem_input.projects.values()))

        project_name2day_and_persons = {}
        for project in projects:
            persons = self.attach_persons_to_project(project)
            if persons is not None:
                project_name2day_and_persons[project.name] = (0, persons)
        return ProblemOutput(project_name2day_and_persons)

    def attach_persons_to_project(self, project):
        project_persons = []

        for role in project.roles.values():
            candidates = find_candidates(role, self.skill2persons, self.name2availability)
            if len(candidates) == 0:
                return None
            candidate = candidates[0]
            project_persons.append(candidate)
            self.name2availability[candidate.name] = False

        if len(project_persons) < len(project.roles):
            return None
        return project_persons
