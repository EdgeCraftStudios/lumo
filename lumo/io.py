from lumo.types import File
from lumo.parser import Parser

def load_file(filepath: str) -> File:
    parser = Parser()
    return parser.parse_file(filepath)

def save_file(file: File, filepath: str, append: bool = False) -> None:
    mode = 'a' if append else 'w'
    with open(filepath, mode, encoding='utf-8') as f:
        for i, section in enumerate(file.sections):
            f.write(f'[{section.name}]\n')
            for entry in section.entries:
                if entry.key is not None:
                    f.write(f'{entry.key}: {entry.value}\n')
                else:
                    f.write(f'{entry.value}\n')
            if i != len(file.sections) - 1:
                f.write('\n')