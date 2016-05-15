from flask import Flask, render_template, request, session, redirect, url_for, flash
import json
import os
import bigoven.recipes as recipes
import threading
from operator import itemgetter

application = Flask(__name__)
application.debug = True

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


@application.route('/')
def home():
    return render_template('hello.html')


@application.route('/user/<userid>')
def load_user_page(userid):
    def get_user_info(userid):
        json_url = os.path.join(SITE_ROOT, "static/db", userid + ".json")
        with open(json_url, 'r') as data_file:
            data = json.load(data_file)
        return data

    def get_user_ingredients_names(data):
        ingredients = []
        for i in data['Ingredients']:
            ingredients.append(i['Name'])
        return ingredients

    def get_user_recipes(ingredients):
        def worker(recipe_id):
            r = recipes.get_recipe(recipe_id)
            recipe_list.append(r)

        recipe_ids = recipes.search_recipes(ingredients)
        recipe_list = []
        threads = []

        for i in recipe_ids:
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
            t.start()
            t.join()

        for t in threads:
            t.join()

        recipe_list = sorted(recipe_list, key=itemgetter('Title'), reverse=False)
        recipe_list = sorted(recipe_list, key=itemgetter('StarRating'), reverse=True)

        return recipe_list

    user_data = get_user_info(userid)
    ingredients = get_user_ingredients_names(user_data)
    print ingredients
    recipe_list = get_user_recipes(ingredients)

    return render_template('user.html', ing=get_user_info(userid)['Ingredients'], recipes=recipe_list)



if __name__ == '__main__':
    application.run()








