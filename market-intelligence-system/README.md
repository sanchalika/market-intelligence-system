# README.md
# Market Intelligence System


## Overview
This project collects and analyzes tweets related to the Indian stock market in real-time, generating trading signals from social sentiment.


### Features
- Scrape tweets with hashtags (#nifty50, #sensex, #intraday, #banknifty) using `snscrape`
- Clean and normalize text, handle Unicode & Indic scripts
- Store data in Parquet format with deduplication
- Extract features (TF-IDF, embeddings, sentiment)
- Provide REST API with FastAPI
- Interactive dashboard with Streamlit


### Quickstart
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt


# Run sample demo
streamlit run src/dashboard/streamlit_app.py
uvicorn src.api.app:app --reload
```


### Data Schema
- tweet_id, username, created_at, content
- hashtags, mentions
- retweets, likes
- sentiment, tfidf, embedding


### Disclaimer
Scraping X/Twitter may violate its Terms of Service. This repo uses `snscrape` for educational/demo purposes only.


---


# docs/TECHNICAL.md
# Technical Documentation


## Architecture
Collector → Processor → Storage → API/Dashboard.


### Collector
- Uses `snscrape` to fetch tweets for defined hashtags
- Rate limiting handled with sleep intervals


### Processing
- Unicode normalization (NFKC)
- Language detection for Indic/English
- TF-IDF vectorization (sparse)
- Sentence embeddings (SBERT multilingual)
- Sentiment scores via lexicon/ML


### Storage
- Parquet files with Snappy compression
- Partitioned by date
- Deduplication on `tweet_id`


### Analysis
- Signals: sentiment + engagement + topic relevance
- Aggregation with weighted sum and bootstrap confidence intervals


### Scalability
- For larger scale, replace collector with Kafka producers
- Spark/Dask for batch feature extraction
- Vector DB (Milvus, Pinecone) for embeddings
- Store on cloud object store (S3/GCS)


---