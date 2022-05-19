from multiprocessing.connection import Client
import tweepy
from baby_names_list import baby_names
from config import client
import random


#client = tweepy.Client(
#    consumer_key="",
#    consumer_secret="",
#    access_token="",
#    access_token_secret=""
#)

selectBabyName = random.choice(baby_names)


response = client.create_tweet(text="The baby name of the day is {}!".format(selectBabyName))

print(response)
