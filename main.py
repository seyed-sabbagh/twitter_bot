import tweepy
import time

consumer_key = '8YiIXlTqc6daUBu2IyQ0CZbnj'
consumer_secret = 'PmZa49PQe2rETukpdelSOc3aRItDkh0O1QfwgzKrBuR1vSDAfM'
key = '1423633756980760577-Wxk4FU6WtY0UMvBhO4HUy32k7SLUQu'
secret = 'KrtEsgAeAJANB0EXPFrEFuHiYWzVhyTC5bmlGvilgZL8b'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
# api.update_status('Hellow World...')

#
# hastagh = "#android"
# tweetnumber = 10
# tweets = tweepy.Cursor(api.search, hastagh).items(tweetnumber)
#
# #
# def searchBot():
#     for tweet in tweets:
#         try:
#             tweet.retweet()
#             print("retweet...")
#             time.sleep(2)
#         except tweepy.TweepError as e:
#             print(e.reason)
#             time.sleep(2)
#
#
# searchBot()
#

FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME))
    for tweet in reversed(tweets):
        if '#test' in tweet.text.lower():
            print(str(tweet.id) + ' _ ' + tweet.text)

            api.update_status("@" + tweet.user.screen_name + " test like retweet reply", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print(follower.screen_name)


while True:
    reply()
    time.sleep(15)
