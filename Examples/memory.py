import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lumo

def main():
    lumo_file = lumo.File()

    db_section = lumo.Section("Database")
    db_section.add_key_value("Host", "localhost")
    db_section.add_key_value("Port", 5432)
    db_section.add_key_value("UseSSL", True)
    lumo_file.add_section(db_section)

    modules_section = lumo.Section("Modules")
    modules_section.add_list_item("auth")
    modules_section.add_list_item("billing")
    modules_section.add_list_item("notifications")
    lumo_file.add_section(modules_section)

    logging_section = lumo.Section("Logging")
    logging_section.add_key_value("Level", "INFO")
    logging_section.add_list_item("Verbose")
    logging_section.add_key_value("Debug", False)
    logging_section.add_list_item("RotateLogs")
    lumo_file.add_section(logging_section)

    for section in lumo_file.sections:
        print(f"[{section.name}]")
        for entry in section.entries:
            if entry.key:
                print(f"{entry.key}: {entry.value}")
            else:
                print(entry.value)
        print()

if __name__ == "__main__":
    main()