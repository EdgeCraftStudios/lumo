from typing import Optional, Union
from .types import Entry, Section, File

class Parser:
    """Parses configuration-style files into a File object.

    Methods:
        parse(lines): Parse a list of strings into a File.
        parse_file(filepath): Parse a file from disk into a File.
    """

    def __init__(self):
        self.file = File()

    def _parse_value(self, value: str) -> Union[str, int, float, bool]:
        """Internal helper: parse a string into int, float, bool, or keep as str."""
        value = value.strip()
        low = value.lower()
        if low == 'true':
            return True
        if low == 'false':
            return False
        try:
            if '.' not in value:
                return int(value)
            return float(value)
        except ValueError:
            return value

    def parse(self, lines: list[str]) -> File:
        """Parse a list of strings into a File object.

        Args:
            lines: Lines of a configuration file.

        Returns:
            File object containing sections and entries.
        """
        current_section: Optional[Section] = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith('[') and line.endswith(']'):
                section_name = line[1:-1].strip()
                current_section = Section(section_name)
                self.file.add_section(current_section)
                continue
            if current_section is None:
                raise ValueError(f"Line outside any section: {line}")
            if ':' in line:
                key, val = line.split(':', 1)
                key = key.strip()
                val = val.strip()
                parsed_val = self._parse_value(val)
                entry = Entry(key, parsed_val)
            else:
                parsed_val = self._parse_value(line)
                entry = Entry(None, parsed_val)
            current_section.add_entry(entry)
        return self.file

    def parse_file(self, filepath: str) -> File:
        """Parse a file from disk into a File object.

        Args:
            filepath: Path to the configuration file.

        Returns:
            File object containing sections and entries.
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return self.parse(lines)