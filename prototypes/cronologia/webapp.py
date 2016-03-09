# -*- coding: utf-8 -*-
## CVRanalytics: webapp.py

## Provides a web-based front end using the web.py framework for easy access
## to the data and functions in CVRanalytics. Updated version using Flask instead
## of web.py.

## Originally developed by Eduardo Marisca @ MIT (emarisca[at]mit[dot]edu).
## Released under a Creative Commons NC-BY-SA 3.0 license.
## Code and additional info available at http://github.com/piscosour/cvranalytics

from flask import Flask
from flask import render_template
from flask import request

import timeline
import conclusions
from conclusions import conclusions_list

## Initialise Flask app

app = Flask(__name__)

@app.route("/conclusion/<int:conclusion_id>")
def render_conclusion(conclusion_id):
    global conclusions_list
    for element in conclusions_list:
        if conclusion_id == element.id:
            return render_template("conclusion.html", conclusion=element)
    else:
        return "Conclusion not found."

@app.route("/conclusion/tags/<tag>")
def render_tagged_conclusions(tag, data=conclusions_list):
    selection = []
    
    for element in data:
        if tag in element.tags:
            selection = selection + [element]
    
    return render_template("tagged_list.html", tag=tag, selection=selection)


## Run app

if __name__ == "__main__":
    app.debug = True
    app.run()
