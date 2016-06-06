#! Python 3
import tweepy, json
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pandas as pd
from tweepy import Stream
import matplotlib as plt
import re

consumer_key = 'X1oBSouWiKfQZSdqF8iuAUDOK'
consumer_secret = 'OCrqzRFK8iq4S7JoutGmnU6WglmpcgjvqPvi26EDYFqfUqb2zV'
access_token = '156372154-IWdpOGaWhhtNP3FS6GoTvTMVXs6ek7hOobzLflUV'
access_secret = 'mxYhYwDpCe3PehTCjclkwlvgwlZFYewGFbtDKznkof9tZ'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


bern = api.search(q='%23FeelTheBern')
trump = api.search(q='%23MakeAmericaGreatAgain')
trump2 = api.search(q='%23DumpTrump')
hillary = api.search(q='%23ImWithHer')


class StdOutListener(StreamListener):

    def on_data(self, data):
        saveData = open('C:\\Users\\Mr Software\\PycharmProjects\\PresidentialCandidates\\collectedData.txt', 'a')
        saveData.write(data)
        print (data)
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    stream.filter(track=['clinton', 'trump', 'bernie'])


