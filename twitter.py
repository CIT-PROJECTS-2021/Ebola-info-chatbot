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

#public_tweets = api.home_timeline()

user = 'MinofHealthUG'
limit = 10

tweets = api.user_timeline(screen_name = user, count = limit, tweet_mode = 'extended')

try:
    f = open("info\\latest.txt", "w", encoding="utf-8")
    tweet_num = 0
    for tweet in tweets:
        if 'ebola' in tweet.full_text.lower():
            tweet_num += 1
            try:
                text = tweet.retweeted_status.full_text
            except:
                text = tweet.full_text
            f.write(text)
            f.write('\n\n')
            if tweet_num > 2:
                break
except Exception as err:
    print("An error occurred: ", err)
finally:
    f.close()