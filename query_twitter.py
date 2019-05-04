from pprint import pprint

import yaml
import twitter

with open("twitter.yaml", "r") as auth_file:
    auth = yaml.safe_load(auth_file)

api = twitter.Api(
    consumer_key=auth["api_key"],
    consumer_secret=auth["api_secret"],
    access_token_key=auth["access_token"],
    access_token_secret=auth["access_secret"],
    tweet_mode="extended",
    cache=None,
)


def get_tweet_text(screen_name):
    timeline = api.GetUserTimeline(
        screen_name=screen_name, count=2000, exclude_replies=True, include_rts=False
    )
    return [status.full_text for status in timeline]


if __name__ == "__main__":
    pprint(get_tweet_text(screen_name="UniOfSurrey"))
