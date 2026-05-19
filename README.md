 ````markdown
# Startup Funding Analysis

## Project Overview

This project analyzes Indian startup funding trends using Python, SQL, and data visualization techniques.  
The goal was to identify:

- Top funded sectors
- Leading startup cities
- Most active investors
- Yearly funding trends

The project uses real-world startup funding data and demonstrates:
- Data cleaning
- Exploratory Data Analysis (EDA)
- SQL querying
- Data visualization

---

## Dataset

Dataset Source:

https://www.kaggle.com/datasets/sudalairajkumar/indian-startup-funding

Dataset contains:
- Startup names
- Industry sectors
- Investors
- Funding amounts
- Cities
- Funding dates

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- SQL
- VS Code
- Git & GitHub

---

## Project Structure

```text
startup_pred/
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
````

---

## Data Cleaning Steps

* Removed duplicate records
* Converted funding amounts to numeric format
* Handled missing values
* Cleaned column names
* Converted dates into datetime format
* Extracted yearly funding information

---

## SQL Analysis

The following SQL queries were created:

### 1. Top Funded Sectors

* Identifies sectors receiving highest funding

### 2. Top Startup Cities

* Identifies cities with highest startup investments

### 3. Investor Analysis

* Finds most active investors

### 4. Yearly Funding Trend

* Tracks startup funding growth over time

---

## Visualizations

### Yearly Funding Trend

Shows startup investment growth across years.

### Top Funded Sectors

Highlights industries attracting highest capital.

### Top Startup Cities

Shows major startup ecosystems.

### Investor Analysis

Displays most active investors by funding volume.

---

## Key Insights

* Bengaluru emerged as the leading startup hub.
* E-Commerce and FinTech attracted major investments.
* Startup funding significantly increased after 2017.
* A small number of investors dominated multiple funding rounds.

---

## How to Run

### Clone Repository

```bash
git clone <your-repository-link>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Analysis

```bash
python3 analysis.py
```

---

## Future Improvements

* Build interactive Power BI dashboard
* Add machine learning prediction models
* Perform startup success prediction
* Add investor network analysis

---

## Author
Sudeep

```
```
