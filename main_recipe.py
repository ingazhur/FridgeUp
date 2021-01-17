from bs4 import BeautifulSoup
import requests
from Hackdavis import allrecipes, simplyrecipes, marthastewart, epicurious, tasty
import time

# name, type, ingredients, url
types = ["soup", "vegetarian", "poultry", "beef", "pork", "fish", "pasta",
         "breakfast", "lunch", "dinner", "dessert"]
pantry = []

def enter_pantry():
    print("Add items to your virtual fridge. Press enter after each ingredient, and enter 0 when you want to stop.")
    entry = input().lower()
    while entry != '0':
        pantry.append(entry)
        entry = input().lower()
    return pantry #list

def del_pantry():
    print("Delete items from your pantry. Press enter after each ingredient, and enter 0 when you want to stop.")
    entry = input().lower()
    while entry != '0':
        pantry.remove(entry)
        entry = input().lower()
    return pantry

def search_allrecipes(): #include up to 4 ingredients
    websites = []
    str = ""
    for item in pantry:
        str += item + ","
    str = str[:-1]
    try:
        for type in types:
            # link = requests.get("https://www.allrecipes.com/search/results/?wt="+type+"&sort=re") #"&page=1"
            link = requests.get("https://www.allrecipes.com/search/results/?wt="+type+"&ingIncl="+str+"&sort=re")
            soup = BeautifulSoup(link.text, 'lxml')
            urls = soup.find_all(class_='fixed-recipe-card__h3') #list of size 1
            for i in range(len(urls)):
                websites.append(urls[i].find_all('a')[0].get('href'))
        websites = set(websites)
        websites = list(websites)
        return websites
    except:
        return ""

def search_simplyrecipes(): #website doesn't work for some reason
    websites = []
    str = ""
    for item in pantry:
        str += item + "+"
    str = str[:-1]
    try:
        link = requests.get("https://www.simplyrecipes.com/?s="+str)
        soup = BeautifulSoup(link.text, 'lxml')
        urls = soup.find_all(class_='entry-list') #list size 1
        urls = urls[0].find_all('li')
        for i in range(len(urls)):
            websites.append(urls[i].find_all('a')[0].get('href'))
        websites = set(websites)
        websites = list(websites)
        return websites
    except:
        return ""

def search_marthastewart():
    websites = []
    str = ""
    for item in pantry:
        str += item + "+"
    str = str[:-1]
    try:
        link = requests.get("https://www.marthastewart.com/search?q=" + str)
        soup = BeautifulSoup(link.text, 'lxml')
        urls = soup.find_all(class_='search-result')
        for i in range(len(urls)):
            websites.append(urls[i].find('a').get('href'))
        websites = set(websites)
        websites = list(websites)
        return websites
    except:
        return ""

def search_epicurious():
    websites = []
    str = ""
    for item in pantry:
        str += item + "%2C"
    str = str[:-3]
    try:
        link = requests.get('https://www.epicurious.com/search/?include=' + str)
        soup = BeautifulSoup(link.text, 'lxml')
        urls = soup.find_all(class_='show-quick-view') #list of multiple items
        for i in range(len(urls)):
            websites.append("https://www.epicurious.com/" + urls[i].get('href'))
        websites = set(websites)
        websites = list(websites)
        return websites
    except:
        return ""

def search_tasty():
    websites = []
    str = ""
    for item in pantry:
        str += item + "%20"
    str = str[:-3]
    try:
        link = requests.get('https://www.tasty.co/search?q=' + str)
        soup = BeautifulSoup(link.text, 'lxml')
        urls = soup.find_all(class_='feed-item')  # list of multiple items
        for i in range(len(urls)):
            websites.append("https://www.tasty.co/" + urls[i].get('href'))
        websites = set(websites)
        websites = list(websites)
        return websites
    except:
        return ""

if __name__ == "__main__":
    enter_pantry()
    # print('\n\n\n\n')
    # time.sleep(2)
    # print('FridgeUp will show you personalized recipe suggestions based on the food you have!')
    # time.sleep(5)
    # print('\n\nBy web scraping from popular recipe websites, FridgeUp gives you a list of recipes.')
    # time.sleep(11)
    # print("\n\nFridge:")
    # time.sleep(1)
    # pantry = ['cheese', 'bread', 'tomatoes', 'mustard']
    # for food in pantry:
    #     print(food)
    #     time.sleep(1.2)
    print("\n\nHere are some recipe suggestions based on the food in your fridge!\n")
    for website in search_allrecipes(): #has most websites
        a = allrecipes.Allrecipes(website)
        if a.find_name() != "Not available" and a.find_ingredients() != "Not available":
            print(a.find_name() + ": " + a.find_url())
    for website in search_simplyrecipes(): #not reliable website
        s = simplyrecipes.Simplyrecipes(website)
        if s.find_name() != "Not available" and s.find_ingredients() != "Not available":
            print(s.find_name() + ": " + s.find_url())
    for website in search_marthastewart(): #most reliable but not always recipes
        m = marthastewart.Marthastewart(website)
        if m.find_name() != "Not available" and m.find_ingredients() != "Not available":
            print(m.find_name() + ": " + m.find_url())
    for website in search_epicurious():
        e = epicurious.Epicurious(website)
        if e.find_name() != "Not available" and e.find_ingredients() != "Not available":
            print(e.find_name() + ": " + e.find_url())
    for website in search_tasty():
        t = tasty.Tasty(website)
        if t.find_name() != "Not available" and t.find_ingredients() != "Not available":
            print(t.find_name() + ": " + t.find_url())


'''
Outline:
-program that web scrapes from 4 recipe websites
-user inputs ingredients
-program finds recipes based on those ingredients
Weaknesses:
-limited number of websites (3-4)
-takes a long time depending on number of recipes
-recipe ingredients may include other ingredients not in pantry
-may not include every single ingredient if ingredients are very different
'''