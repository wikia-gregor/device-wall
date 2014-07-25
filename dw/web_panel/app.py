"""Device Wall Web Panel"""
__author__ = 'wikia-gregor'


import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    """Panel main page"""
    return flask.render_template('index.html')


def run_panel():
    """Run web application"""
    app.debug = True
    app.run()

