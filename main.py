from PlayerScrape import *
from TeamScrape import *

print("2k Scraper Tool")

user_input = ""

while user_input != 'q' or user_input != 'Q':
    user_input = input("Team or Player? Enter 'T' or 'P'. 'Q' to quit: ")
    if (user_input == "T" or user_input == 't'):
        plist = scrape_Team()
        for p in plist:
            scrape_Player(p)
        print("Done!")
    elif (user_input == 'P' or user_input =='p'):
        name = input("Enter a Player's name:")
        scrape_Player(name)
        print("Done!")
    elif (user_input == 'Q' or user_input == 'q'):
        print("Bye-bye!")
        break