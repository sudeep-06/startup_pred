import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/startup_funding.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

df = df.drop_duplicates()

df.columns = df.columns.str.strip().str.replace(' ', '_')

df['Date_dd/mm/yyyy'] = pd.to_datetime(
    df['Date_dd/mm/yyyy'],
    errors='coerce')
df['Year'] = df['Date_dd/mm/yyyy'].dt.year

df['Amount_in_USD'] = (
    df['Amount_in_USD']
    .astype(str)
    .str.replace(',', '')
    .str.replace('+', '')
    .str.replace('Undisclosed', ''))
df['Amount_in_USD'] = pd.to_numeric(
    df['Amount_in_USD'],
    errors='coerce')
df = df.dropna(subset=['Amount_in_USD'])

top_sectors = (
    df.groupby('Industry_Vertical')['Amount_in_USD']
    .sum()
    .sort_values(ascending=False)
    .head(10))
print(top_sectors)

top_cities = (
    df.groupby('City_Location')['Amount_in_USD']
    .sum()
    .sort_values(ascending=False)
    .head(10))
print(top_cities)

yearly_funding = (
    df.groupby('Year')['Amount_in_USD']
    .sum())
print(yearly_funding)
yearly_funding.plot(kind='bar', figsize=(10,5))

plt.title("Yearly Startup Funding")
plt.xlabel("Year")
plt.ylabel("Funding Amount")
plt.savefig("visuals/yearly_funding.png")
top_sectors.plot(kind='bar', figsize=(12,6))

plt.title("Top Funded Sectors")
plt.xlabel("Sector")
plt.ylabel("Funding")

plt.savefig("visuals/top_sectors.png")

top_cities.plot(kind='bar', figsize=(12,6))

plt.title("Top Startup Cities")
plt.xlabel("City")
plt.ylabel("Funding")

plt.savefig("visuals/top_cities.png")

top_investors = (
    df.groupby('Investors_Name')['Amount_in_USD']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_investors.plot(kind='bar', figsize=(12,6))

plt.title("Top Investors")
plt.xlabel("Investor")
plt.ylabel("Total Funding")

plt.savefig("visuals/top_investors.png")
df.to_csv("data/cleaned_startup_funding.csv", index=False)