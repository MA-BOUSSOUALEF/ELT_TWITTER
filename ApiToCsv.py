import pandas as pd 
import s3fs
from datetime import datetime
import json
import requests

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
    new_data.to_csv('cc')
    # filtered_data = new_data[new_data['country'].notna()]
    # print(filtered_data[['author', 'country']])

run_twitter_etl()