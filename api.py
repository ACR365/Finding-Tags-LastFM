import json
import requests
import pylast
import pandas as pd
import sqlalchemy as db

from pylast import *

#---------------------------------------------------------------------------------------------------#
# Purpose of program - Get the tags from a track and artist using user-input and printing them out  #
#---------------------------------------------------------------------------------------------------#

def find_track_tags(d, n):
  #Initalizing two empty lists:
  tags = [] #tags = list that holds the tags from the track track_object
  track_tags = [] #track_tags = list of lists that holds the tags lists
  

  i = 0
  while i != len(d):
    #Initializing artist_name and artist_track that holds the artist name and artist track
    a = d.keys() #pulls the artist name out of the list

    for k in a:
      artist = k
      artist_name = artist
      track = d[k]
      artist_track = track
      break

    track_object = n.get_track(artist_name, artist_track) #passing artist_name and #artist_track as string parameters to create the Track object
    track_tags_object = track_object.get_top_tags() #using the Track object, getting the track tags and are stored in a list
    
    #Retreiving only the name of the tag
    for t in track_tags_object:
      tag_name = t.item.get_name()
      tags.append(tag_name)

    track_tags.append(tags)
    i += 1
  
  return track_tags
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Creating an engine object
engine = db.create_engine('sqlite:///.db')

#Created variables that hold the API key, Secret ID, and User Agent for Last.fm#
LASTFM_CLIENTID = '558bf9c077dc58bcc6c355363e01ff48'
LASTFM_SECRETID = '02122f0b52383207d100b8f957b5131a'
LASTFM_USERAGENT = 'JSON Access'

#Authorizing the user in LastFM#
AUTH_URL = 'https://www.last.fm/api/auth'

headers = {
  'user-agent': LASTFM_USERAGENT
}

LASTFM_INFO = {
  'client_id': LASTFM_CLIENTID,
  'shared_secret': LASTFM_SECRETID
}

data = requests.get(AUTH_URL, headers = headers, params = LASTFM_INFO)

# In order to perform a write operation you need to authenticate yourself
username = str(input("Enter Last.FM username: ")) 
password_hash = pylast.md5(str(input("Enter Last.FM password: ")))

network = pylast.LastFMNetwork(api_key = LASTFM_CLIENTID, api_secret = LASTFM_SECRETID, username = username, password_hash = password_hash)

#Asks the user how many tracks they want to compare
count = int(input("How many artists do you want to see the track tags of: "))
ARTISTS_AND_TRACKS = [] #list of dictionaries holding the artist's name and track name
at = {} #Temporary dictionary to how the inputs of the artist's name and track name

i = 0
while i != count:
  at = {}
  ARTIST_NAME = input("Enter artist " + str(i+1) + " name: ")
  TRACK_NAME = input("Enter the track's full name: ")
  print("---------------------------------------------------------", end = '\n')
  at[ARTIST_NAME] = TRACK_NAME
  ARTISTS_AND_TRACKS.append(at)
  i += 1

#Accessing the tracks
BASE_URL = 'https://www.last.fm/api'


i = 0
TRACK_AND_TAG = {}
results = []
while i != len(ARTISTS_AND_TRACKS):
  tracks = {}
  artist_and_track = ARTISTS_AND_TRACKS[i]
  TRACK_TAGS = find_track_tags(artist_and_track, network)

  artist = ""
  track = ""
  for k in artist_and_track:
      artist = k
      track = artist_and_track[k]
  
  TRACK_AND_TAG[track] = TRACK_TAGS
  results.append(TRACK_AND_TAG.copy())

  """
  print(artist, ": ", track)
  for t in TRACK_TAGS:
    print(t)
  

  print("---------------------------------------------------------", end = '\n')
  """
  i += 1

'''
lastfm_dataframe = pd.DataFrame.from_records(results, columns=['name', 'tags'])

engine = db.create_engine('sqlite:///lastfm_database.db')
lastfm_dataframe.to_sql('lastfm_table', con=engine, if_exists='replace', index=False)

query_result = engine.execute("SELECT * FROM lastfm_table;").fetchall()
print(pd.DataFrame(query_result))
'''















