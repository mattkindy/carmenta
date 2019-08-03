from flask import Flask
from flask import Blueprint, render_template, abort
from api.api import api_page

app = Flask(__name__)
app.register_blueprint(api_page, url_prefix='/api')

@app.route('/')
def show():
    return 'Hello, World!'

