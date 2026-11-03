# Startup Funding Analysis

An exploratory data analytics project analyzing Indian startup funding trends, investment patterns, sector-wise funding distribution, and investor activity using Python, SQL, and data visualization.

## Overview

Startup Funding Analysis is a data-driven analytical project that explores the Indian startup ecosystem through historical funding data. The project uses data cleaning, exploratory data analysis (EDA), SQL queries, and visualization techniques to identify investment patterns and understand how funding is distributed across different sectors, cities, and investors.

The system transforms raw startup funding records into meaningful insights, helping uncover investment trends and funding concentration within India's startup ecosystem.

The project provides:

* Startup funding trend analysis
* Sector-wise funding distribution
* Leading startup city identification
* Most active investor analysis
* Yearly funding trend visualization
* Data cleaning and preprocessing
* SQL-based analytical queries
* Exploratory Data Analysis (EDA)

---

## Features

### Data Cleaning & Preprocessing

The project processes raw startup funding data to improve data quality and consistency.

Key operations include:

* Handling missing values
* Cleaning inconsistent records
* Standardizing dataset fields
* Processing funding amount information
* Preparing structured datasets for analysis

### Sector-wise Funding Analysis

Identifies industries attracting the highest startup investments.

The analysis includes:

* Top-funded startup sectors
* Sector-wise funding distribution
* Investment concentration across industries

### Startup City Analysis

Examines the geographical distribution of startup investments across India.

The analysis identifies:

* Leading startup cities
* Cities attracting the highest funding
* Geographical concentration of startup investments

### Investor Analysis

Evaluates investor participation and funding activity.

The analysis includes:

* Most active investors
* Investor participation patterns
* Funding activity across the startup ecosystem

### Yearly Funding Trends

Analyzes historical funding patterns to understand changes in startup investments over time.

Key indicators include:

* Annual funding distribution
* Year-over-year funding patterns
* Changes in investment activity

### Data Visualization

The project uses graphical representations to make funding patterns easier to interpret.

Visualizations include:

* Top-funded startup cities
* Leading investors
* Top-funded sectors
* Yearly funding trends

---

## Dataset

**Dataset Source:** [Indian Startup Funding – Kaggle](https://www.kaggle.com/datasets/sudalairajkumar/indian-startup-funding)

The dataset contains historical Indian startup funding information, including:

* Startup names
* Industry sectors
* Investor information
* Funding amounts
* Startup locations
* Funding dates

The dataset serves as the foundation for exploratory analysis and SQL-based investigation.

---

## Technology Stack

### Programming & Data Analysis

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib

### Database & Querying

* SQL

### Development Tools

* VS Code
* Git
* GitHub

---

## Project Structure

```text
Startup-Funding-Analysis/
│
├── data/
│   ├── startup_funding.csv
│   └── cleaned_startup_funding.csv
│
├── sql/
│   ├── investors.sql
│   ├── top_cities.sql
│   ├── top_sectors.sql
│   └── yearly_fund.sql
│
├── visuals/
│   ├── top_cities.png
│   ├── top_investors.png
│   ├── top_sectors.png
│   └── yearly_funding.png
│
├── analysis.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/startup-funding-analysis.git
cd startup-funding-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Ensure the dataset is placed inside the `data/` directory.

Run the analysis:

```bash
python analysis.py
```

---

## SQL Analysis

The project uses SQL queries to investigate different dimensions of startup funding.

Analytical queries include:

* `investors.sql` – Identifies the most active investors.
* `top_cities.sql` – Analyzes startup funding across cities.
* `top_sectors.sql` – Identifies leading funded sectors.
* `yearly_fund.sql` – Examines annual funding trends.

---

## Exploratory Data Analysis

The EDA workflow focuses on identifying patterns, distributions, and relationships within the startup funding dataset.

Key analytical dimensions include:

* Funding distribution across industries
* Geographical investment concentration
* Investor participation
* Historical funding patterns

---

## Visualizations

The project generates visual representations of the analytical findings.

Add screenshots of:

* Top Startup Cities
* Top Investors
* Top Funded Sectors
* Yearly Funding Trends

---

## Future Enhancements

Planned improvements include:

* Interactive Power BI dashboard
* Advanced investor network analysis
* Startup funding prediction models
* Geographic funding distribution maps
* Industry-wise investment forecasting
* Year-over-year growth analysis
* Automated data ingestion pipeline
* Interactive filtering and reporting

---

## License

MIT License

Copyright (c) 2026 Startup Funding Analysis

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction.

---

## Author

Sudeep

Student • Builder • Aspiring Founder

---

## Acknowledgments

* Kaggle – Indian Startup Funding Dataset
* Python
* Pandas & NumPy
* Matplotlib
* SQL
* Open Source Community

Built to explore India's startup investment landscape through data analytics, SQL, and visualization.
