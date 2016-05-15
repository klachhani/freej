from flask import Flask, render_template, request, session, redirect, url_for, flash
import json
import os
import bigoven.recipes as recipes
import threading

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

        ingredients = []
        for i in data['Ingredients']:
            ingredients.append(i['Name'])
        return ingredients

    def get_user_recipes(ingredients):
        def worker(recipe_id):
            r = recipes.get_recipe(recipe_id)
            print r
            recipe_list.append(r)

        recipe_ids = recipes.search_recipes(ingredients)
        print recipe_ids

        recipe_list = []
        threads = []
        for i in recipe_ids[:20]:
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return recipe_list


    ingredients = get_user_info(userid)
    recipe_list = get_user_recipes(ingredients)

    print len(recipe_list)

    return render_template('user.html', ing=ingredients, recipes=recipe_list)



if __name__ == '__main__':
    application.run()








