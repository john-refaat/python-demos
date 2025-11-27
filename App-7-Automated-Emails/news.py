import os
from datetime import datetime

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class NewsFeed:
    _base_url = "https://newsapi.org/v2/everything"

    def __init__(self, user_name: str,
                 keyword: str, from_date: str = "2025-11-24", to_date: str = datetime.now().strftime("%Y-%m-%d"),
                 language: str = "en", sort_by: str = "popularity"):
        self.user_name = user_name
        self.keyword = keyword.replace(" ", "+")
        self.from_date = from_date
        self.to_date = to_date
        self.language = language
        self.sort_by = sort_by
        self.url = f"{self._base_url}?q={self.keyword}"
        self.url += "&searchIn=title,description"
        if self.from_date:
            self.url += f"&from={self.from_date}"
        if self.to_date:
            self.url += f"&to={self.to_date}"
        if self.language:
            self.url += f"&language={self.language}"
        if self.sort_by:
            self.url += f"&sortBy={self.sort_by}"
        api_key = os.getenv("newsapi.key")
        self.url += f"&apiKey={api_key}"
        self.feed_items = []

    def _get_news(self):
        print(f"Retrieving news feed for '{self.keyword}'...")
        response = requests.get(self.url)

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.json()['message']}")
        else:
            print("News feed retrieved successfully.")
            self.feed_items = response.json()["articles"]
        return self.feed_items

    def create_email_body(self):
        self._get_news()
        body = f"Hi {self.user_name},\n\n"
        if self.feed_items:
            body += f"Here are the top news articles for {self.keyword}:\n\n"
            for item in self.feed_items:
                body += f"{item['title']}\n{item['url']}\n\n"
        else:
            body += f"No news articles found for {self.keyword}.\n\n"
        body += "Regards,\nNewsBot"
        return body


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    search_term = input("Enter a search term: ")
    feed = NewsFeed(user_name, keyword=search_term, from_date="2025-11-24", to_date="2025-11-25")
    body = feed.create_email_body()
    print(body)
