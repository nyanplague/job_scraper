from selenium.webdriver import Chrome
from selenium import webdriver
import time
import pandas as pd



from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_path = "C:/Users/Username/Documents/Development/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_path))

driver.get("https://www.linkedin.com/jobs/search?keywords=Data%20Scientist&location=Toronto%2C%20Ontario%2C%20Canada&geoId=100025096&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0")


jobs_lists = driver.find_element_by_class_name("jobs-search__results-list")
jobs = jobs_lists.find_elements_by_tag_name("li")

print(len(jobs))