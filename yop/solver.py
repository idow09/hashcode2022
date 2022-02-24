from collections import defaultdict
from typing import List, Dict

from yop.objects import ProblemInput, ProblemOutput, Person, Skill


def calc_fitness(person: Person, role: Skill):
    diff = person.skills[role.name].level - role.level
    return diff


def find_candidates(role: Skill, skill2persons):
    persons: List[Person] = skill2persons[role.name]
    fitness = [calc_fitness(person, role) for person in persons]
    return [p for _, p in sorted(zip(fitness, persons))]


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
        return ProblemOutput({})

    @staticmethod
    def attach_persons_to_project(persons, project):
        output_persons = []
        candidates = find_candidates(role, skill2persons)
        
        for role in project.roles:
            output_persons.append(find_candidates(role, skill2persons)[0])
            
        return output_persons
