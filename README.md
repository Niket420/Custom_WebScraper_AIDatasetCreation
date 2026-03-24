# Custom Web Scraper for AI Dataset Creation

A modular, production-oriented data pipeline that scrapes Google News to generate a continuous stream of <image, caption> tuples, suitable for training image captioning and multimodal AI systems.


## Overview

This project implements a scalable and configurable web scraping pipeline designed to automatically collect and store news data as structured datasets.

The system:
	•	Scrapes Google News dynamically (no hardcoded URLs)
	•	Extracts top stories, including headlines and thumbnails
	•	Handles lazy loading
	•	Stores structured data in a database
	•	Ensures deduplication
	•	Runs as an automated pipeline (cron-friendly)

## Motivation

Inspired by datasets like Flickr30k, this project builds a custom data generation pipeline for real-world multimodal AI applications.

Instead of static datasets, this system creates a live, continuously updating dataset — a much more realistic setup for modern AI systems.



## Architecture

The pipeline follows a modular design:

Google News → Homepage Scraper → Top Stories Extractor 
→ Data Extraction (Image + Headline)
→ Deduplication → Database Storage
→ Continuous Pipeline Execution

As described in the assignment workflow (see page 1 diagram)  ￼, the system continuously processes and stores <thumbnail, headline> pairs.


##  Project Structure

Google News 
   → Homepage Scraper 
      → Top Stories Extractor 
         → Data Extraction (Image + Headline) 
            → Deduplication 
               → Database Storage 
                  → Continuous Pipeline Execution



##  Key Features

1. Fully Configurable Scraping
	•	No hardcoded URLs or selectors
	•	Easily adaptable to layout changes

2. Lazy Loading Handling
	•	Handles dynamically loaded content
	•	Ensures complete data extraction

3. Modular Design

Each module is independently testable:
	•	Scraping
	•	Extraction
	•	Storage
	•	Deduplication
	•	Orchestration

4. Database Integration
	•	Stores:
	•	Images (or references)
	•	Headlines
	•	Metadata (timestamps, URLs, etc.)
	•	Designed for scalability

5. Intelligent Deduplication
	•	Prevents redundant entries
	•	Can be extended beyond naive headline matching

6. Production-Ready Orchestration
	•	Central pipeline runner
	•	Logging for debugging and monitoring
	•	Easily schedulable via cron jobs



## Tech Stack
	•	Python
	•	BeautifulSoup / Requests (or similar scraping tools)
	•	Database: PostgreSQL / MongoDB / MariaDB (configurable)
	•	Logging & Config-based architecture



##  How to Run

1. Install Dependencies

pip install -r requirements.txt

2. Configure Parameters

Update:

config_news_data.py

You can change:
	•	Base URLs
	•	Selectors
	•	Database configs



3. Run Pipeline

python M5_main_orchestration.py




4. (Optional) Automate with Cron

crontab -e

Example:

*/30 * * * * python /path/to/M5_main_orchestration.py




## Output

The system continuously generates structured data:

{
  "headline": "...",
  "image_url": "...",
  "article_url": "...",
  "timestamp": "...",
  "metadata": {...}
}

This can directly be used for:
	•	Image captioning datasets
	•	Multimodal LLM training
	•	News intelligence systems



## Design Highlights
	•	Built for robustness against UI changes
	•	Designed with real-world scraping challenges in mind
	•	Separation of concerns → easy debugging & extension
	•	Suitable for scaling into data engineering pipelines



## Future Improvements
	•	Add async scraping (faster pipeline)
	•	Integrate message queues (Kafka / RabbitMQ)
	•	Add image downloading & preprocessing
	•	Build dataset versioning system
	•	Add evaluation metrics for dataset quality

