# lumo — Simple Config Format

![lumo logo](logo/lumo_256px.png)

![License](https://img.shields.io/github/license/EdgeCraftStudios/lumo?style=flat&color=%2320B2AA)
![Release](https://img.shields.io/github/v/release/EdgeCraftStudios/lumo?sort=semver&display_name=release&style=flat&color=%23CD5C5C)
![Downloads)](https://img.shields.io/github/downloads/EdgeCraftStudios/lumo/latest/total?sort=semver&style=flat&label=Downloads&color=%23F44336)

lumo is a lightweight configuration file format inspired by INI files, designed to be easy to read and write. It supports:

- Named sections using `[SectionName]` syntax  
- Key-value pairs inside sections (`Key: Value`)  
- List-style values without keys inside sections (just `Value` lines)  
- Typed values: strings, integers, floats, booleans  
- Simple parsing, reading, writing, and modifying with Python  

The file extension used is `.lumo`.

## Examples

This repo includes several example scripts showing how to use lumo in Python:

- **memory.py**  
  Creates an in-memory lumo file with multiple sections containing both key-values and list items, then prints the config.

- **write.py**  
  Writes a lumo file called `output.lumo` with sections having mixed key-values and list items.

- **read.py**  
  Reads and prints the contents of an existing lumo file `output.lumo`.

- **parse.py**  
  Parses raw lumo-format lines from a list, demonstrating how the parser works with key-values and list values.

- **modify.py**  
  Loads an existing lumo file `output.lumo`, updates key-values and adds list items to sections, then saves the changes.

Run the examples in order to see how easy it is to create, read, parse, and modify `.lumo` configuration files.