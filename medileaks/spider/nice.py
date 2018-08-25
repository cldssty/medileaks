# -*- coding: utf-8 -*-
"""Scraping function for NICE.
   Given a medical procedure given by the user,
   the scraper goes through this webpages and looks for pages that contain this keyword. 

   Source url: https://www.nice.org.uk/guidance/ng87/chapter/Recommendations. 
"""
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from multiprocessing import Pool
from scrapers import get_scraper

def simple_get(url):
    """Attempts to get the content at `url` by making an HTTP GET request.
    
    Args:
        url (string): Webpage to be scraped.
       
    Returns:
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content 
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """Attempts to get the content at `url` by making an HTTP GET request.
    
    Args:
        resp (string): Webpage to be scraped.
       
    Returns:
        bool: HTML or not. Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    print(e)


def get_raw_best_practices(url):
    """Downloads the page where the list of best practices is found.

    Args:
        url (string): Webpage to be scraped.
       
    Returns:
        list: Best practices. Returns list of html elements containing best practices.
    """
    response = simple_get(url)
    raw_best_practices = set()

    if response is not None:
        soup = BeautifulSoup(response, 'html.parser')
        start_at = soup.find('a', id='recommendations') 
        stop_at = soup.find('div', class_='section', title='Terms used in this guideline.') 
        while stop_at != start_at: 
            raw_best_practices.add(start_at.get_text(strip=True)) 
            start_at = start_at.find_next() 
        return list(raw_best_practices)

    return response