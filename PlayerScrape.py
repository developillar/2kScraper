import bs4
import csv
import os
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

def scrape_Player(player_name):
     
    # player_name = input("Enter the name of a player: ")
    pname = player_name.replace(' ', '-')
    my_url = 'https://www.2kratings.com/' + pname
    headers = {"User-Agent": "Chrome"}
####
    request = Request(my_url, headers = headers)
    page_html = urlopen(request).read()
    page_soup = soup(page_html, "html.parser")

    containers = page_soup.findAll("li", {"class":"mb-1"})
    a_list = []
    i = -1
    for container in containers:
     a_list.append(container.get_text())

    ###fix list

    del a_list[36:46]
    idef = a_list[26][0:19]
    a_list[26] = idef
    # a_list.extend([idef, pdef, stl, blk, latq, helpd, passp]
    # i = 0
    # for att in a_list:
    #     i= i+1
    #     print(str(i) +" " + att)
    player = [player_name] + a_list
    csv_head = "Name, Close_shot, Mid-Range_shot, Three-Point_Shot, Free_Throw, Shot_IQ, Offensive_Consistency, Speed, Acceleration, Strength, Vertcal, Stamina, Hustle, Overall_Durability, Layup, Standing_Dunk, Driving_dunk, Post_Hook, Post_Fade, Post_Control, Draw_Foul, Hands, Pass_accuracy, Ball_handle, Speed_with_Ball, Pass_IQ, Pass_Vision, Interior_Defense, Perimeter_defense, Steal, Block, Lateral_Quickness, Help_Defense_IQ, Pass_Perception, Defensive_Consistency, Offensive_Rebound, Defensive_Rebound\n"
    filename = "Players.csv"
    f = open(filename,"a", newline="")
    fileEmpty = os.stat(filename).st_size == 0
    if fileEmpty:
        f.write(csv_head)
    write= csv.writer(f)
    write.writerow(player)
    f.close()
    print("Adding " + player_name)

    

    
