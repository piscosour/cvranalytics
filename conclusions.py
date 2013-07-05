# -*- coding: utf-8 -*-
## CVRanalytics: conclusions.py

## Performas exploratory computational analysis on the 171 conclusions to the
## Final Report by the Peruvian Truth and Reconciliation Commission.
## This file provides backend processing and analysis, which is then served through
## a web frontend using webapp.py.

## Originally developed by Eduardo Marisca @ MIT (emarisca[at]mit[dot]edu).
## Released under a Creative Commons NC-BY-SA 3.0 license.
## Code and additional info available at http://github.com/piscosour/cvranalytics

import nltk
import re
import codecs

datafile = codecs.open("conclusiones.txt", encoding="utf-8", mode="r")
conclusions = []

class Conclusion:

    """A conclusion to the report."""
    
    def __init__(self, text):
        self.id = int(re.findall(r"\d+", text)[0])
        self.text = text[len(re.findall(r"\d+", text)[0])+2:]
        self.tags = []
    
    def add_tag(self, tags):
        if type(tags) is not "list":
            raise ValueError("Tags must be passed as list.")
        else:
            self.tags = self.tags + tags

def parse_conclusions(data):
    data.seek(0)
    conclusion_holder = []
    counter = 1
    
    for line in data:
        if re.match(r"^\d", line) is not None:
            conclusion_holder = conclusion_holder + [Conclusion(line)]
            counter = counter + 1
    
    return conclusion_holder

conclusions = parse_conclusions(datafile)    