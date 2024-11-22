import pandas as pd 
import s3fs
from datetime import datetime
import json
import requests

# this function is used to transform the data from the twitter API to a csv file

# def run_twitter_etl():

#     access_key = "" 
#     access_secret = "" 
#     consumer_key = ""
#     consumer_secret = ""


#     # Twitter authentication
#     auth = tweepy.OAuthHandler(access_key, access_secret)   
#     auth.set_access_token(consumer_key, consumer_secret) 

#     # # # Creating an API object 
#     api = tweepy.API(auth)
#     tweets = api.user_timeline(screen_name='@elonmusk', 
#                             # 200 is the maximum allowed count
#                             count=200,
#                             include_rts = False,
#                             # Necessary to keep full_text 
#                             # otherwise only the first 140 words are extracted
#                             tweet_mode = 'extended'
#                             )

#     list = []
#     for tweet in tweets:
#         text = tweet._json["full_text"]

#         refined_tweet = {"user": tweet.user.screen_name,
#                         'text' : text,
#                         'favorite_count' : tweet.favorite_count,
#                         'retweet_count' : tweet.retweet_count,
#                         'created_at' : tweet.created_at}
        
#         list.append(refined_tweet)

#     df = pd.DataFrame(list)
#     df.to_csv('refined_tweets.csv')


# for index, row in data.iterrows():
#    refid_twet ={
#         'author':row['author'],
#         'content':row['content'],
#         'country':row['country'],
#         'id':row['id'],
#         'language':row['language'],
#         'latitude':row['latitude'],
#         'longitude':row['longitude'],
#         'number_of_likes':row['number_of_likes'],
#         'number_of_shares':row['number_of_shares'],
#     }
#    twitter_list.append(refid_twet) 
def run_twitter_etl():

    response = requests.get('http://127.0.0.1:5000/api/data')
    data = response.json()

    twitter_list = []
    for item in data:
      refid_twet = {
        'author': item['author'],
        'content': item['content'],
        'id': item['id'],
        'language': item['language'],
        'number_of_likes': item['number_of_likes'],
        'number_of_shares': item['number_of_shares'],
        'date_time':item['date_time']
      }
      twitter_list.append(refid_twet)

    new_data = pd.DataFrame(twitter_list)
    new_data.to_csv('s3://boussoialef-airflow-twitter-buckett/refined_tweets.csv')
    # filtered_data = new_data[new_data['country'].notna()]
    # print(filtered_data[['author', 'country']])

#run_twitter_etl()


