from typing import Optional, TextIO

from yop.objects import ProblemInput, ProblemOutput


def load(file, mock=False) -> ProblemInput:
    if mock:
        return _load_mock()
    lines = file.readlines()
    return ProblemInput()


def _load_mock():
    raise NotImplementedError()


def dump(output: ProblemOutput, file=Optional[TextIO]):
    def write(string):
        if file:
            file.write(string)
        else:
            print(string, end='')

    write(f'')
    for each in output.something:
        write(f'{each}\n')
