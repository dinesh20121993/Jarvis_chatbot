import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def get_news(category="general"):  # Added category parameter
    if not NEWS_API_KEY:
        return "Error: NEWS_API_KEY environment variable not set."

    params = {
        "country": "us",  # You can change the country
        "category": category,  # You can change the category
        "apiKey": NEWS_API_KEY,
        "pageSize": 5  # Number of headlines to return
    }
    try:
        response = requests.get(NEWS_API_URL, params=params)
        print(response)
        response.raise_for_status() # check for errors
        news_data = response.json()
        articles = news_data.get("articles", [])  # Handle cases where there are no articles
        if articles:
            headlines = [f"- {article['title']}" for article in articles]
            return "\n".join(headlines)
        else:
            return "No news headlines found for that category."
    except requests.exceptions.RequestException as e:
        return f"Error fetching news: {e}"

def extract_news_category(user_input):
    # Extract news category using regex or other methods (similar to location)
    # This is a placeholder. Implement your logic here.
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    for category in categories:
      if category in user_input:
        return category
    return "general" # Default category

