# Section Type
Class to validate the section types for the parsed `.inp` file:

```python
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
```


