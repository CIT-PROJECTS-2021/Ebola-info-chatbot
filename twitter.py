import tweepy
import configparser


# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = 'MinofHealthUG'
limit = 20

# fetch tweets
tweets = api.user_timeline(screen_name = user, count = limit, tweet_mode = 'extended')

try:
    f = open("info\\latest.txt", "w", encoding="utf-8")
    tweet_num = 0
    for tweet in tweets:
        if 'ebola' in tweet.full_text.lower():
            tweet_num += 1
            try:
                # to fetch full text for retweets; since twitter api has a limit of characters sent
                text = tweet.retweeted_status.full_text
            except:
                # fetch full text for normal tweets
                text = tweet.full_text
            # add tweets to latest.txt file
            f.write(text)
            f.write('\n\n')

            # limit to 5 tweets
            if tweet_num > 5:
                break
except Exception as err:
    print("An error occurred: ", err)
finally:
    f.close()