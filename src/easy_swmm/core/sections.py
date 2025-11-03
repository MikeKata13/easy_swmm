from enum import Enum

class Section_Type(Enum):
    JUNCTIONS = "JUNCTIONS"
    CONDUITS = "CONDUITS"
    STORAGE = "STORAGE"
    PUMPS = "PUMPS"

    @classmethod
    def custom(cls, name: str):
        """Create a custom Section_Type at runtime."""
        temp = object.__new__(cls)
        temp._value_ = name.upper()
        return temp


class Core_Section:
    def __init__(self, section_type: Section_Type | str, content: list | None = None):
        if isinstance(section_type, Section_Type):
            self.section_type = section_type
        elif isinstance(section_type, str):
            self.section_type = Section_Type.custom(section_type)
        else:
            raise TypeError("section_type must be Section_Type or str")

        self.content = content or []

    def __repr__(self):
        return f"<Core_Section {self.section_type.value} ({len(self.content)} lines)>"

    def parse(self):
        """Optionally overridden by subclasses."""
        pass


class JunctionsSection(Core_Section):
    def parse(self):
        print(f"Parsing {len(self.content)} junctions...")


class ConduitsSection(Core_Section):
    def parse(self):
        print(f"Parsing {len(self.content)} conduits...")
