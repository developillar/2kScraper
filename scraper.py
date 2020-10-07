import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen


my_url = 'https://www.2kratings.com/'
headers = {"User-Agent": "Chrome"}

request = Request(my_url, headers=headers)
page_html = urlopen(request).read()
# request.close()

#html parsing
page_soup = soup(page_html , "html.parser")

page_soup.h1