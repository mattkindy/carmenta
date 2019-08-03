from linkedin_scraper import Person, Experience, Education
from linkedin_scraper.functions import time_divide
from parsel import Selector
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from scraper.interface.util import map_from_search


class Candidate(Person):
  def __init__(self, linkedin_url=None, name=None, experiences=[], educations=[], driver=None, get=True, scrape=True):
    super().__init__(linkedin_url, name, experiences, educations, driver, get, scrape)

  def get_connections(self, limit=None):
    driver = self.driver
    # topcard_view_all_connections
    # /search/results/people/
    # find_element_by_xpath("//a[contains(@href, '/search/results/people/')]").text
    driver.find_element_by_xpath("//a[contains(@href, '/search/results/people/')]").click()

    return map_from_search(driver,
                           wait_time=10,
                           fn=lambda res: Candidate.parse_candidate_from_search_result(self.driver, res),
                           limit=limit)

  @staticmethod
  def parse_candidate_from_search_result(driver, search_result):
    try:
      result_link = search_result.find_element_by_class_name("search-result__result-link")
      result_name = search_result.find_elements_by_class_name("search-result__result-link")[1]

      candidate = Candidate(linkedin_url=(result_link.get_attribute("href")),
                            name=result_name.text.encode('utf-8').strip(),
                            driver=driver,
                            get=False,
                            scrape=False)

      position_title = search_result.find_element_by_xpath('.//span[@dir="ltr"]')
      candidate.add_experience(Experience(position_title=position_title.text))
      return candidate
    except:
      return None

  def scrape_logged_in(self, close_on_complete=True):
    driver = self.driver
    _ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "pv-top-card-v3")))
    root = driver.find_element_by_class_name("pv-top-card-v3")
    self.name = str(root.find_elements_by_xpath("//section/div/div/div/*/li")[0].text.strip())

    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")

    try:
      _ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "experience-section")))

      # get experience
      exp = driver.find_element_by_id("experience-section")
      for position in exp.find_elements_by_class_name("pv-position-entity"):
        position_title = position.find_element_by_tag_name("h3").text.strip()
        selector = Selector(text=driver.page_source)
        company_xpath = '//*[starts-with(@class, "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()'
        company = (selector.xpath(company_xpath).extract_first())

        try:
          times = position.find_element_by_class_name("pv-entity__date-range").text.strip()
          times = "\n".join(times.split("\n")[1:])
          from_date, to_date, duration = time_divide(times)
        except:
          from_date, to_date, duration = ("Unknown", "Unknown", "Unknown")
        try:
          location = position.find_element_by_class_name("pv-entity__location").text.strip()
        except:
          location = None
        experience = Experience(position_title=position_title, from_date=from_date, to_date=to_date, duration=duration,
                                location=location)
        experience.institution_name = company
        self.add_experience(experience)
    except TimeoutException:
      print("No experience...")

    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/1.5));")

    try:
      _ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "education-section")))

      # get education
      edu = driver.find_element_by_id("education-section")
      for school in edu.find_elements_by_class_name("pv-education-entity"):
        university = school.find_element_by_class_name("pv-entity__school-name").text.strip()
        degree = "Unknown Degree"
        try:
          degree = school.find_element_by_class_name("pv-entity__degree-name").text.strip()
          times = school.find_element_by_class_name("pv-entity__dates").text.strip()
          from_date, to_date, duration = time_divide(times)
        except:
          from_date, to_date = ("Unknown", "Unknown")
        education = Education(from_date=from_date, to_date=to_date, degree=degree)
        education.institution_name = university
        self.add_education(education)

    except TimeoutException:
      print("No education...")

    if close_on_complete:
      driver.close()

  def scrape_not_logged_in(self, close_on_complete=True, retry_limit=10):
    driver = self.driver
    retry_times = 0
    while self.is_signed_in() and retry_times <= retry_limit:
      page = driver.get(self.linkedin_url)
      retry_times = retry_times + 1

    # get name
    self.name = str(driver.find_element_by_id("name").text.strip())

    # get experience
    exp = driver.find_element_by_id("experience")
    for position in exp.find_elements_by_class_name("position"):
      position_title = position.find_element_by_class_name("item-title").text.strip()
      company = position.find_element_by_class_name("item-subtitle").text.strip()

      try:
        times = position.find_element_by_class_name("date-range").text.strip()
        from_date, to_date, duration = time_divide(times)
      except:
        from_date, to_date, duration = (None, None, None)

      try:
        location = position.find_element_by_class_name("location").text.strip()
      except:
        location = None
      experience = Experience(position_title=position_title,
                              from_date=from_date,
                              to_date=to_date,
                              duration=duration,
                              location=location)
      experience.institution_name = company
      self.add_experience(experience)

    # get education
    edu = driver.find_element_by_id("education")
    for school in edu.find_elements_by_class_name("school"):
      university = school.find_element_by_class_name("item-title").text.strip()
      degree = school.find_element_by_class_name("original").text.strip()
      try:
        times = school.find_element_by_class_name("date-range").text.strip()
        from_date, to_date, duration = time_divide(times)
      except:
        from_date, to_date = (None, None)
      education = Education(from_date=from_date, to_date=to_date, degree=degree)
      education.institution_name = university
      self.add_education(education)

    # get
    if close_on_complete:
      driver.close()
