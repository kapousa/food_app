# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, request


from app.foodsearch import blueprint
from app.fs.middleware.APIsSearchServices import APIsSearchServices


## APIs

@blueprint.route('/findrecipes', methods=['POST'])
def findrecipes():
    if request.method == 'POST':
        search_words = request.form.get("search")
        search_service = APIsSearchServices()
        related_cluster = search_service.get_related_cluster(search_words)
        content = request.get_json(silent=True)

    return 0


@blueprint.route('/api/v1/classifydata', methods=['POST'])
def classifydata_api():
    content = request.json

    return 0


# Errors



@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('page-500.html'), 500
