import time
import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

bearer_token = "AAAAAAAAAAAAAAAAAAAAABwBzgEAAAAAVCPmFnZswEoIQ%2BxxTiss7mzr1XA%3DOpAilqkD3ZEPTjpimGrSFFPgspzneKX5SfakRY6wdHLcCoHxqk"
client = tweepy.Client(bearer_token=bearer_token)

hashtag = "#cats"
num_tweets = 70

tweets = []

def fetch_tweets():
    global tweets
    wait_time = 20
    max_wait = 180

    while True:
        try:
            for tweet in tweepy.Paginator(client.search_recent_tweets, query=hashtag, max_results=10).flatten(
                    limit=num_tweets):
                tweets.append(tweet.text)
                time.sleep(2)
            break

        except tweepy.errors.TooManyRequests as e:
            reset_time = int(e.response.headers.get("x-rate-limit-reset", time.time() + 60))
            wait_time = max(reset_time - time.time(), 30)

            print(f"Rate limit aşıldı! {int(wait_time)} saniye bekleniyor...")
            time.sleep(wait_time)

            if wait_time >= max_wait:
                print("Çok uzun süredir bekleniyor. Twitter API bloklamış olabilir. Daha sonra tekrar dene.")
                break

fetch_tweets()

df = pd.DataFrame(tweets, columns=["Tweet"])

def get_sentiment(text):
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Tweet"].apply(get_sentiment)

plt.figure(figsize=(6, 4))
sns.countplot(x=df["Sentiment"], palette=["red", "blue", "green"])
plt.title("Sentiment Analysis of Tweets")
plt.xlabel("Sentiment")
plt.ylabel("Tweet Count")
plt.show()
