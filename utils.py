import os
import sys
import time
import urllib
from bs4 import BeautifulSoup
from flickrapi import FlickrAPI
from credential import KEY, SECRET

class Scraping():
    def __init__(self, KEY, SECRET):
        self.KEY = KEY
        self.SECRET = SECRET
        self.flickr = FlickrAPI(KEY, SECRET, format='parsed-json')
        return self.flickr


    def search_image(self, search_word, amount=200,media='photos', sort='relevance', safe_search=1, extras='url_q, licence'):
        result = flickr.photos.search(
            text = search_word,
            per_page = amount,
            media = media,
            sort = sort,
            safe_search = safe_search,
            extras = extras
        )
        return result
