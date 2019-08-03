from flask import Flask
from flask import Blueprint, render_template, abort
from api.api import api_page
from templates import app

#Load this config object for development mode
app.config.from_object('configurations.DevelopmentConfig')
app.register_blueprint(api_page, url_prefix='/api')

@app.route('/')
def show():
    return 'Hello, World!'


app.run()
