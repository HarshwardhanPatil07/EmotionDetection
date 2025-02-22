"""
server.py

Flask server for the Emotion Detection web application.
Provides endpoints for serving the main page and processing emotion detection requests.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    This code receives the text from the HTML interface and 
    runs the emotion_detector() function over it. The output returned shows 
    the label and its confidence score for the provided text.
    
    Returns:
        str: A formatted response with emotion scores and the dominant emotion,
             or an error message if the text is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    stored_text = emotion_detector(text_to_analyze)
    if stored_text.get('dominant_emotion') is not None:
        anger = stored_text.get('anger')
        disgust = stored_text.get('disgust')
        fear = stored_text.get('fear')
        joy = stored_text.get('joy')
        sadness = stored_text.get('sadness')
        dominant_emotion = stored_text.get('dominant_emotion')
        return (
            f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, "
            f"'fear': {fear}, 'joy': {joy} and "
            f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
        )
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    """
    Initiates the rendering of the main application page over the Flask channel.
    
    Returns:
        str: Rendered HTML content from the index.html template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
