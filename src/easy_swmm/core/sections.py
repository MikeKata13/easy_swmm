from enum import Enum

class Section_Type(Enum):
    TITLE = "TITLE"
    OPTIONS = "OPTIONS"
    FILES = "FILES"
    EVAPORATION = "EVAPORATION"
    RAINGAGES = "RAINGAGES"
    SUBCATCHMENTS = "SUBCATCHMENTS"
    SUBAREAS = "SUBAREAS"
    INFILTRATION = "INFILTRATION"
    JUNCTIONS = "JUNCTIONS"
    OUTFALLS = "OUTFALLS"
    CONDUITS = "CONDUITS"
    XSECTIONS = "XSECTIONS"
    POLLUTANTS = "POLLUTANTS"
    LANDUSES = "LANDUSES"
    COVERAGES = "COVERAGES"
    LOADINGS = "LOADINGS"
    BUILDUP = "BUILDUP"
    WASHOFF = "WASHOFF"
    TIMESERIES = "TIMESERIES"
    REPORT = "REPORT"
    TAGS = "TAGS"
    MAP = "MAP"
    COORDINATES = "COORDINATES"
    VERTICES = "VERTICES"
    POLYGONS = "POLYGON"
    STORAGE = "STORAGE"
    DWF = "DWF"
    PUMPS = "PUMPS"
    SYMBOLS = "SYMBOLS"

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
        else:
            self.section_type = Section_Type.custom(section_type)

        self.content = content or []

    def __repr__(self):
        return f"<Core_Section {self.section_type.value} ({len(self.content)} lines)>"

    def parse(self):
        """Optionally overridden by subclasses."""
        pass

class Junctions(Core_Section):
    def __init__(self, section_type: Section_Type | str, content: list | None = None):
        if str(section_type).upper() != Section_Type.JUNCTIONS.value:
            raise ValueError("Junctions Section must have section_type 'JUNCTIONS'")
        super().__init__(Section_Type.JUNCTIONS, content)

    def parse(self):
        print(f"Parsing {len(self.content)} junctions...")


class Conduits(Core_Section):
    def __init__(self, section_type: Section_Type | str, content: list | None = None):
        if str(section_type).upper() != Section_Type.CONDUITS.value:
            raise ValueError("Conduits Section must have section_type 'JUNCTIONS'")
        super().__init__(Section_Type.CONDUITS, content)
    def parse(self):
        print(f"Parsing {len(self.content)} conduits...")
