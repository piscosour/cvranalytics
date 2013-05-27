# -*- coding: utf-8 -*-

import timeline
import web

render = web.template.render("templates/")
## timeline.init_timeline()

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
        map = timeline.word_map(timeline.sections, str(term))
        return render.wordmap(map)
        
class Eventcount:
    def GET(self, year, category):
        return render.eventcount(year, category)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
