import requests
import os
import re

from html import unescape
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("NAVER_CLIENT_ID")
client_secret = os.getenv("NAVER_CLIENT_SECRET")

url = "https://openapi.naver.com/v1/search/news.json"

headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}


def get_news(query):

    params = {
        "query": query,
        "display": 5,
        "sort": "date"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    data = response.json()

    news_list = []

    for news in data["items"]:

        title = re.sub(r"<.*?>", "", news["title"])
        description = re.sub(r"<.*?>", "", news["description"])

        title = unescape(title)
        description = unescape(description)

        news_list.append({
            "종목": query,
            "제목": title,
            "링크": news["link"],
            "요약": description,
            "날짜": news["pubDate"]
        })

    return news_list