import json
import requests
import pylast

from pylast import *

#---------------------------------------------------------------------------------------------------#
#Purpose of program - compares tags of tracks by artists (the same or different) inputed by the user#
#---------------------------------------------------------------------------------------------------#

def find_track_tags(d, n):
  tags = []
  track_tags = []
  
  i = 0
  while i != len(d):
    a_and_t = d[i]
    a = a_and_t.keys()

    artist_name = ""
    artist_track = ""

    for k in a:
      artist = k
      artist_name = artist
      track = a_and_t[k]
      artist_track = track
      break

    track_object = n.get_track(artist_name, artist_track)
    track_tags_object = track_object.get_top_tags()
    
    for t in track_tags_object:
      print(t)
      break;

    track_tags.append(tags)
    i += 1

    
    
    
    
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
username = str(input("Enter username: ")) 
password_hash = pylast.md5(str(input("Enter password: ")))

network = pylast.LastFMNetwork(api_key = LASTFM_CLIENTID, api_secret = LASTFM_SECRETID, username = username, password_hash = password_hash)

#Asks the user how many tracks they want to compare
count = int(input("How many artists do you want to compare: "))
ARTISTS_AND_TRACKS = [] #list of dictionaries holding the artist's name and track name
at = {} #Temporary dictionary to how the inputs of the artist's name and track name

i = 0
while i != count:
  ARTIST_NAME = input("Enter artist " + str(i+1) + " name: ")
  TRACK_NAME = input("Enter the track's full name: ")
  print("---------------------------------------------------------", end = '\n')
  at[ARTIST_NAME] = TRACK_NAME
  ARTISTS_AND_TRACKS.append(at.copy())
  i += 1

#Accessing the tracks
BASE_URL = 'https://www.last.fm/api'

print(
  "Choose the options below!\n" + 
  "(1) Compare the tags to see if they are the same\n" +
  "(2) Compare the number of tags\n"
)

answer = int(input("Answer: "))
if (answer == 1):
  tagsEqual = find_track_tags(ARTISTS_AND_TRACKS, network)















