import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging
from config import CONFIG
import logging
logger = logging.getLogger(__name__)





def scrape_top_stories_link(url,key_string=CONFIG["scrapping_website"]["top_stories_identifier"]):
    page = requests.get(url)
    html_doc = page.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    top_stories_link = None

    for link in soup.find_all('a'):
        if key_string.lower() in link.text.lower():
            top_stories_link = link.get('href')
            top_stories_link = urljoin(CONFIG["scrapping_website"]["base_url"],top_stories_link)

        if top_stories_link:
            logger.info(f'scrapped top stories link :{top_stories_link}')
            break
    
    if not top_stories_link:
        logger.error('Unable to find the top stories link')

    return top_stories_link





if __name__=="__main__":
    url = CONFIG["scrapping_website"]["url"]
    key_string = CONFIG["scrapping_website"]["top_stories_identifier"]
    top_stories_link = scrape_top_stories_link(url,key_string)
    print(f"top_stories_link : {top_stories_link}")