from typing import Optional, Union

class Entry:
    """Represents a single entry in a section.

    An entry can either be a key-value pair or a list-style value (key is None).

    Attributes:
        key: Optional key of the entry; None for list-style entries.
        value: The stored value (str, int, float, or bool).
    """
    def __init__(self, key: Optional[str], value: Union[str, int, float, bool]):
        self.key = key
        self.value = value


class Section:
    """A named section containing entries.

    Sections can contain both key-value pairs and list-style items.

    Attributes:
        name: The name of the section.
        entries: List of `Entry` objects in this section.

    Methods:
        add_entry(entry): Add an Entry object to the section.
        add_key_value(key, value): Add a key-value pair entry.
        add_list_item(value): Add a list-style entry.
        get(key): Get the value for a key; returns None if not found.
        set(key, value): Set or add a key-value entry.
        get_values(): Return all list-style entry values.
    """

    def __init__(self, name: str):
        self.name = name
        self.entries: list[Entry] = []

    def add_entry(self, entry: Entry):
        """Add an Entry object to the section."""
        self.entries.append(entry)

    def add_key_value(self, key: str, value: Union[str, int, float, bool]):
        """Add a key-value entry to the section."""
        self.entries.append(Entry(key, value))

    def add_list_item(self, value: Union[str, int, float, bool]):
        """Add a list-style entry (without a key) to the section."""
        self.entries.append(Entry(None, value))

    def get(self, key: str) -> Union[str, int, float, bool, None]:
        """Return the value associated with a key, or None if not found."""
        for entry in self.entries:
            if entry.key == key:
                return entry.value
        return None

    def set(self, key: str, value: Union[str, int, float, bool]):
        """Set the value of a key; add the key if it does not exist."""
        for entry in self.entries:
            if entry.key == key:
                entry.value = value
                return
        self.add_key_value(key, value)

    def get_values(self) -> list[Union[str, int, float, bool]]:
        """Return all values of list-style entries (entries with no key)."""
        return [entry.value for entry in self.entries if entry.key is None]


class File:
    """Represents a configuration file containing multiple sections.

    Attributes:
        sections: List of Section objects.

    Methods:
        add_section(section): Add a Section to the file.
        get_section(name): Get a Section by name; creates it if it doesn't exist.
    """

    def __init__(self):
        self.sections: list[Section] = []

    def add_section(self, section: Section):
        """Add a Section to the file."""
        self.sections.append(section)

    def get_section(self, name: str) -> Section:
        """Get a Section by name; create and add it if it does not exist."""
        for section in self.sections:
            if section.name == name:
                return section
        section = Section(name)
        self.add_section(section)
        return section