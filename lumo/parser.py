from typing import Optional, Union
from lumo.types import Entry, Section, File

class Parser:
    def __init__(self):
        self.file = File()

    def _parse_value(self, value: str) -> Union[str, int, float, bool]:
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
        current_section: Optional[Section] = None
        for line in lines:
            line = line.strip()
            if line == '':
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
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return self.parse(lines)