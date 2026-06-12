"""
Flask server for Emotion Detection application.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def em_detector():
    """
    Handles emotion detection request and returns formatted response.
    """
    text_to_analyse = request.args.get("textToAnalyze")

    # handle blank input
    if not text_to_analyse:
        return "Invalid input. Please try again", 400

    response = emotion_detector(text_to_analyse)

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the main UI page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000)
