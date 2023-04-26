import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class Scraper:
    def __init__(self, title, location, experience, type, salary):
        self.title = title
        self.location = location
        self.experience = experience
        self.type = type
        self.salary = salary


    def get_info_djinni(self):
        URL = f"https://djinni.co/jobs/?keywords={self.title}&all-keywords=&any-of-keywords=&exclude-keywords=&region=UKR&exp_level={self.experience}&employment={self.type}&salary={self.salary}"
        response = requests.get(url=URL)
        html_page = response.text
        soup = BeautifulSoup(html_page, "html.parser")
        titles = soup.find_all(name="a", class_="profile", href=True)
        dict_linkedin = {}
        for title in titles:
            dict_linkedin[title.getText()] = title['href']

        return dict_linkedin

    def get_info_dou(self):
        req = Request(
            url='https://jobs.dou.ua/vacancies/?search=python+lviv',
            headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'},

        )
        webpage = urlopen(req).read()
        decoded = webpage.decode()
        soup = BeautifulSoup(decoded, "html.parser")

        titles = soup.find_all(name="a", class_="vt", href=True)

        dict_dou = {}
        for title in titles:
            dict_dou[title.getText()] = title['href']
        return dict_dou

    def get_info_linkedin(self):
        experience = ""
        if self.experience == '1y':
            experience = "2"
        if self.experience == '2y':
            experience = "4"
        if self.experience == '3y' or self.experience == '5y':
            experience = '5'


        type = ""

        if self.type == "office" or "remote":
            type = "F"
        if self.type == "parttime":
            type = "P"

        title = self.title.replace(' ', '%20')
        URL = f"https://www.linkedin.com/jobs/search?keywords={title}&f_E={experience}&f_JT={type}&location={self.location}&P&position=1&pageNum=0"
        response = requests.get(url=URL)

        html_page = response.text
        soup = BeautifulSoup(html_page, "html.parser")

        titles_soup = soup.find_all(name="span", class_="sr-only")
        links_soup = soup.find_all(name="a", class_="base-card__full-link", href=True)

        titles_list = []
        links_list = []


        for title in titles_soup:
            titles_list.append(title.getText())
        del titles_list[0:2]
        del titles_list[-1]


        for link in links_soup:
            links_list.append(link['href'])


        dict_linkedin ={}
        for key in titles_list:
            for value in links_list:
                dict_linkedin[key] = value


        return dict_linkedin
