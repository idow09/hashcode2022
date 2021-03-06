from collections import OrderedDict
from typing import Optional, TextIO, List

from yop.objects import ProblemInput, ProblemOutput, Skill, Person, Project


def load(file, mock=False) -> ProblemInput:
    if mock:
        return _load_mock()
    lines: List[str] = file.readlines()
    C, P = lines.pop(0).split()
    C, P = int(C), int(P)
    persons = []
    for _ in range(C):
        person_name, N = lines.pop(0).split()
        N = int(N)
        skill_name2skills = OrderedDict()
        for _ in range(N):
            skill_name, skill_level = lines.pop(0).split()
            skill_level = int(skill_level)
            skill_name2skills[skill_name] = Skill(skill_name, skill_level)
        person = Person(person_name, skill_name2skills)
        persons.append(person)
    projects = OrderedDict()
    for _ in range(P):
        project_name, D, S, B, R = lines.pop(0).split()
        D, S, B, R = int(D), int(S), int(B), int(R)
        role_name2roles = []
        for _ in range(R):
            skill_name, skill_level = lines.pop(0).split()
            skill_level = int(skill_level)
            role_name2roles.append(Skill(skill_name, skill_level))
        project = Project(project_name, D, S, B, role_name2roles)
        projects[project_name] = project

    return ProblemInput(persons, projects)


def _load_mock():
    raise NotImplementedError()


def dump(output: ProblemOutput, file=Optional[TextIO]):
    def write(string):
        if file:
            file.write(string)
        else:
            pass
            # print(string, end='')

    write(f'{len(output.project_name2day_and_persons)}\n')
    for project_name, day_and_persons in output.project_name2day_and_persons.items():
        unused_day, persons = day_and_persons
        write(f'{project_name}\n')
        person_names = [person.name for person in persons]
        write(f'{" ".join(person_names)}\n')
