import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lumo

def main():
    file = lumo.load_file("output.lumo")

    db_section = file.get_section("Database")
    if db_section.get("Port") is None:
        db_section.set("Host", "localhost")
        db_section.set("Port", 5432)
        db_section.set("UseSSL", True)
    print("Original Database Port:", db_section.get("Port"))

    db_section.set("Port", 3306)
    db_section.set("Username", "admin")

    modules_section = file.get_section("Modules")
    print("Modules before append:", modules_section.get_values())
    modules_section.add_list_item("email")

    logging_section = file.get_section("Logging")
    logging_section.add_list_item("ExtraDebug")

    print("Modules after append:", modules_section.get_values())

    lumo.save_file(file, "output.lumo")
    print("Saved updated config to output.lumo")

if __name__ == "__main__":
    main()