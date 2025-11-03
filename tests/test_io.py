
def test_section_names():
    from pathlib import Path
    import tomllib
    from easy_swmm.io.parser import Parser
    config_path = Path().cwd() / "config.toml"

    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    file_path = Path(config["paths"]["example3"])
    parser = Parser()              
    model = parser.read_file(file_path)  

    assert model.section_names, "Parser did not return any sections"

    names_to_check = ["TITLE", "SUBCATCHMENTS", "POLLUTANTS"]
    for name in names_to_check:
        assert name in model.section_names, f"Missing expected section: {name}"


def test_section_types():
    from pathlib import Path
    import tomllib
    from easy_swmm.core.sections import Core_Section, Section_Type
    from easy_swmm.io.parser import Parser

    config_path = Path().cwd() / "config.toml"

    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    file_path = Path(config["paths"]["example3"])
    parser = Parser()              
    model = parser.read_file(file_path)  

    # Ensure sections exist
    assert model.sections, "No sections were parsed"

    for section_name, section_obj in model.sections.items():
        # All sections should be Core_Section or subclass
        assert isinstance(section_obj, Core_Section), f"{section_name} is not a Core_Section"

