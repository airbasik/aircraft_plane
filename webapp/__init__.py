from flask import Flask, render_template
from webapp.forms import BasicParametersForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')


    @app.route("/")
    def hello():
        text = 'Hello!'
        return render_template('index.html', text=text)


    @app.route("/start")
    def basic_parameters():
        basic_parameters_form = BasicParametersForm()
        return render_template('calculation.html', form=basic_parameters_form)


    return app