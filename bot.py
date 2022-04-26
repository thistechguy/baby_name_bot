from multiprocessing.connection import Client
import tweepy
from baby_names_list import baby_names
import random


client = tweepy.Client(
    consumer_key="vhaEN7oPE8TJKcm4eLhtB6YdJ",
    consumer_secret="vedXZsui47wPyadPyvDlAvizPTGc2ADZGvVDNJvh1uZz6mPrnO",
    access_token="1511667960330469376-1hGsrv19CEQjEw2e2MbowkLXPEmkPg",
    access_token_secret="yaF6O4XlymmyUHuAvmUjVEIkNxrvrXVIo16kb02U1vIBa"
)

selectBabyName = random.choice(baby_names)


response = client.create_tweet(text="The baby name of the day is {}!".format(selectBabyName))

print(response)