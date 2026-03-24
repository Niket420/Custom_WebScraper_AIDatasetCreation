
# AI Dataset Creation Pipeline (Web Scraper)

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Database-MongoDB-green?style=flat-square" />
  <img src="https://img.shields.io/badge/Architecture-Modular-black?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Production--Ready-success?style=flat-square" />
</p>





## Overview

A production-style data pipeline that scrapes Google News to generate a continuous stream of:

<image, caption>

tuples for multimodal AI training.

This is not just scraping — it’s a mini data engineering system built with modularity, scalability, and automation in mind.



## Core Features
	•	 Dynamic scraping (no hardcoded URLs/selectors)
	•	 Lazy loading handling (real-world DOM behavior)
	•	 Modular pipeline architecture
	•	 Database storage with structured schema
	•	 Intelligent deduplication
	•	 Cron-job ready orchestration
	•	 Logging for monitoring & debugging



## Architecture

Google News
   ↓
Homepage Scraper
   ↓
Top Stories Extractor
   ↓
Image + Headline Extraction
   ↓
Deduplication Engine
   ↓
MongoDB Storage
   ↓
Continuous Pipeline Execution








## Tech Stack

Backend
	•	Python

Web Scraping
	•	BeautifulSoup
	•	Requests

Database
	•	MongoDB

System Design
	•	Modular Pipeline
	•	Config-driven architecture
	•	Logging + Orchestration



## Quick Start

1. Clone the repo

git clone <your-repo-url>
cd Custom_WebScraper_AIDatasetCreation




2. Install dependencies

pip install -r requirements.txt




3. Configure parameters

Edit:

config_news_data.py




4. Run the pipeline

python M5_main_orchestration.py




 Automation (Cron Job)

*/30 * * * * python /path/to/M5_main_orchestration.py




## Output Format

{
  "headline": "string",
  "image_url": "string",
  "article_url": "string",
  "timestamp": "datetime",
  "metadata": {}
}




## Design Decisions
	•	No hardcoded selectors → resilient to UI changes
	•	Separation of concerns → easy debugging
	•	Database-first approach → scalable storage
	•	Logging layer → production readiness



## Future Improvements
	•	Async scraping (faster throughput)
	•	Kafka-based pipeline
	•	Image download + preprocessing
	•	Dataset versioning
	•	Quality scoring for captions

ics (even fake but realistic)

That’s how you make recruiters pause.
