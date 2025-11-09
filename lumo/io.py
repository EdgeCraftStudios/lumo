from .types import File
from .parser import Parser

def load_file(filepath: str) -> File:
    """Load a configuration file and return a File object.

    Args:
        filepath: Path to the configuration file.

    Returns:
        File object parsed from the file.
    """
    parser = Parser()
    return parser.parse_file(filepath)


def save_file(file: File, filepath: str, append: bool = False) -> None:
    """Save a File object to disk.

    Args:
        file: The File object to save.
        filepath: Path to save the file.
        append: If True, append to existing file; otherwise overwrite.
    """
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