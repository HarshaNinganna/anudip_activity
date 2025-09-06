from transformers import pipeline
import requests

# HuggingFace summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Example: Fetch news from an API (here we use NewsAPI - replace with your API key)
API_KEY = "your_api_key"
url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"

response = requests.get(url).json()

# Take the first article
article = response["articles"][0]
title = article["title"]
content = article["description"] or article["content"]

print(" Title:", title)
print("\nOriginal Content:", content)

# Summarize the news content
if content:
    summary = summarizer(content, max_length=60, min_length=25, do_sample=False)
    print("\n AI Summary:", summary[0]['summary_text'])
else:
    print("No content available for summarization.")
