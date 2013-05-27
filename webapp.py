# -*- coding: utf-8 -*-

import timeline
import web

render = web.template.render("templates/")

urls = (
    "/(.*)", "Index",
    "/wordmap/(.*)", "Wordmap",
    "/eventcount/(.*)", "Eventcount"
)

class Index:
    def GET(self, name):
        return render.index(name)

class Wordmap:
    def GET(self, term):
        return render.wordmap(term)
        
class Eventcount:
    def GET(self, year, category):
        return render.eventcount(year, category)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
