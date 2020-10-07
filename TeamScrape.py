import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen


def scrape_Team():
    team = input("Enter Team Name:")
    teamdash =team.replace(' ', "-")
    my_url = 'https://www.2kratings.com/' + teamdash
    headers = {"User-Agent": "Chrome"}
    request = Request(my_url, headers = headers)
    page_html = urlopen(request).read()
    page_soup = soup(page_html, "html.parser")


    containers = page_soup.findAll("span",{"class":"entry-bg mr-1"})
    plist = []
    for container in containers:
        plist.append(container('img')[0]['alt'])
    

    #remove team name from list
    while (plist[-1].lower().find(team.lower()) != -1):
        plist.pop()
    print(plist)
    
    return plist
 
  #  print(page_soup.select('span[class ="entry-bg mr-1"]'))

