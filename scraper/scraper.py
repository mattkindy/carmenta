from time import sleep
from selenium import webdriver
import csv
from parsel import Selector
from selenium.webdriver.common.keys import Keys

search_query = 'site:linkedin.com/in/ AND "Praetorian"'
file_name = 'results_file.csv'

linkedin_username = 'anna.pobletts+hackathon@praetorian.com'
linkedin_password = 'Welcome2PS!'

driver = webdriver.Chrome('/Users/apobletts/bin/chromedriver')
driver.get('https://www.linkedin.com/login')

username = driver.find_element_by_id('username')
username.send_keys(linkedin_username)
#sleep(0.5)

password = driver.find_element_by_id('password')
password.send_keys(linkedin_password)
#sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
#sleep(0.5)

driver.get('https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+AND+%22Praetorian%22&num=500')

#search_query = driver.find_element_by_name('q')
#search_query.send_keys(search_query)
#sleep(0.5)

#search_query.send_keys(Keys.RETURN)
#sleep(3)

linkedin_urls = driver.find_elements_by_class_name('iUh30')
linkedin_urls = [url.text for url in linkedin_urls]
#sleep(0.5)

print(linkedin_urls[0:10])

with open(file_name, 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Name","Job Title", "Company", "College", "Location"])

    for linkedin_url in linkedin_urls:

        driver.get(linkedin_url)
        sleep(1)
        sel = Selector(text=driver.page_source)

    # xpath to extract the text from the class containing the name
        name = sel.xpath('//*[starts-with(@class,  "inline t-24 t-black t-normal break-words")]/text()').extract_first()

        if name:
            name = name.strip()


        # xpath to extract the text from the class containing the job title
        job_title = sel.xpath('//*[starts-with(@class, "mt1 t-18 t-black t-normal")]/text()').extract_first()

        if job_title:
            job_title = job_title.strip()


        # xpath to extract the text from the class containing the company
        company = sel.xpath('//*[starts-with(@class, "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()

        if company:
            company = company.strip()


        # xpath to extract the text from the class containing the college
        college = sel.xpath('//*[starts-with(@class, "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()

        if college:
            college = college.strip()


        # xpath to extract the text from the class containing the location
        location = sel.xpath('//*[starts-with(@class, "t-16 t-black t-normal inline-block")]/text()').extract_first()

        if location:
            location = location.strip()

        #print(name, job_title, company, college, location)
        writer.writerow([name, job_title, company, college, location])

        linkedin_url = driver.current_url

    #driver.quit()


