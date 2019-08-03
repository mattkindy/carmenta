from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from parsel import Selector
from selenium.webdriver.common.keys import Keys
import urllib
import json

api_page = Blueprint('api', __name__,
                        template_folder='templates')

chrome_options = Options()
chrome_options.add_argument("--headless")


@api_page.route('/')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)

@api_page.route('/scrape_user')
def scrape_user():
    link = request.args.get('link')

    #TODO use other library to get a specific profile
    return link

def linkedin_login(driver):
    linkedin_username = 'anna.pobletts+hackathon2@praetorian.com'
    linkedin_password = 'Welcome2PS!'
    driver.get('https://www.linkedin.com/login')

    username = driver.find_element_by_id('username')
    username.send_keys(linkedin_username)

    password = driver.find_element_by_id('password')
    password.send_keys(linkedin_password)

    sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
    sign_in_button.click()

@api_page.route('/scraper')
def scraper():
    keyword = "Praetorian"
    if request.args.get('keyword'):
        keyword = request.args.get('keyword')
    search_number = 2
    if request.args.get('num'):
        search_number = request.args.get('num')

    search_query = 'site:linkedin.com/in/ AND "' + keyword + '"'

    driver = webdriver.Chrome(chrome_options=chrome_options)
    linkedin_login(driver)
    driver.get('https://www.google.com/search?' + urllib.parse.urlencode({'q':search_query, "num":search_number}))
    linkedin_urls = driver.find_elements_by_class_name('iUh30')
    linkedin_urls = [url.text for url in linkedin_urls]

    entries = []
    for linkedin_url in linkedin_urls:
        entry = {}
        driver.get(linkedin_url)
        sel = Selector(text=driver.page_source)

        # xpath to extract the text from the class containing the name
        name = sel.xpath('//*[starts-with(@class,  "inline t-24 t-black t-normal break-words")]/text()').extract_first()

        if name:
            entry['name'] = name.strip()

        # xpath to extract the text from the class containing the job title
        job_title = sel.xpath('//*[starts-with(@class, "mt1 t-18 t-black t-normal")]/text()').extract_first()

        if job_title:
            entry['job_title'] = job_title.strip()

        # xpath to extract the text from the class containing the company
        company = sel.xpath(
            '//*[starts-with(@class, "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()

        if company:
            entry['company'] = company.strip()

        # xpath to extract the text from the class containing the college
        college = sel.xpath(
            '//*[starts-with(@class, "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()

        if college:
            entry['college'] = college.strip()

        # xpath to extract the text from the class containing the location
        location = sel.xpath('//*[starts-with(@class, "t-16 t-black t-normal inline-block")]/text()').extract_first()

        if location:
            entry['location'] = location.strip()

        entries.append(entry)
        linkedin_url = driver.current_url

    return json.dumps(entries)