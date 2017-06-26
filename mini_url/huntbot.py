# -*- coding: utf-8 -*-
import os
import re
import requests
import pygsheets
from bs4 import BeautifulSoup as Bs

SEARCH_PAGE = 'http://www.pap.fr/annonce/vente-appartements-paris-75-g439g43308g43313g43335g43339-du-studio-au-2-pieces'
SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/1OkqYB9Z4rHIYLZXjwboV_v0BmBSKWtn6_gVGFw1CDF8/edit?usp=sharing'
URL_DOMAIN = 'http://www.pap.fr'

PAGINATION_SELECTOR = '.pagination li a'
LISTING_DETAIL_BTN_SELECTOR = '.btn-details'
NEXT_PAGE_SELECTOR = '.next'
GEOLOC_SELECTOR = '.item-geoloc'
SPECS_SELECTOR = '.item-summary'
DESCRIPTION_SELECTOR = '.item-description'
METRO_SELECTOR = '.item-metro .label'
PRICE_SELECTOR = '.price'

def process_listings_page(link)
  try:
    res = requests.get(link)
    dom = Bs(res.text, 'lxml')
    
    #details_urls = [
      #URL_DOMAIN + btn.get('href')
      #for btn in dom.select('.btn-details')
    #]
    
    details_urls = []
    
    details_btn = dom.select('.btn-details')
    
    for btn in list_of_details_btn:
      details_relative_url = btn.get('href')
      details_absolute_url = URL_DOMAIN + details_relative_url
      
      details_urls.append(details_absolute_url)
    
    return [
      process_listing(listing_details_url)
      for listing_details_url in details_urls
    ]
  except Exception as e:
    print(e)
    
    
def process_listing(listing):
  res = requests.get(listing)
  dom = Bs(res.text, 'lxml')
  
  specs = ' / '.join([
    clean_spaces(
      clean_markup(
        str(li).replace('<strong>': ': ').lower()
      )
    )
    for li in dom.select(SPECS_SELECTOR)[0].select('li')
  ])
  
  metro = ', '.join([
    clean_markup(elm.get_text())
    for elm in dom.select(METRO_SELECTOR)
  ])
  
  location = dom.select(GEOLOC_SELECTOR)[0].h2.text
  
  description_body = dom.select(DESCRIPTION_SELECTOR)[0]
  description = clean_spaces(description_body.get_text())
  
  price = dom.select(PRICE_SELECTOR)[0].text
  
  return {
    "specs": specs,
    "location": location,
    "description": description,
    "metro": metro,
    "url": listing,
    "price": price
  }


def clean_special_chars(string):
  """ remove special characters """
  return string.replace('²', '2').replace('€', 'e')


def clean_markup(string):
  string = clean_special_chars(string)
  return re.sub(r'<[^>]*>', '', string)

def clean_spaces(string):
  string = re.sub('\n|\r|\r|\t', ' ', string)
  return re.sub('\s{2,}', ' ', string).strip()


try:
  gc = pygsheets.authorize(service_file='credentials.json')
  
  sheet = gc.open_by_url(SPREADSHEET_URL).sheet1
  
  res = requests.get(SEARCH_PAGE)
  dom = Bs(res.text, 'lxml')
  
  
  links = [SEARCH_PAGE] + [
    URL_DOMAIN + a.get('href')
    for a in dom.select(PAGINATION_SELECTOR)
  ]
  
  links = []
  
  links.append[SEARCH_PAGE]
  
  paginated_links = dom.select(PAGINATION_SELECTOR)
  
  for a in paginated_links:
    relative_url = a.get('href')
    absolute_url = a.get('href')
    links.append(absolute_url)
    
  urls_stored = sheet.get_col(5)
  
  for link in links:
    for ls in process_listings_page(link):
      if ls['url'] not in urls_stored:
        sheet.insert_rows(row=0, values=[
          ls['specs'], ls['price'], ls['location'], 
          ls['description'], ls['metro'], ls['url'],
        ])
  
  
except Exception as e:
  print(e)
  
  

