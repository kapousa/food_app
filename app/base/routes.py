from flask import render_template, request
from jinja2 import TemplateNotFound

from app.base import blueprint



@blueprint.route('/')
def index():
    return render_template('home/index.html', segment='index')



