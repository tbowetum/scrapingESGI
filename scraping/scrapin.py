import requests
from bs4 import BeautifulSoup as bs
#import streamlit as st
import pymongo
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

def get_soup():
    for x in range(1, 5):
        page = requests.get(f'https://www.marmiton.org/recettes?type=platprincipal&page={x}')
        soup = bs(page.text, "lxml")
        return soup

################"get all links#############################################
def get_links(soup):
    links = []
    homePages = soup.find_all("div", {"class": "recipe-card"})
    for homePage in homePages:
        href_tags = homePage.find("a").get('href')
        links.append(href_tags)
    return links

#print(len(get_links(get_soup())))
###########get our recipe###################################################
def recipe(links):
    recipes = []
    for link in links:
        res = requests.get(link, headers=headers)
        soup = bs(res.content, 'lxml')

        title = soup.find('h1', class_="main-title show-more").text.strip()

        items = soup.find_all('span', class_="ingredient-name show-icon")
        ingredient = []
        for i in items:
            ingredient.append(i.getText().strip())

        # steps = []
        # Cooking_steps = soup.find_all('div', class_="recipe-step-list__container")
        # for i in Cooking_steps:
        # steps.append(i.getText().strip())
        recipe = {
            'title': title,
            'ingredient': ingredient
        }
        recipes.append(recipe)
    return recipes
####################################################################################
    # for i in steps:
    # i.replace('\n','')

soup = get_soup()
links=get_links(soup)
#print(len(links))
recipes = recipe(links)
a = json.dumps(recipes, indent = 4)
l = json.loads(a)

#####################################################################################
#myclient = pymongo.MongoClient('mongod',27017)
#db = myclient["projet"]
#collection=db["Nosql"]
#collection.insert_many(l)

#cur = collection.find({})
#for res in cur:
    #print(res)

#u = 'poivre'
#test = searcheAllergie(cur, u)


#print(test)