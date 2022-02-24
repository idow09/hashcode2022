from yop.objects import ProblemInput, ProblemOutput


class Solver:
    def __init__(self):
        pass

    @staticmethod
    def solve(input_problem: ProblemInput) -> ProblemOutput:

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