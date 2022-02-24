from dataclasses import dataclass
from typing import List, Dict, Tuple, OrderedDict


@dataclass
class Skill:
    name: str
    level: int


@dataclass
class Project:
    name: str
    duration: int
    score: int
    best_before: int
    roles: OrderedDict[str, Skill]


@dataclass
class Person:
    name: str
    skills: OrderedDict[str, Skill]


@dataclass
class ProblemInput:
    persons: List[Person]
    projects: List[Project]


@dataclass
class ProblemOutput:
    project_name2day_and_persons: Dict[Project, Tuple[int, List[Person]]]
