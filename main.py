import requests
from bs4 import BeautifulSoup

website = "https://ponisha.ir"
url = "https://ponisha.ir/search/projects"
params = {
    "page": 1,
    "order": "approved_at|desc",
    "category": 3,
    "promotion": "-",
    "filterByProjectStatus": "open"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0 Safari/537.36"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code != 200:
    print("Failed to fetch the page:", response.status_code)
    exit()

html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

jobs = soup.find_all("a",class_="MuiBox-root css-f8mog2")

for job in jobs[::2][:3]:
    title = job.get_text(strip=True)
    link = website + job["href"]
    print(f"{title}\n{link}\n")
