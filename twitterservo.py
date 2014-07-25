#!/usr/bin/env python
import twitter
import os

def tweetIt (description, fname, ftype):
	api = twitter.Api(consumer_key=os.environ["TW_CONSUMER_KEY"], consumer_secret=os.environ["TW_CONSUMER_SECRET"], access_token_key=os.environ["TW_TOKEN"],access_token_secret=os.environ["TW_TOKEN_SECRET"])
	if len(description) > 99:
		description = description[:99]
	out_text = "New posting: " + description[:99] + " https://s3.amazonaws.com/dcfoiaservo/" + fname + "." + ftype
	status = api.PostUpdate(out_text)