import logging
from M1_scrape_homePage import scrape_top_stories_link
from config import CONFIG
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging

logger = logging.getLogger(__name__)


def get_img_and_news(url):
    page = requests.get(url)
    html_doc = page.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    img_news_dict = {}

    for article in soup.find_all("article"):
        img_url = article.find("img")
        link = img_url.get("srcset")[:img_url.get("srcset").index(" ")] if img_url else None

        if "faviconV2" in  link:
            continue
        final_link = urljoin(CONFIG["scrapping_website"]["base_url"], link)

        headline_tag = article.find('a', class_='gPFEn')

        if headline_tag:
            headline = headline_tag.get_text(strip=True)
            img_news_dict[headline] = final_link
    logger.info("Successfully,scrapped the image and news")
    return img_news_dict
   

  
if __name__=="__main__":
    
    # url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    url =CONFIG["scrapping_website"]["url"]
    url = scrape_top_stories_link(url)
    result = get_img_and_news(url)
    print(len(result), "news headlines found with images.")
    for i in result:
        print(f"Headline: {i}\nImage URL: {result[i]}\n{'-'*30}")




