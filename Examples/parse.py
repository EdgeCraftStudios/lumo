import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lumo

def main():
    raw_lines = [
        "[Database]",
        "Host: localhost",
        "Port: 5432",
        "UseSSL: true",
        "",
        "[Modules]",
        "auth",
        "billing",
        "notifications",
        "",
        "[Logging]",
        "Level: INFO",
        "Verbose",
        "Debug: false",
        "RotateLogs",
    ]

    parser = lumo.Parser()
    file = parser.parse(raw_lines)

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