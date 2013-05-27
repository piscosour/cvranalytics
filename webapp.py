# -*- coding: utf-8 -*-

import timeline
import web

render = web.template.render("templates/")
timeline_sections = []
timeline_sections = timeline.init_timeline(timeline.data, timeline_sections)


urls = (
    "/", "Index",
    "/wordmap/(.*)", "Wordmap",
    "/eventcount/(.*)", "Eventcount"
)

class Index:
    def GET(self):
        return render.index()

class Wordmap:
    def GET(self, term):
        map = timeline.word_map(timeline_sections, str(term))
        max = sorted(map.values())[-1]
        return render.wordmap(map, max, term)
        
class Eventcount:
    def GET(self, year, category):
        return render.eventcount(year, category)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
