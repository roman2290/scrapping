import requests
from bs4 import BeautifulSoup
import fake_useragent
import json
import time
import bs4
from fake_headers import Headers
import pprint




fake_useragent = Headers
def get_link():
    return Headers(browser="opera", os="win").generate()


response = requests.get("https://spb.hh.ru/search/vacancy",
                         headers=get_link())
main_page_data = bs4.BeautifulSoup(response.text, features="lxml")
main = main_page_data.find("main", class_ = "vacancy-serp-content")
v_card = main.find_all("div", class_= "vacancy-search-item__card")

list_vacance = []

for job_h in v_card:
    
    salary_s = job_h.find("div", class_ = "narrow-container--lKMghVwoLUtnGdJIrpW4").find("span", class_ = "bloko-text")
    salary = salary_s
    
    name_company = job_h.find(class_ = "bloko-link bloko-link_kind-secondary")
    company = name_company.text.strip()

    city = job_h.find("div", class_ = "narrow-container--lKMghVwoLUtnGdJIrpW4").find("span", class_ = "bloko-text")
    city_c = city

    link_job = job_h.find("a", attrs = {"data-qa": "vacancy-serp__vacancy-employer"})
    site_link_job = link_job["href"]
    link_site = f'https://spb.hh.ru/search/vacancy{site_link_job}'


list_job = ({
        'salary': salary,
        'company': company,
        'city_c':city_c,
        'link_site': link_site
    })
list_vacance.append(list_job)

with open("job.json", "w", encoding="utf-8") as f:
    json.dump(list_vacance, f, ensure_ascii=False, indent=1)


