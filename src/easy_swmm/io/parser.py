from easy_swmm.core.sections import Section_Type, Core_Section, JunctionsSection, ConduitsSection
from pathlib import Path
import re
from easy_swmm.io.model import Model


class Parser:
    """Reads a SWMM input file and builds a structured Model."""

    sectionPattern = re.compile(r"\[(.*?)\]")

    def read_file(self, file: Path | str) -> Model:
        with open(file, "r") as f:
            content = [line.strip("\n") for line in f.readlines()]

        section_names = self.get_section_names(content)
        sections = self.build_sections(content, section_names)

        return Model(content=content, section_names=section_names, sections=sections)

    @classmethod
    def get_section_names(cls, content: list) -> list:
        return [m.group(1).upper() for line in content if (m := cls.sectionPattern.match(line))]

    @staticmethod
    def build_sections(content: list, section_names: list) -> dict[str, Core_Section]:
        sections = {}
        current_name = None
        current_lines = []

        for line in content:
            if m := re.match(r"\[(.*?)\]", line):
                if current_name:
                    sections[current_name] = Parser.create_section(current_name, current_lines)
                current_name = m.group(1).upper()
                current_lines = []
            elif current_name:
                current_lines.append(line)

        if current_name:
            sections[current_name] = Parser.create_section(current_name, current_lines)

        return sections

    @staticmethod
    def create_section(name: str, lines: list) -> Core_Section:
        """Factory that maps section name → specific Section class."""
        match name:
            case "JUNCTIONS":
                return JunctionsSection(Section_Type.JUNCTIONS, lines)
            case "CONDUITS":
                return ConduitsSection(Section_Type.CONDUITS, lines)
            case _:
                return Core_Section(name, lines)
