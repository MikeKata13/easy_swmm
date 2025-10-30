from easy_swmm.core.sections import Core_Section
from dataclasses import dataclass, field


@dataclass
class Model:
    content: list
    section_names: list = field(default_factory=list)
    sections: dict[str, Core_Section] = field(default_factory=dict)

    def __getitem__(self, key: str) -> Core_Section:
        return self.sections[key.upper()]

    def __getattr__(self, key: str) -> Core_Section:
        key = key.upper()
        if key in self.sections:
            return self.sections[key]
        raise AttributeError(f"No section named '{key}'")

    def __repr__(self):
        return f"<Model with sections: {', '.join(self.section_names)}>"
