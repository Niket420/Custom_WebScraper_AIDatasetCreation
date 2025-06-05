from pymongo import UpdateOne
from M3_storing_in_database import InitializeMongoDB
import os
import logging
logger = logging.getLogger(__name__)


def upsert_articles(article_dict, collection):
    """
    Upsert articles into MongoDB:
    - If news_article exists: update image_link
    - If not: insert new article
    
    Args:
        article_dict (dict): {news_article: image_link}
        collection (pymongo.collection.Collection): Your MongoDB collection
    """
    operations = [
        UpdateOne(
            {"news_article": article},
            {"$set": {"image_link": image_link}},
            upsert=True
        )
        for article, image_link in article_dict.items()
    ]

    if operations:
        result = collection.bulk_write(operations)
        logger.info("Data Added Successfully")
    else:
        logger.warning("No operations to perform. Please check the input data.")


if __name__=="__main__":
    # Assuming you already have a MongoDB collection initialized as `collection`
    db = InitializeMongoDB(os.getenv("MONGO_PASSWORD"),"Cluster0")
    collection = db.get_collection("articles")
    articles = {
        "RCB victory parade cancelled...": "https://news.google.com/xyz1.jpg",
        "YouTuber Jasbir Singh tried...": "https://news.google.com/xyz2.jpg"
    }

    upsert_articles(articles, collection)