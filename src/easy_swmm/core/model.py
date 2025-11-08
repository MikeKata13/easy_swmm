from easy_swmm.core.sections import Core_Section
from pathlib import Path

class Model:
    def __init__(self, file: Path | str):
        self.file = Path(file)
        self.content = []
        self.section_names = []
        self.sections: dict[str, Core_Section] = {}

    def __getitem__(self, key: str) -> 'Core_Section':
        return self.sections[key.upper()]

    def __getattr__(self, key: str) -> 'Core_Section':
        key = key.upper()
        if key in self.sections:
            return self.sections[key]
        raise AttributeError(f"No section named '{key}'")

    def __repr__(self):
        return f"<Model with sections: {', '.join(self.section_names)}>"

