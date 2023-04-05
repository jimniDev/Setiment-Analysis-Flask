from __future__ import print_function
import base64
import json
import requests

# Workaround to support both python 2 & 3
try:
    import urllib.request, urllib.error
    import urllib.parse as urllibparse
except ImportError:
    import urllib as urllibparse




# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

'''

    This code was based on
    https://github.com/hereismari/spotify-flask

    --------------------- HOW THIS FILE IS ORGANIZED --------------------
    0. SPOTIFY BASE URL
    1. SEARCH : https://developer.spotify.com/documentation/web-api/reference/search
    2. TRACK: https://developer.spotify.com/documentation/web-api/reference/get-track
    3. RECOMMENDATIONS: https://developer.spotify.com/documentation/web-api/reference/get-recommendations
'''

# ----------------- 0. SPOTIFY BASE URL ----------------

SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# ------------------ 1. SEARCH ------------------------
#  https://developer.spotify.com/documentation/web-api/reference/search

SEARCH_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'search')

def search(track, artist):
    myparams = {'limit': 1}
    myparams['type'] = 'track'
    myparams['q'] = 'track:{track} artist:{artist}'
    resp = requests.get(SEARCH_ENDPOINT, params=myparams)
    return resp.json()

# ------------------ 2. TRACK ------------------------
# https://developer.spotify.com/documentation/web-api/reference/get-track

GET_TRACK_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'tracks')  # /<id>

def get_track(track_id):
    url = "{}/{id}".format(GET_TRACK_ENDPOINT, id=track_id)
    resp = requests.get(url)
    return resp.json()

GET_TRACK_AUDIO_FEATURE_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'audio-features')  # /<id>

# https://developer.spotify.com/documentation/web-api/reference/get-track
def get_track_audio_feature(track_id):
    url = "{}/{id}".format(GET_TRACK_AUDIO_FEATURE_ENDPOINT, id=track_id)
    resp = requests.get(url)
    return resp.json()


# ------------------ 3. RECOMMENDATIONS ------------------------
#  https://developer.spotify.com/documentation/web-api/reference/get-recommendations

RECOMMENDATIONS_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'search')

# seed_artists, seed_genres, seed_tracks(Spotify ID)
def get_recommendations(seed_artists, seed_genres, seed_tracks):

    myparams = {'limit': 5}
    myparams['seed_artists'] = seed_artists
    myparams['seed_genres'] = seed_genres
    myparams['seed_tracks'] = seed_tracks
    resp = requests.get(RECOMMENDATIONS_ENDPOINT, myparams)
    return resp.json()
