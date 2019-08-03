from linkedin_scraper import scraper, Person, Company, actions
from selenium import webdriver
driver = webdriver.Chrome("/Users/apobletts/bin/chromedriver")


search_query = 'site:linkedin.com/in/ AND "Praetorian"'
file_name = 'results_file.csv'


linkedin_username = 'anna.pobletts+hackathon@praetorian.com'
linkedin_password = 'Welcome2PS!'


driver = webdriver.Chrome('/Users/apobletts/bin/chromedriver')
#driver.get('https://www.linkedin.com/login')
#actions.login(driver, linkedin_username, linkedin_password) # if email and password isnt given, it'll prompt in terminal

#username = driver.find_element_by_id('username')
#username.send_keys(linkedin_username)
#sleep(0.5)

#password = driver.find_element_by_id('password')
#password.send_keys(linkedin_password)
#sleep(0.5)

#sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
#sign_in_button.click()
#sleep(0.5)

driver.get('https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+AND+%22Praetorian%22&num=100')

#search_query = driver.find_element_by_name('q')
#search_query.send_keys(search_query)
#sleep(0.5)

#search_query.send_keys(Keys.RETURN)
#sleep(3)

linkedin_urls = driver.find_elements_by_class_name('iUh30')
linkedin_urls = [url.text for url in linkedin_urls]

people = []

actions.login(driver, linkedin_username, linkedin_password) # if email and password isnt given, it'll prompt in terminal
for linkedin_url in linkedin_urls:
    print(linkedin_url)
    person = Person(linkedin_url, driver=driver, scrape=False)
    person.scrape(close_on_complete=False)
    people.append(person)

