"""Device Wall Web Panel"""
__author__ = 'wikia-gregor'


import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    """Panel main page"""
    return flask.render_template('index.html')


@app.route('/devices-list')
def devices_list():
    pass


@app.route('/device/<int:device_id>')
def display_device(device_id):
    pass


def run_panel():
    """Run web application"""
    app.debug = True
    app.run()

