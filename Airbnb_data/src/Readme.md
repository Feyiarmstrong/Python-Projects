# Airbnb Data Deep Dive – Python & Pandas Analysis

## Project Overview

This project provides a comprehensive exploration and analysis of London Airbnb listings using Python and Pandas. The dataset is downloaded directly from Inside Airbnb’s online API, ensuring reproducibility and automation. The objective is to clean, enrich, and analyze the dataset to extract actionable insights about pricing, availability, room types, and host activity.

## The project demonstrates skills in:
 
 • Automated data fetching from public APIs
 
 • Data loading and inspection
 
 • Data cleaning and handling inconsistencies
 
 • Enrichment with calculated fields
 
 • Exploratory data analysis (EDA)
 
 • Modular and reusable Python code
 
 • Analytical reproducibility


## Project structure 

project-folder/

│

├─ data/

│   ├─ london_listing_raw.csv       # Raw dataset fetched from Inside Airbnb

│   ├─ london_listing_clean.csv     # Cleaned dataset

│   └─ cleaned_enriched.csv         # Enriched dataset with calculated fields

│

├─ src/

│   ├─ cleaner.py                   # Functions to clean the dataset

│   ├─ enricher.py                  # Functions to enrich dataset with calculated columns

│   └─ analyzer.py                  # Functions to load enriched dataset for analysis

│

├─ notebooks/

│   ├─ loading.ipynb                # Data fetching & initial inspection

│   ├─ cleaning.ipynb               # Data cleaning

│   ├─ enrichment.ipynb             # Dataset enrichment

│   └─ analysis.ipynb               # Exploratory data analysis and visualizations

│

└─ README.md


## Workflow

1. Data Loading (loading.ipynb)
 
 • The raw Airbnb dataset is fetched programmatically from the Inside Airbnb API.
 
 • Data is loaded directly into a Pandas DataFrame (df_raw) without manual download.
 
 • Initial inspection performed using .info(), .describe(), and .head().
 
 • Checks for duplicates and missing values conducted.


2. Data Cleaning (cleaning.ipynb)
 
 • Irrelevant columns such as license, scrape_id, neighbourhood_group_cleansed, and neighbourhood 
 removed.
 
 • Rows with zero price or zero availability eliminated.
 
 • Null values strategically retained to allow subsequent analysis.
 
 • Cleaned dataset saved as london_listing_clean.csv.

3. Data Enrichment (enrichment.ipynb)
 
 • Calculated price_per_booking = price × minimum_nights.
 
 • Availability categorized into:
 
 • Full-time (>300 days)
 
 • Part-time (100–300 days)
 
 • Rare (<100 days)
 
 • Enriched dataset saved as cleaned_enriched.csv.

4. Data Analysis (analysis.ipynb)
 
 • Enriched dataset loaded via analyzer.py.
 
 • Key questions addressed:
 
 • Top neighborhoods by average price
 
 • Average price and availability by room type
 
 • Hosts with the most listings
 
 • Borough-level price comparison
 
 • Listings without reviews
 
 • Visualizations created for clear interpretation.
 
 • Summary of key insights provided in markdown.

⸻

## Challenges and Resolutions
 
 • Data inconsistencies & missing values: Irrelevant columns removed; nulls retained strategically for review and availability analysis.
 
 • Notebook variable scope: Cleaned and enriched datasets saved as CSV files for accessibility across notebooks.
 
 • Column count discrepancies: Columns verified before saving; index=False used in to_csv() to preserve all columns.
 
 • Reproducible pipeline: Dataset is fetched automatically from API and processed through modular functions.

⸻

## Key Insights

 • Most expensive neighborhoods: City of London, Lambeth, Kensington and Chelsea.
 
 • Entire home/apartments have higher average price and availability compared to private rooms.
 
 • A few hosts control a significant portion of listings.
 
 • Numerous listings have never been reviewed, indicating inactive or new listings.
 
 • Most listings fall into Full-time or Part-time availability categories.

⸻

## Technologies Used
 
 • Python (3.x)
 
 • Pandas
 
 • Jupyter Notebook
 
 • Matplotlib / Seaborn for visualization
 
 • Requests and gzip for automated data fetching



## Usage Instructions

 1. Clone the repository.
 
 2. Install required dependencies:


pip install pandas matplotlib seaborn requests

3. Execute notebooks in order:

• loading.ipynb 

→ cleaning.ipynb 

→ enrichment.ipynb 

→ analysis.ipynb

 4. Explore outputs, visualizations, and derived insights.
