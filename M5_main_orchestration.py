import logging
import os
from M1_scrape_homePage import scrape_top_stories_link
from M2_scrape_news_img import get_img_and_news
from M3_storing_in_database import InitializeMongoDB
from M4_check_duplicate import upsert_articles
from news_scrapper.config_news_data import CONFIG
import dotenv
dotenv.load_dotenv()
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',filename='process.log',encoding='utf-8')
logger = logging.getLogger(__name__)




if __name__=="__main__":
    get_top_stories_link = scrape_top_stories_link(CONFIG["scrapping_website"]["url"],CONFIG["scrapping_website"]["top_stories_identifier"])


    news_img_dict = get_img_and_news(get_top_stories_link)

    password = os.getenv("MONGO_PASSWORD")
    db = InitializeMongoDB(password,"Cluster0")
   
    collection = db.get_collection("articles")

    upsert_articles(news_img_dict, collection)
    logger.info("Process Completed Successfully")