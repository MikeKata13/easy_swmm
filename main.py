from src.easy_swmm.core.sections import Core_Section, Section_Type

# from src.easy_swmm.io.parser import Parser


def main():
    print("Testing imports...")
    section = Core_Section(Section_Type.JUNCTIONS)
    print(section.sectionType.value)


if __name__ == "__main__":
    main()
