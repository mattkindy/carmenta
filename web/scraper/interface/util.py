import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def map_from_search(driver, wait_time, fn, limit=None):
  _ = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results__list")))
  total = []

  driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")
  time.sleep(0.5)
  driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*3/4));")
  results_list = driver.find_element_by_class_name("search-results__list")
  results_items = results_list.find_elements_by_class_name("search-result")

  for res in results_items:
    total.append(fn(res))
    if limit and len(total) > limit:
      return total

  while driver.find_element_by_class_name("artdeco-pagination__button--next").is_enabled():
    driver.find_element_by_class_name("artdeco-pagination__button--next").click()
    _ = WebDriverWait(driver, wait_time).until(EC.staleness_of(driver.find_element_by_class_name("search-result")),
                                               'visible')

    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/4));")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/3));")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*2/3));")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*3/4));")

    results_list = driver.find_element_by_class_name("search-results__list")
    results_items = results_list.find_elements_by_class_name("search-result")
    for res in results_items:
      _ = WebDriverWait(driver, wait_time).until(EC.visibility_of(res))
      total.append(fn(res))
      if limit and len(total) > limit:
        return total

  return total
