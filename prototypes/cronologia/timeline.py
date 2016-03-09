# -*- coding: utf-8 -*-
## CVRanalytics: timeline.py

## Parses the "Timeline of Events" section in the Final Report of the
## Peruvian Truth and Reconciliation Commission, and applies natural language
## processing to allow identification of patterns in event data. Uses
## webapp.py as a web front end using the web.py framework.

## Originally developed by Eduardo Marisca @ MIT (emarisca[at]mit[dot]edu).
## Released under a Creative Commons NC-BY-SA 3.0 license.
## Code and additional info available at http://github.com/piscosour/cvranalytics


import nltk
import re
import codecs

## -- Classes -- ##

class Section:
    """A section of the document with events for a single year."""

    def __init__(self, year, text=None):
        self.year = year
        self.text = text
        self.tokens = None
        self.ttext = None
        self.events = []
        self.fdist = None

    ## Why does parse_section() not work as a method?

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
                    if category_check in element:
                        category = category_check
                        continue
                parse_date = re.findall(r'\d\d\sde\s\w+', element)
                if date is None or parse_date == []:
                    date = month
                else:
                    date = parse_date[0]
                ## Next line added for debugging purposes:
                ## print str(date) + "(" + str(category) + "):" + str(element)
                self.events = self.events + [Event(element)]
                self.events[len(self.events) - 1].set_date()
                if self.events[len(self.events) - 1].set_date() is False:
                    self.events[len(self.events) - 1].date = month
                self.events[len(self.events) - 1].set_category(category)


class Event:
    """An event listed in the document."""

    ## Event is initialised only with text. Separate methods are called to set
    ## date (based on parsing text) and category (based on context).
    
    def __init__(self, text):
        self.text = text
        self.date = None
        self.category = None
    
    ## Date parser attempts to infer date from text. If unable to, returns False
    ## and date can be assigned by calling function.
    
    def set_date(self):
        date = re.findall(r'\d\d\sde\s\w+', self.text)
        
        if len(date) > 0:
            self.date = date[0]
            return True
        else:
            self.date = None
            return False
            
    def set_category(self, category):
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

## This was intended as a test function to get the year parsing correct.
## Same procedure then implemented in year_split() on the actual data.

def match_years(data):
    data.seek(0)
    years = []
    
    for line in data:
        years = years + re.findall(r'^\d\d\d\d$', line)

    return years

## Parses text file looking for dates in Spanish format, adds them to list.
## Originally intended to test date parsing. Implemented as a method within
## the Event class.

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
    result_map = {}
	
    for section in sections:
        if section.fdist[term] > max_freq:
            max_freq = section.fdist[term]

    if max_freq == 0:
        print "Term not found in timeline."
        return False
    else:
        for section in sections:
            if __name__ == "__main__":
                print str(section.year) + ":",
                print (section.fdist[term] * 50 / max_freq) * "#" + str(section.fdist[term])
            else:
                result_map[section.year] = section.fdist[term]
    
    return result_map


def event_count(sections, category=None):
    max_count = 0
    total_count = 0
    max_cat_count = 0
    yearly_cat_counts = []
	
    if category is None:
        for section in sections:
            if len(section.events) > max_count:
                max_count = len(section.events)
        
        print "Generating event count table."
        for section in sections:
            print str(section.year) + ":",
            print ((len(section.events) * 50 / max_count) * "#") + str(len(section.events))
            total_count = total_count + len(section.events)
        print "Done. " + str(total_count) + " total events."
    elif category is not None:
        for section in sections:
            cat_counter = 0
            for event in section.events:
                if event.category == category:
                    cat_counter = cat_counter + 1
            yearly_cat_counts = yearly_cat_counts + [cat_counter]
            if cat_counter > max_cat_count:
                max_cat_count = cat_counter
        
        print "Generating event count table for category " + str(category)
        for i in range(len(sections)):
            print str(sections[i].year) + ":",
            print ((yearly_cat_counts[i] * 50 / max_cat_count) * "#") + str(yearly_cat_counts[i])
            total_count = sum(yearly_cat_counts)
        print "Done. " + str(total_count) + " total events."    
    


def show_events_slice(sections, year=None, category=None):
    counter = 0
    
    if year is None and category is None:
        print "Must specify year or category to generate slice."
        return False
    elif year is not None and category is None:
        print "Generating slice for year " + str(year)
        for section in sections:
            if int(year) == section.year:
                for event in section.events:
                    print str(event.date) + ". " + str(event.text) + " (" + str(event.category) + ")"
                    counter = counter + 1
    elif year is not None and category is not None:
        print "Generating slice for year " + str(year) + " and category " + str(category)
        for section in sections:
            if int(year) == section.year:
                for event in section.events:
                    if event.category == category:
                        print str(event.date) + ". " + str(event.text) + " (" + str(event.category) + ")"
                        counter = counter + 1
    elif year is None and category is not None:
        print "Generating slice for category " + str(category)
        for section in sections:
            print section.year
            for event in section.events:
                if event.category == category:
                    print str(event.date) + ". " + str(event.text) + " (" + str(event.category) + ")"
                    counter = counter + 1
            print "\n"
    print "Done. " + str(counter) + " events listed."

def parse_events_all_sections(sections):
    for section in sections:
        section.parse_events()

def init_timeline(data, sections):
    sections = year_split(data)
    parse_sections(sections)
    parse_events_all_sections(sections)
    
    return sections


## -- Things we do on load (unless import): -- ##

if __name__ == "__main__":
    
    ## We split the file on load to have separate yearly sections.
    
    print "Parsing files into yearly sections...",
    sections = year_split(data)
    print "Done."
    
    ## And parse the text into NLTK-operable fields.
    
    print "Parsing text for natural language processing...",
    parse_sections(sections)
    print "Done."
    
    ## Parse every section for event data (still very imperfect).
    
    print "Parsing sections for event data...",
    parse_events_all_sections(sections)
    print "Done."
    
