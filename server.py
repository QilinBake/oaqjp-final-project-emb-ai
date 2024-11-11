from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    response = emotion_detector(request.args.get('textToAnalyze'))
    if not response['dominant_emotion']:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
            f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}.")

@app.route("/")
def render_index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)