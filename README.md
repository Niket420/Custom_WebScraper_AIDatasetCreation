# News Scrapper

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED)](https://www.docker.com/)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248)](https://www.mongodb.com/)

A modular Python scraper that collects Google News Top Stories headlines with image links and stores them in MongoDB using idempotent upsert operations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Docker](#docker)
- [Data Model](#data-model)
- [Logging](#logging)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project runs a simple ETL-style flow:

1. Discover the Top Stories page from Google News Home.
2. Extract headline and image URL pairs from article cards.
3. Write data to MongoDB with bulk upsert to prevent duplicates.

## Features

- Modular pipeline split into clear stages.
- Config-driven source URL and section identification.
- MongoDB bulk upsert for efficient writes.
- Dockerized runtime for reproducible execution.
- File-based logging for pipeline runs.

## Architecture

```text
Google News Home
       |
       v
M1_scrape_homePage.py  -> finds Top Stories URL
       |
       v
M2_scrape_news_img.py  -> extracts {headline: image_url}
       |
       v
M4_check_duplicate.py  -> bulk upsert operations
       |
       v
MongoDB (articles collection)
```

## Project Structure

```text
.
|-- config.py
|-- M1_scrape_homePage.py
|-- M2_scrape_news_img.py
|-- M3_storing_in_database.py
|-- M4_check_duplicate.py
|-- M5_main_orchestration.py
|-- requirements.txt
|-- Dockerfile
|-- .env (local, ignored by git)
`-- process.log
```

## Getting Started

### Prerequisites

- Python 3.9 or newer
- MongoDB instance (Atlas or self-hosted)
- Valid MongoDB connection URI

### Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Run Full Pipeline

```bash
python M5_main_orchestration.py
```

### Run Individual Stages

```bash
python M1_scrape_homePage.py
python M2_scrape_news_img.py
python M3_storing_in_database.py
python M4_check_duplicate.py
```

## Configuration

Core scraping settings are stored in `config.py`:

- `base_url`: base domain for URL joining
- `top_stories_identifier`: text key used to locate Top Stories link
- `url`: Google News home URL

Environment variables are loaded from `.env`.

Create `.env` in project root:

```env
MONGO_PASSWORD=<your_mongodb_connection_uri>
```

Important note:

- The main pipeline currently uses `MONGO_PASSWORD` as MongoDB URI.
- The standalone block in `M3_storing_in_database.py` uses `MONGO_DB_URL`.

For consistency, consider standardizing on a single variable name.

## Docker

Build image:

```bash
docker build -t news-scrapper .
```

Run container:

```bash
docker run --rm --env-file .env news-scrapper
```

## Data Model

Target collection: `articles`

Example document:

```json
{
  "news_article": "headline text",
  "image_link": "https://example.com/image.jpg"
}
```

Write behavior:

- If `news_article` exists, update `image_link`.
- If missing, insert as new document.

## Logging

Pipeline execution logs are written to `process.log` by `M5_main_orchestration.py`.

## Limitations

- HTML selectors are tightly coupled to current Google News markup.
- No retry, timeout tuning, or backoff strategy yet.
- Minimal exception handling around HTTP and parsing failures.
- No automated tests currently included.

## Roadmap

- Add retries and request timeouts.
- Add structured schema validation before writes.
- Add unit tests and integration tests.
- Add scheduler support (cron/Airflow).
- Export data to downstream analytics storage.

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes with clear messages.
4. Open a pull request with context and test notes.

If you are proposing larger changes, open an issue first to discuss scope.

## License

No license file is currently included in this project.

If you plan to open source this publicly, add a `LICENSE` file (for example MIT, Apache-2.0, or GPL-3.0) and update this section.
