from pathlib import Path
import re
from easy_swmm.core.sections import Core_Section
from easy_swmm.io.model import Model


class Parser:
    """Reads a SWMM input file and builds a structured Model."""
    section_pattern = re.compile(r"^\[(.*?)\]")

    def read_file(self, file: Path | str, custom_section:bool = False) -> Model:
        path = Path(file)
        raw_content = path.read_text().splitlines()

        sections_dict = dict(self.create_sections(raw_content))
        section_names = list(sections_dict.keys())

        sections = {
            name: Core_Section(name, content=lines, custom=custom_section)
            for name, lines in sections_dict.items()
        }

        return Model(content=raw_content, section_names=section_names, sections=sections)

    def create_sections(self, lines: list[str]):
        current_name = None
        current_lines = []

        for line in lines:
            if line.startswith('['):
                m = self.section_pattern.match(line)
                if m:
                    if current_name is not None:
                        yield current_name, current_lines
                    current_name = m.group(1).upper()
                    current_lines = []
            elif current_name:
                current_lines.append(line)

        if current_name:
            yield current_name, current_lines
