import sys
import os
import pprint
import argparse

parser = argparse.Parser()
parser.add_argument()
# Add the 'src' folder to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from easy_swmm.core.sections import Core_Section, Section_Type
from easy_swmm.io.parser import Parser
from pathlib import Path

file = 
parser = Parser()
model = parser.read_file(file)
print(model.section_names)
print(model.INFLOWS.lines)
