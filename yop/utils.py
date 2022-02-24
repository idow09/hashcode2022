from yop.objects import Project


def get_project_value(proj: Project):
    result = 0
    roles_total_size = 0
    for i in proj.roles:
        roles_total_size += i.level
    return ((proj.score * 1000) / (roles_total_size * proj.duration)) - proj.best_before
