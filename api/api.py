from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

api_page = Blueprint('api', __name__,
                        template_folder='templates')


@api_page.route('/')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)


@api_page.route('/scraper')
def scrape():
    return "Scraping"