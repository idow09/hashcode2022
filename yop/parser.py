from typing import Optional, TextIO, List

from yop.objects import ProblemInput, ProblemOutput, Skill, Person, Project


def load(file, mock=False) -> ProblemInput:
    if mock:
        return _load_mock()
    lines: List[str] = file.readlines()
    C = int(lines.pop(0))
    P = int(lines.pop(0))
    persons = []
    for _ in range(C):
        person_name, N = lines.pop(0).split()
        N = int(N)
        skills = []
        for _ in range(N):
            skill_name, skill_level = lines.pop(0).split()
            skill_level = int(skill_level)
            skills.append(Skill(skill_name, skill_level))
        person = Person(person_name, skills)
        persons.append(person)
    projects = []
    for _ in range(P):
        project_name, D, S, B, R = lines.pop(0).split()
        D, S, B, R = int(D), int(S), int(B), int(R)
        roles = []
        for _ in range(R):
            skill_name, skill_level = lines.pop(0).split()
            skill_level = int(skill_level)
            roles.append(Skill(skill_name, skill_level))
        project = Project(project_name, D, S, B, roles)
        projects.append(project)

    return ProblemInput(persons, projects)


def _load_mock():
    raise NotImplementedError()


def dump(output: ProblemOutput, file=Optional[TextIO]):
    def write(string):
        if file:
            file.write(string)
        else:
            print(string, end='')

    write(f'{len(output.project_name2day_and_persons)}\n')
    for project_name, day_and_persons in output.project_name2day_and_persons.items():
        day, persons = day_and_persons
        write(f'{project_name}\n')
        person_names = [person.name for person in persons]
        write(f'{" ".join(person_names)}\n')
