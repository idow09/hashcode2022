from collections import defaultdict
from typing import List, Dict

from yop.objects import ProblemInput, ProblemOutput, Person


def find_candidates(role, skill2persons):
    return skill2persons.values()


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
        return ProblemOutput({})
    @staticmethod
    def attach_persons_to_project(persons, project):
        output_persons = []
        # diffs_persons = {}

        # for role in project.roles:
            # for person in persons:
                # diff = diff_person_level_to_role_level(person, role)

        return output_persons

    @staticmethod
    def diff_person_level_to_role_level(person, role):
        for per_skill in person.Skills:
            if per_skill.name == role.name:
                return per_skill.level - role.level
        return -10
