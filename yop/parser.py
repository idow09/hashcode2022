from typing import Optional, TextIO, List

from yop.objects import ProblemInput, ProblemOutput


def load(file, mock=False) -> ProblemInput:
    if mock:
        return _load_mock()
    lines: List[str] = file.readlines()
    C = int(lines.pop(0))
    P = int(lines.pop(0))
    for i in range(C):
        line = lines.pop(0)
        name, N = line.split()
        N = int(N)
        for j in range(N):
            pass

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
