from typing import Optional, Union

class Entry:
    def __init__(self, key: Optional[str], value: Union[str, int, float, bool]):
        self.key = key
        self.value = value

class Section:
    def __init__(self, name: str):
        self.name = name
        self.entries: list[Entry] = []

    def add_entry(self, entry: Entry):
        self.entries.append(entry)

    def add_key_value(self, key: str, value: Union[str, int, float, bool]):
        self.entries.append(Entry(key, value))

    def add_list_item(self, value: Union[str, int, float, bool]):
        self.entries.append(Entry(None, value))

    def get(self, key: str) -> Union[str, int, float, bool, None]:
        for entry in self.entries:
            if entry.key == key:
                return entry.value
        return None

    def set(self, key: str, value: Union[str, int, float, bool]):
        for entry in self.entries:
            if entry.key == key:
                entry.value = value
                return
        self.add_key_value(key, value)

    def get_values(self) -> list[Union[str, int, float, bool]]:
        return [entry.value for entry in self.entries if entry.key is None]

class File:
    def __init__(self):
        self.sections: list[Section] = []

    def add_section(self, section: Section):
        self.sections.append(section)

    def get_section(self, name: str) -> Section:
        for section in self.sections:
            if section.name == name:
                return section
        section = Section(name)
        self.add_section(section)
        return section