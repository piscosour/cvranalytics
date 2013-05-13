# -*- coding: utf-8 -*-

import nltk
import re
import codecs

## -- Classes -- ##

class Section:
    """A section of the document with events for a single year."""

    def __init__(self, year, text=None, tokens=None, ttext=None):
        self.year = year
        self.text = text
        self.tokens = tokens
        self.ttext = ttext
        self.events = []
        self.fdist = None

## Why does this not work as a method?

    def parse_section(self):
        self.text = self.text.encode("utf-8")
        self.tokens = nltk.word_tokenize(self.text)
        self.ttext = nltk.Text(self.tokens)

    def parse_events(self):
	    category = None
	    date = None
	    month = None
	    
	    splitted = self.text.split("\n")
	    
	    for element in splitted:
	    	if element == '' or element == ' ' or re.search(r'^\d\d$', element) is not None:
				continue
            for month_check in months:
				if month_check in element:
					month = month_check
					continue
            if month is not None:
				for category_check in categories:
					if category_check.decode("utf-8") in element:
						category = category_check
						continue
				parse_date = re.findall(r'\d\d\sde\s\w+', element)
				if date is None or parse_date == []:
					date = month
				else:
					date = parse_date[0]
				print date + "(" + category + "):" + element
				self.events = self.events + [Event(element, date, category)]


class Event:
	"""An event listed in the document."""
	
	def __init__(self, text, date=None, category=None):
		self.text = text
		self.date = date
		self.category = category
		

## -- Data -- ##

months = {"Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5,
          "Junio": 6, "Julio": 7, "Agosto": 8, "Setiembre": 9, "Octubre": 10,
          "Noviembre": 11, "Diciembre": 12}
categories = ["Política", "Fuerzas Armadas y Policiales", 
              "Violencia de origen político", "Movimientos sociales", "Exterior", 
              "Derechos humanos", "Congreso", "Centros Penitenciarios", 
              "Partidos políticos"]
data = codecs.open("cronologia.txt", encoding="utf-8", mode="r")
sections = []


## -- Functions/Operations -- ##

## Parses text file looking for year values, adds them to a list.

def match_years(data):
    data.seek(0)
    years = []
    
    for line in data:
        years = years + re.findall(r'^\d\d\d\d$', line)

    return years


## Parses text file looking for dates in Spanish format, adds them to list.

def match_dates(data):
    data.seek(0)
    dates = []
    
    for line in data:
        dates = dates + re.findall(r'\d\d\sde\s\w+', line)

    return dates


## Parses text file, identifies year values and appends a new Section object
## to the sections list. It then adds every line before the next year value
## to the text attribute of the Section object.

def year_split(data):
    data.seek(0)
    sections = []

    for line in data:
        if re.match(r'^\d\d\d\d$', line) is not None:
            sections = sections + [Section(int(line[:4]))]
        else:
            if sections[-1].text is None:
                sections[-1].text = line
            else:
                sections[-1].text = sections[-1].text + line

    return sections

def parse_sections(sections):
	for section in sections:
		section.text = section.text.encode("utf-8")
		section.tokens = nltk.word_tokenize(section.text)
		section.ttext = nltk.Text(section.tokens)
		section.fdist = nltk.FreqDist(section.ttext)

def yearly_collocations(sections):
	for section in sections:
		print section.year
		section.ttext.collocations()

def word_map(sections, term):
	max_freq = 0
	
	for section in sections:
			if section.fdist[term] > max_freq:
				max_freq = section.fdist[term]
		
	if max_freq == 0:
		print "Term not found in timeline."
	else:
		for section in sections:
			print str(section.year) + ":",
			print (section.fdist[term] * 50 / max_freq) * "#" + str(section.fdist[term])
		

## -- Things we do on load: -- ##

## We split the file on load to be able to operate directly.

sections = year_split(data)

## And parse the text into NLTK-operable fields.

parse_sections(sections)