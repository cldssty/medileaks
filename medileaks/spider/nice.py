# -*- coding: utf-8 -*-
"""Scraping function for NICE.
   Given a medical procedure given by the user,
   the scraper goes through this website and look for pages that contain this keyword. 

   Basically need best practices from https://www.nice.org.uk/guidance/ng87/chapter/Recommendations

   Todo:
        Will actually need a different page for a different user_input. Will add that later. 
        Because the html structure of all the recommendation pages are the same within this website, 
        we just need to store a page for each medical condition in a database, and then do a simple query 
        for the right page given a user input. 
"""
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from multiprocessing import Pool
from scrapers import get_scraper

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
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
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def get_raw_best_practices(url):
    """
    Downloads the page where the list of best practices is found
    and returns the html element containing those best practice.
    """
    url = url
    response = simple_get(url)

    if response is not None:
        soup = BeautifulSoup(response, 'html.parser')
        start_at = soup.find('a', id='recommendations') 
        stop_at = soup.find('div', class_='section', title='Terms used in this guideline.') 
        raw_best_practices = set()
        while stop_at != start_at: 
            raw_best_practices.add(start_at.get_text(strip=True)) 
            start_at = start_at.find_next() 
        return list(raw_best_practices)

    raise Exception('Error retrieving contents at {}'.format(url))
