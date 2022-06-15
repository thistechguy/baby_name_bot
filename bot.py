from multiprocessing.connection import Client
import tweepy
from baby_names_list import baby_names
from config import client
import random

selectBabyName = random.choice(baby_names)


response = client.create_tweet(text="The baby name of the day is {}!".format(selectBabyName))

print(response)
