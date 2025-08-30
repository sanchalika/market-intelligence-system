import snscrape.modules.twitter as sntwitter
import json
from datetime import datetime, timedelta


HASHTAGS = ['#nifty50', '#sensex', '#intraday', '#banknifty']
since = (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%d')
until = datetime.utcnow().strftime('%Y-%m-%d')


query = " OR ".join(HASHTAGS) + f" since:{since} until:{until}"
outf = "data/raw/tweets_last24h.jsonl"


def stream_tweets(limit=2000):
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
yield tweet
if limit and i+1 >= limit:
break


with open(outf, "w", encoding="utf-8") as fh:
for tweet in stream_tweets():
data = {
"tweet_id": tweet.id,
"username": tweet.user.username,
"created_at": tweet.date.isoformat(),
"content": tweet.content,
"retweets": tweet.retweetCount,
"likes": tweet.likeCount
}
fh.write(json.dumps(data, ensure_ascii=False) + "\n")