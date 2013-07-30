# -*- coding: utf-8 -*-
## CVRanalytics: webapp.py

## Provides a web-based front end using the web.py framework for easy access
## to the data and functions in CVRanalytics.

## Originally developed by Eduardo Marisca @ MIT (emarisca[at]mit[dot]edu).
## Released under a Creative Commons NC-BY-SA 3.0 license.
## Code and additional info available at http://github.com/piscosour/cvranalytics


import timeline
import web
from web import form

render = web.template.render("templates/")
timeline_sections = []
timeline_sections = timeline.init_timeline(timeline.data, timeline_sections)

term_select = form.Form(
    form.Textbox("term", description="Buscar:")
)

urls = (
    "/", "Index",
    "/wordmap/(.*)", "Wordmap",
    "/eventcount/(.*)", "Eventcount"
)

class Index:
    def GET(self):
        f = term_select()
        return render.index(f)
        
class Wordmap:
    def GET(self, term):
        user_term = web.input(term=None)
        if user_term.term is not None:
            term = user_term.term
        ## if "," in term:
        ##    terms = split(term, ",")
        map = timeline.word_map(timeline_sections, str(term))
        if map == False:
            max = 0
        else:
            max = sorted(map.values())[-1]
        return render.wordmap(map, max, term)

class Eventcount:
    def GET(self, year, category):
        return render.eventcount(year, category)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
