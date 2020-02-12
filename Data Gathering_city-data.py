# Data Gathering
## Webscraping: city-data.com

# imports
import pandas as pd
import requests

from bs4 import BeautifulSoup

# scraping
source = "http://www.city-data.com/nbmaps/neigh-Seattle-Washington.html#N11"

response = requests.get(source)

soup = BeautifulSoup(response.content, "lxml")

neighborhoods = soup.find_all("div", attrs = {"class": "neighborhood"})

# goal fields: area, population, median household income, median rent, average estimated value of detached homes

# thank you to Bennett Brown from Stack Overflow
# their participation helped me figure out how to isolate text between breaks
# link: https://stackoverflow.com/questions/16835449/python-beautifulsoup-extract-text-between-element

# filling anything that throws an error with None

hoods = []

for n in neighborhoods:
    hood = {}
    hood["neighborhood"] = n.find("span", attrs = {"class": "street-name"}).text

    try:
        hood["area"] = n.find_all("b")[0].next.next
    except:
        hood["area"] = None

    try:
        hood["population"] = n.find_all("b")[2].next.next
    except:
        hood["population"] = None

    try:
        tables = n.find_all("div", attrs = {"class": "hgraph"})
    except:
        pass

    try:
        table_income = tables[1]
        hood["median_income"] = table_income.find_all("td")[1].p.next
    except:
        hood["median_income"] = None

    try:
        table_rent = tables[2]
        hood["median_rent"] = table_rent.find_all("td")[1].p.next
    except:
        hood["median_rent"] = None

    try:
        table_house_val = tables[5]
        hood["avg_house_value"] = table_house_val.find_all("td")[1].p.next
    except:
        hood["avg_house_value"] = None

    hoods.append(hood)

df = pd.DataFrame(hoods)

# formatting
# casting everything as float for cases where None is in the column
df[["median_income", "median_rent", "avg_house_value"]] = df[["median_income", "median_rent", "avg_house_value"]].replace(to_replace = "\$", value = "", regex = True)

df["median_income"] = df["median_income"].replace(",", "", regex = True)

df["median_income"] = df["median_income"].astype("float")

df["population"] = df["population"].replace(",", "", regex = True)
df["population"] = df["population"].astype("float")

df["avg_house_value"] = df["avg_house_value"].replace(",", "", regex = True)
df["avg_house_value"] = df["avg_house_value"].astype("float")

df["median_rent"] = df["median_rent"].replace(",", "", regex = True)
df["median_rent"] = df["median_rent"].astype("float")

df["area"] = df["area"].astype("float")

df.to_csv("./datasets/city-data.csv", index = False)
