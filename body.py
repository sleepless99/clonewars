import tweepy
import logging
import time
import random
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from config import create_api
api = create_api()




def make_a_tweet(api):

    #making a tweet
    change=[5,6,7,5,6,3,2,1]
    message = ["“In other words, we’re lyrical Zuckerbergs” – Lupe Fiasco","“Great things are done by a series of small things brought together” — Vincent Van Gogh","“Turn sh*t into sugar” – Robert Greene","“You have to create something from nothing” – Ralph Lauren","“In order to be irreplaceable, one must always be different”— Gabrielle Bonheur “Coco” Chanel","“Hustle beats talent, when talent doesn’t hustle” – Unknown","“It’s the job that’s never started that takes longest to finish” – J. R. R. Tolkien","Question every traditional way of doing things when you are luckyenough to live in the internet age`- Alex Da Kid",". “Your friends just flipped over the swift penmanship” – Marshall Mathers","“Everyone sleeping on you is gonna wake up working for you” – Kia Shine"]
    tags=["\n\nThe Remedy for Writer's Block|Link in Bio \n\n#resumehelp #ghostwriter  #essaypay  #Termpaper  #essaydue"," \n\nThe Remedy for Writer's Block|Link in Bio\n\n #essaypay #essayhelp #Termpaper  #essaydue #Dissertations #englishpaper #writersblock","\n\n The Remedy for Writer's Block|Link in Bio \n\n#Dissertations #englishpaper #writersblock #lyrics #businessplans #historypaper ","\n\nThe Remedy for Writer's Block|Link in Bio\n\n#englishpaper #writersblock #lyrics #businessplans #historypaper #literaryanalysis  ","\n\nThe Remedy for Writer's Block|Link in Bio \n\n#Dissertations #englishpaper #writersblock #lyrics #businessplans #historypaper"]
    while True:
        now = str(datetime.now().strftime('%H:%M:%S'))
        try:
            api.update_status(  random.choice(message) + "\n \n " +random.choice(tags) + "\n" + now)
            print("made a tweet")
            time.sleep(60*59)
        except Exception as e:
            print(e)
        time.sleep(random.choice(change))

    #liking a tweet

        for tweet in tweepy.Cursor(api.search, q='#resumehelp',rpp=100).items(4):
            time.sleep(5)
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    time.sleep(45)
                except Exception as e:
                    print(e)

        for tweet in tweepy.Cursor(api.search, q='#ghostwriter',rpp=100).items(4):
            time.sleep(5)
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    time.sleep(45)
                except Exception as e:
                    print(e)
    
        for tweet in tweepy.Cursor(api.search, q='#ghostwriting',rpp=100).items(4):
            time.sleep(5)
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    time.sleep(45)
                except Exception as e:
                    print(e)
    
        for tweet in tweepy.Cursor(api.search, q='#essaypay',rpp=100).items(4):
            time.sleep(5)
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    time.sleep(45)
                except Exception as e:
                    print(e)
    
        for tweet in tweepy.Cursor(api.search, q='#essayhelp',rpp=100).items(4):
            time.sleep(5)
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    time.sleep(45)
                except Exception as e:
                    print(e)
    
        for tweet in tweepy.Cursor(api.search, q='#Termpaper',rpp=100).items(4):
            time.sleep(5)
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    time.sleep(45)
                except Exception as e:
                    print(e)
    
        for tweet in tweepy.Cursor(api.search, q='#essaydue',rpp=100).items(4):
            time.sleep(5)
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    time.sleep(45)
                except Exception as e:
                    print(e)
    
        for tweet in tweepy.Cursor(api.search, q='#Dissertations',rpp=100).items(4):
            time.sleep(5)
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    time.sleep(45)
                except Exception as e:
                    print(e)
    
        for tweet in tweepy.Cursor(api.search, q='#englishpaper',rpp=100).items(4):
            time.sleep(5)
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    time.sleep(45)
                except Exception as e:
                    print(e)
    
        for tweet in tweepy.Cursor(api.search, q='#writersblock',rpp=100).items(4):
            time.sleep(5)
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    time.sleep(45)
                except Exception as e:
                    print(e)
    
    


while True:
    make_a_tweet(api)
    time.sleep(10)
print('\n\n\n                   out of the loop                           ')