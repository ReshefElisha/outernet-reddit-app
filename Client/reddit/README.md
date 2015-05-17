# twitter-app
Twitter app for use with Librarian. 
Takes JSON files from /files/tweets/ and displays them in accordance with the [twitter guidelines](https://support.twitter.com/articles/114233). The following is an example of the syntax required for JSON files (order of keys is irrelevant, i used alphabetical for simplicity):
```json
{
    "date": "2015-03-17",
    "handle": "BreakingNews",
    "id": "577895032209960960",
    "text": "RT @breakingpol: Illinois Rep. Aaron Schock is resigning his seat in Congress - @politico http://t.co/sgCkJiSSyP",
    "time": "18:11:27"
}
```

Also included is tweetfeeder.py, which is currently set up with my keys except the secret ones, so if you'd like to use it (you're welcome to) you'll have to change the keys to reflect your twitter access keys. Syntax for use is simple:
```
python tweetfeeder.py @BreakingNews MY_LONG_SECRET_KEY MY_LONG_SECRET_TOKEN --since OPTIONAL_ID_TO_RETRIEVE_TWEETS_SINCE
```

