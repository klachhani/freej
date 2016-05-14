from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'You are home!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'The user is...%s' % username


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
