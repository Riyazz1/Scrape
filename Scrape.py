import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

session = requests.Session()
session.headers.update(headers)
sub=input("Enter the name of subreddit whose username you want to scrape: ")

url = f"https://old.reddit.com/r/{sub}/"
all_usernames = []

after = None  
pages=int(input("ENTER HOW MANY PAGES YOU WANT TO SCRAPE(Enter higher number for more results): "))

for page in range(pages):  
    params = {"after": after} if after else {}
    r = session.get(url, params=params)
    print(f"Page {page+1} - Status: {r.status_code}")

    soup = BeautifulSoup(r.text, "html.parser")

    # Get usernames
    unames = soup.find_all("a", class_="author")
    for u in unames:
        all_usernames.append(u.text)
        print(u.text)

  
    next_btn = soup.find("span", class_="next-button")
    if next_btn:
        after = next_btn.find("a")["href"].split("after=")[-1]
    else:
        print("No more pages")
        break

print(f"\nTotal usernames: {len(all_usernames)}")