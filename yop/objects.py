from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class ProblemInput:
    pass



@dataclass
class Project:
    pass


@dataclass
class Person:
    pass


@dataclass
class ProblemOutput:
    project_name2day_and_persons: Dict[Project, Tuple[int, List[Person]]]
