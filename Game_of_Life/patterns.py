# patterns.py and patterns.toml handle the game’s patterns
# game's seed

from dataclasses import dataclass
from pathlib import Path

@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]

    # Load the Life Patterns From TOML
    @classmethod
    def from_toml(cls, name, toml_data):
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]},
        )

'''
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Automatically generates __init__, __repr__, and other methods
point = Point(1, 2)
print(point)  # Output: Point(x=1, y=2)
'''

try:
    import tomllib
except ImportError:
    import tomli as tomllib

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"

# function retrieves a single pattern from the TOML file using the pattern’s name.
def get_pattern(name, filename=PATTERNS_FILE):
    # load the content of patterns.toml using the TOML library of choice. 
    # The .loads() method returns a dictionary.
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name, toml_data=data[name])

# function retrieved all patterns from the TOML files
def get_all_patterns(filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return [
        Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
    ]