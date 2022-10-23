import pandas
import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools


# searching by location
loc = '51.500153, -0.1262362, 100km'
df_coord = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    'tired of this life geocode:"{}"'.format(loc)).get_items(), 500))[['user', 'date', 'content']]

df_coord['user_location'] = df_coord['user'].apply(lambda x: x['location'])

df_coord.head()

# df_coord.to_csv("tired.csv")

print(df_coord)


# merging the data
from pathlib import Path
import pandas as pd
import numpy as np

path = r'C:\Users\sumbo\PycharmProjects\omdenaproject_self_harm'

# Get the files from the path provided in the OP
files = Path(path).glob('*.csv')  # .rglob to get subdirectories

# loading the data from path to directory and on system for merging
dfs = list()
for f in files:
    data = pd.read_csv(f)
    # .stem is method for pathlib objects to get the filename w/o the extension
    data['file'] = f.stem
    dfs.append(data)

df = pd.concat(dfs, ignore_index=True)

# df.to_csv("final.csv")
# https://medium.com/swlh/how-to-scrape-tweets-by-location-in-python-using-snscrape-8c870fa6ec25


dataframe = pandas.read_csv(r'C:\Users\sumbo\PycharmProjects\omdenaproject_self_harm\data.csv')
print(dataframe)



