import json

from flask import Blueprint, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from api.api import api_root
from scraper.interface.candidate import Candidate
from scraper.interface.company import Company

scrape_root = Blueprint('scrape', __name__, url_prefix="{}/scrape".format(api_root.url_prefix))

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


def linkedin_login(driver, linkedin_username, linkedin_password):
  driver.get('https://www.linkedin.com/login')

  username = driver.find_element_by_id('username')
  username.send_keys(linkedin_username)

  password = driver.find_element_by_id('password')
  password.send_keys(linkedin_password)

  sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
  sign_in_button.click()


@scrape_root.route('/user', methods=['POST'])
def scrape_user():
  data = request.get_json()

  # TODO use other library to get a specific profile
  return data['link']


@scrape_root.route('/user/connections', methods=['POST'])
def scrape_user_connections():
  args = request.args
  limit = int(args.get('limit'))

  data = request.get_json()

  driver = webdriver.Chrome()
  linkedin_login(driver, linkedin_username=data['username'], linkedin_password=data['password'])

  candidate = Candidate(data['link'], driver=driver, scrape=False)

  connections = candidate.get_connections(limit=limit)
  return json.dumps([{
    'name': str(c.name),
    'url': c.linkedin_url,
  } for c in connections])


@scrape_root.route('/company', methods=['POST'])
def scrape_company():
  keyword = "Security"

  data = request.get_json()
  username = data['username']
  password = data['password']

  driver = webdriver.Chrome()
  linkedin_login(driver, linkedin_username=username, linkedin_password=password)

  company_url = 'https://www.linkedin.com/company/praetorian/'
  praetorian = Company(company_url, driver=driver, scrape=False)
  print('Making request for {}'.format(company_url))
  employees = praetorian.get_employees()

  existing_users = set()

  employees = [
    employee
    for employee in employees
    if 'search' not in employee.linkedin_url
       and employee.name not in existing_users
       and employee.experiences
  ]

  security_employees = [
    employee
    for employee in employees
    if keyword.lower() in employee.experiences[0].position_title.lower()
  ]

  entries = []

  for employee in security_employees:
    linkedin_url = employee.linkedin_url
    position_title = employee.experiences[0].position_title

    print('Scraping: {} for {}: {}'.format(linkedin_url, employee.name, position_title))
    candidate = Candidate(linkedin_url, driver=driver, scrape=False)
    candidate.scrape(close_on_complete=False)

    experience = candidate.experiences[0] if candidate.experiences else None
    education = candidate.educations[0] if candidate.educations else None

    entry = {
      'name': candidate.name,
      'job_title': experience.position_title if experience else None,
      'company': experience.institution_name if experience else None,
      'college': education.institution_name if education else None,
      'location': experience.location if experience else None,
    }

    entries.append(entry)

    from database.models import Candidate
    from database.models import db
    c = Candidate(employee.linkedin_url, employee.name, "mytitle", "schools1", "work1", "location1", "cool")
    db.session.add(c)
    db.session.commit()

  return json.dumps(entries)


if __name__ == '__main__':
  driver = webdriver.Chrome()
  linkedin_login(driver, linkedin_username="user", linkedin_password="pass")

  candidate = Candidate('https://www.linkedin.com/in/amlweems/', driver=driver, scrape=False)

  connections = candidate.get_connections(limit=5)
  dumped = json.dumps([{'name': str(c.name), 'url': c.linkedin_url} for c in connections])
  print(dumped)
