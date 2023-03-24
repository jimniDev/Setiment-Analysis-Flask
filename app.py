from flask import Flask, request, jsonify, render_template
from util.emotion import Emotion
from model import setiment_analysis_inference as inference

app = Flask(__name__)
Emotion = Emotion()

''' Main page '''
@app.route('/')
def hello():
    return "wow!!"


@app.route('/analysis')
def analysisEmotion():
    sentence = request.args.get("s")
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


if __name__ == "__main__": 
    app.run(host='0.0.0.0', port='5001', debug=True)