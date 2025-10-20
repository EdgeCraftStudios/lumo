import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lumo

def main():
    file = lumo.load_file("output.lumo")

    for section in file.sections:
        print(f"[{section.name}]")
        for entry in section.entries:
            if entry.key:
                print(f"{entry.key}: {entry.value}")
            else:
                print(entry.value)
        print()

if __name__ == "__main__":
    main()
