from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask.ext.assets import Environment, Bundle
import json
import os

application = Flask(__name__)
application.debug = True

assets = Environment()
assets.init_app(application)


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

@application.route('/')
def home():
    return render_template('hello.html')

@application.route('/user/<userid>')
def load_user_page(userid):
    json_url = os.path.join(SITE_ROOT, "static/db", userid + ".json")
    with open(json_url, 'r') as data_file:
        data = json.load(data_file)
        ingredients = data['Ingredients']



    return render_template('user.html', ing=ingredients)



if __name__ == '__main__':
    application.run()


