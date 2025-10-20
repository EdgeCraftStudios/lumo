import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lumo

def main():
    file = lumo.File()

    logging_section = lumo.Section("Logging")
    logging_section.add_key_value("Level", "INFO")
    logging_section.add_list_item("Verbose")
    logging_section.add_key_value("Debug", False)
    logging_section.add_list_item("RotateLogs")
    file.add_section(logging_section)

    modules_section = lumo.Section("Modules")
    modules_section.add_list_item("auth")
    modules_section.add_list_item("billing")
    modules_section.add_list_item("notifications")
    file.add_section(modules_section)

    lumo.save_file(file, "output.lumo")
    print("Saved to output.lumo")

if __name__ == "__main__":
    main()