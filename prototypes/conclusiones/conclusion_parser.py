# -*- coding: utf-8 -*-
## mem0r1a: conclusion_parser.py

## Parses a text version of the conclusions to the Final Report of the Peruvian Truth and Reconciliation Commission. 
## Using regular expressions, we analyse the file line by line to determine the nature of the content to then 
## create structure versions of every conclusion. These versions are finally printed out in JSON format to a text file.

## Released under a Creative Commons NC-BY-SA 3.0 license.
## Code and additional info available at http://github.com/piscosour/mem0r1a

import re
import codecs
import json

datafile = codecs.open("conclusiones.txt", encoding="utf-8", mode="r")

class Conclusion:

    """A conclusion to the report."""
    
    def __init__(self, section, subsection, number, content=None):
        self.section = section
        self.subsection = subsection
        self.number = number
        self.content = content

def parse_conclusions(data):
    data.seek(0)
    conclusions_list = []
    active_subsection = None

    for line in data:
        if re.match(r"^\w+(/?\w+)?\.", line):
            flag = re.match(r"^\w+(/?\w+)?\.", line).group(0)
            if re.match(r"^[IV]+\.", flag):
                active_section = re.match(r"^[IV]+", flag).group(0)
            elif re.match(r"^[A-E]\.", flag):
                active_subsection = re.match(r"^[A-E]", flag).group(0)
            elif re.match(r"^\d+(/?\d+)?\.", flag):
                active_number = re.match(r"^\d+(/?\d+)?", flag).group(0)
                active_text = re.sub(r"^\d+(/?\d+)?\. ", "", line)
                conclusions_list = conclusions_list + [Conclusion(active_section, active_subsection, active_number, active_text)]

    return conclusions_list

def build_dictionary(parsed_data):
    conclusions_dict = {}

    for element in parsed_data:
        conclusions_dict[str(element.number)] = {"seccion": element.section, "subseccion": element.subsection, "contenido": element.content}

    return conclusions_dict

conclusions = parse_conclusions(datafile)

with open('cvr_conclusiones.json', 'w') as output:
    json.dump(build_dictionary(conclusions), output, sort_keys=False, indent=4, separators=(',', ': '))

