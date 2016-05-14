from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'

@app.route('/user/<userid>')
def load_user_page(userid):
    return 'Hey, youre userid is %s' % userid


if __name__ == '__main__':
    app.run()
