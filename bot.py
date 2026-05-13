import tweepy

consumer_key = "API_KEY"
consumer_secret = "API_SECRET"

access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_SECRET"

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

client.create_tweet(text="سبحان الله 🤍")
print("Tweet sent")
