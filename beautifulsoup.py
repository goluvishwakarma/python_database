import requests
from bs4 import BeautifulSoup
import pandas as pd


# url = "https://www.moneycontrol.com/company-notices/reliance-industries/notices/RI"
soup = BeautifulSoup(res.txt, "html.parser")

data = []
for ctag in soup.select("li ctag"):
    data.append(
        {
            "title": ctag.find_next("a").get_text(strip=True),
            "date": ctag.find_next(text=True).rsplit(maxsplit=1)[0],
            "desc": ctag.find_next("p", class_="MT2").get_text(strip=True),
        }
    )

df = pd.DataFrame(data)
print(df)