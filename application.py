from flask import Flask, render_template, request, session, redirect, url_for, flash
import json
import os
import bigoven.recipes as recipes

application = Flask(__name__)
application.debug = True

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


@application.route('/')
def home():
    return render_template('hello.html')


@application.route('/user/<userid>')
def load_user_page(userid):
    json_url = os.path.join(SITE_ROOT, "static/db", userid + ".json")
    data = json.load(open(json_url, 'r'))
    ingredients = []

    for i in data['Ingredients']:
        ingredients.append(i['Name'])

    recipe_ids = recipes.search_recipes(ingredients)
    recipe_list = []
    for i in recipe_ids[:20]:
        recipe_list.append(recipes.get_recipe(i))

    print recipe_list

    return render_template('user.html', ing=ingredients, recipes=recipe_list)



if __name__ == '__main__':
    application.run()


