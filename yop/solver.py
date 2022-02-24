from collections import defaultdict
from typing import List, Dict

from yop.objects import ProblemInput, ProblemOutput, Person, Skill


def calc_fitness(person: Person, role: Skill):
    diff = person.skills[role.name].level - role.level
    return diff


def find_candidates(role: Skill, skill2persons):
    persons: List[Person] = skill2persons[role.name]
    fitness = [calc_fitness(person, role) for person in persons]
    fitness_and_persons = [(f, p) for f, p in zip(fitness, persons) if f >= 0]
    fitness_and_persons = [p for _, p in sorted(fitness_and_persons)]
    return fitness_and_persons


def get_skill2persons(input_problem: ProblemInput):
    skill2persons: Dict[str, List[Person]] = defaultdict(list)
    for person in input_problem.persons:
        for skill in person.skills:
            skill2persons[skill].append(person)
    return skill2persons


class Solver:
    def __init__(self):
        pass

    @staticmethod
    def solve(input_problem: ProblemInput) -> ProblemOutput:
        skill2persons = get_skill2persons(input_problem)
        for project in input_problem.projects:
            for role in project.roles.values():
                candidates = find_candidates(role, skill2persons)
                print(candidates)
        return ProblemOutput({})

    @staticmethod
    def attach_persons_to_project(persons, project):
        output_persons = []
        #prioritized_persons 
        # diffs_persons = {}

        # for role in project.roles:
        # for person in persons:
        # diff = diff_person_level_to_role_level(person, role)

        return output_persons

    @staticmethod
    def diff_person_level_to_role_level(person, role):
        for per_skill in person.skills:
            if per_skill.name == role.name:
                return per_skill.level - role.level
        return -10
