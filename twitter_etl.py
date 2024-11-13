import pandas as pd 
import s3fs
from datetime import datetime
import json

data=pd.read_csv('tweets.csv')
print(data[data['author']=='katyperry'].head(10))




