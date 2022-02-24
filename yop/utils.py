from yop.objects import Project
from typing import List


def get_project_value(proj: Project, start_day: int):
    roles_total_size = 0
    for i in proj.roles.values():
        roles_total_size += i.level
    diff_due_to_best_before = 0
    if proj.best_before > (start_day + proj.duration):
        diff_due_to_best_before = 0
    else:
        diff_due_to_best_before = (start_day + proj.duration) - proj.best_before
    proj_score = 0
    if proj.score > diff_due_to_best_before:
        proj_score = proj.score - diff_due_to_best_before

    return ((proj_score * 1000) / (roles_total_size * proj.duration))


def order_projects_by_priority(project_list: List[Project]):
    result = []
    for proj in project_list:
        result.append((get_project_value(proj, 0), proj))
    return [proj for v, proj in sorted(result, key=lambda v_and_p: v_and_p[0])]
