from flask import Flask, request, jsonify, render_template
from util.emotion import Emotion
from util.spotiy_auth import SPOTIFY_AUTH
from model import setiment_analysis_inference as inference
from api import spotify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

app = Flask(__name__)
Emotion = Emotion()

cid = SPOTIFY_AUTH['CID']
secret = SPOTIFY_AUTH['SECRET']
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



''' Main page '''
@app.route('/')
def hello():
    return "Flask Connected"

@app.route('/analysis', methods=['POST'])
def analysisEmotion():
    res = request.get_json()
    sentence = res['text']
    print(sentence)

    res = request.get_json()
    sentence = res['text']
    print(sentence)
    if sentence is None or len(sentence) == 0:
        return jsonify({
            "joy": 0,
            "anxiety": 0,
            "embarrassment": 0,
            "sadness": 0,
            "anger": 0,
            "hurt": 0,
            "top": {
                "num": '',
                "val": '',
            }
        })

    probability, top = inference.predict(sentence)
    return jsonify({
        "joy": probability[Emotion.JOY],
        "anxiety": probability[Emotion.ANXIETY],
        "embarrassment": probability[Emotion.EMBARRASSMENT],
        "sadness": probability[Emotion.SADNESS],
        "anger": probability[Emotion.ANGER],
        "hurt": probability[Emotion.HURT],
        "top": {
            "num": top,
            "val": Emotion.to_string(top),
        }
    })

''' Spotify'''
@app.route('/search', methods=['GET'])
def search():
    track = request.args.get('track', type = str)
    artist = request.args.get('artist', type = str)
    q = 'track:'+ track +' artist:'+ artist

    # q = 'track:'+'dna'+' artist:'+'BTS'
    res = sp.search(q=q, limit=1, type='track')
    items = res['tracks']['items']
    pprint.pprint(res)
    if len(items) == 0:
        return jsonify({
            'res': 'No Matching Result'
            })
    else:
        # pprint.pprint(items[0]['album']['name'])
        # pprint.pprint(items[0]['album']['images'])
        # pprint.pprint(items[0]['artists'][0]['name'])
        # pprint.pprint(items[0]['id'])
        # pprint.pprint(items[0]['name'])
        # pprint.pprint(items[0]['preview_url'])

        return jsonify({
            'album': items[0]['album']['name'],
            'imgs': items[0]['album']['images'],
            'artist': items[0]['artists'][0]['name'],
            'spotify_id': items[0]['id'],
            'name': items[0]['name'],
            'preview': items[0]['preview_url'],
        })


if __name__ == "__main__": 
    app.run(host='0.0.0.0', port='5001', debug=True)