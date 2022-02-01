import time
import requests


def requests_toppage():
    toppage_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    response = requests.get(toppage_url)
    dic = response.json()
    for i in dic:
        try:
            response2 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty").json()
            print("title :" + response2["title"])
            print("Link :" + response2["url"])

            time.sleep(1)
        except KeyError:
            pass
    return 0


def main():
    requests_toppage()


if __name__ == '__main__':
    main()
