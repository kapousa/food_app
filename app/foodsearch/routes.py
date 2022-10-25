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
        tags,meals = search_service.search_meals(search_words)

    return render_template('home/index.html', search_words = search_words,
                           has_results= '1',
                           tags= tags, meals = meals)

@blueprint.route('/showmeal', methods=['GET'])
def showmeal():
    if request.method == 'GET':
        meal_Id = request.args.get("id")
        search_service = APIsSearchServices()
        meal, interactions = search_service.show_meal(meal_Id)

    return render_template('home/meal.html', meal= meal, interactions = interactions)


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
