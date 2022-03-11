import tweepy
import feedparser
import requests
import time
import json
from pathlib import Path


PATH = "/home/ben/codes/python/tt_scrap/"

with open(PATH + "db.json", "r") as json_file:
        DICO = json.load(json_file)

def code(URL, WEBHOOK, USERNAME, AVATAR_URL, GUID):
    print(DICO['USERNAME'][k])

    bearer_token = r""
    client = tweepy.Client(bearer_token)
    query = 'from:DOFUSfr -is:retweet -is:reply'
    tweets = client.search_recent_tweets(query=query, max_results=10)
    for tweet in tweets.data:
        # Recherche si le GUID du post rss existe dans le fichier
        fichier = open(GUID, 'r').read().find(str(tweet.id))
        # Si le GUID existe il renvois 0 sinon -1 | On print les infos et on ecrit le guid du post dans le fichier GUID
        if fichier == -1 :
            print("\nNouveaux Tweet :\n",tweet)
            print(str(tweet.id))
            fichier = open(GUID, "a")
            fichier.write("\n" + str(tweet.id))
            fichier.close()

            # Partie config webhook discord
            data = {}
            data["content"] = tweet.text
            data["username"] = USERNAME
            data["avatar_url"] = AVATAR_URL
            # Partie qui envoi l'info au webhook (a desactiver pour migration / initialisation ou test)
            #requests.post(WEBHOOK, json = data)
            #time.sleep(1)
        else :
            print("exist")

    print('\n')

for (k, v) in DICO['URL'].items():
    guid_file = Path(DICO['GUID'][k])
    guid_file.touch(exist_ok=True)
    code(DICO['URL'][k], DICO['WEBHOOK'][k], DICO['USERNAME'][k], DICO['AVATAR'][k], DICO['GUID'][k])

json_file.close()
