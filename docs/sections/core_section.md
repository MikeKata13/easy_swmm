# Core Section

This is the core class section.
Each separate section in the `.inp` file is built upon this and its own, custom attributes and methods.

```python
class Core_Section:
    def __init__(self, section_type: Section_Type | str, content: list | None = None, custom:bool = False):
        if isinstance(section_type, Section_Type):
            self.section_type = section_type
        elif not isinstance(section_type, Section_Type) and custom==True:
            self.section_type = Section_Type.custom(section_type)
        else:
            raise ValueError("Incorrect section in the file. Pass flag 'custom=True' if you want a custom section")

        self.name = str(section_type).upper()
        self.headers = []
        self.comments = []
        self.content = content or []

    def __repr__(self):
        return f"<Core_Section {self.section_type.value} ({len(self.content)} lines)>"

    def parse(self):
        """Optionally overridden by subclasses."""
        pass
```
`section_type`: If not `custom=True`, it is validated to one of the section types in [`Section_Type`](section_type.md)
