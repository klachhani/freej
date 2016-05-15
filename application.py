from flask import Flask, render_template

freej = Flask(__name__)

freej.debug = True

@freej.route('/')
def home():
    return 'Hello World!'

@freej.route('/user/<userid>')
def load_user_page(userid):
    return 'Hey, youre userid is %s' % userid


if __name__ == '__main__':
    freej.run()
