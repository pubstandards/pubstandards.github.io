#!/usr/bin/python
import flask
app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('homepage.html')

@app.route('/about')
def next():
    return flask.render_template('about.html')

@app.route('/newchapter')
def previous():
    return flask.render_template('newchapter.html')

if __name__ == '__main__':
    app.run(debug=True)
