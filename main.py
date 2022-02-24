import os
import zipfile
from pathlib import Path

from yop.parser import dump, load
from yop.scorer import Scorer
from yop.solver import Solver

DATA_ROOT = Path('.')
DEBUG_MODE = False
# INPUT_FILES = ['a_an_example.in.txt']
INPUT_FILES = None


def read_input(path):
    with path.open() as f_in:
        problem_input = load(f_in, mock=DEBUG_MODE)
    return problem_input


def write_output(data_out_path, problem_output):
    with open(data_out_path, 'w') as f_out:
        dump(problem_output, f_out if not DEBUG_MODE else None)


def get_input_paths():
    if INPUT_FILES is not None:
        input_paths = [(DATA_ROOT / 'data' / f) for f in INPUT_FILES]
    else:
        input_paths = [p for p in (DATA_ROOT / 'data').iterdir() if p.is_file()]
    return input_paths


def generate_zip():
    def zipdir(path, ziph):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".py"):
                    ziph.write(os.path.join(root, file),
                               os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

    zipf = zipfile.ZipFile('submission.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('.', zipf)
    zipf.close()


def main():
    (DATA_ROOT / 'output').mkdir(parents=True, exist_ok=True)
    input_paths = get_input_paths()

    for path in input_paths:
        problem_input = read_input(path)

        parameters = {}
        problem_output = Solver(**parameters).solve(problem_input)
        print(f'Score for {path.stem} is: {Scorer().score(problem_input, problem_output)}')

        data_out_path = DATA_ROOT / 'output' / f'{path.stem}_out.txt'
        write_output(data_out_path, problem_output)


if __name__ == '__main__':
    main()
    generate_zip()
