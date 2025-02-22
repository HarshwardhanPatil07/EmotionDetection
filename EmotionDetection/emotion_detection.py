import json
import requests

def emotion_detector(text_to_analyze):
    # If the input is blank (after stripping whitespace), return error dictionary.
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        emotions = data.get('emotionPredictions', [{}])[0].get('emotion', {})
        if not emotions:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        dominant_emotion = max(emotions, key=emotions.get)
        output = {
            'anger': emotions.get('anger'),
            'disgust': emotions.get('disgust'),
            'fear': emotions.get('fear'),
            'joy': emotions.get('joy'),
            'sadness': emotions.get('sadness'),
            'dominant_emotion': dominant_emotion
        }
        return output
    elif response.status_code == 400:
        # If the API returns a 400 status (e.g., due to blank input), return keys with None.
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # For other errors, you may choose to return an error dictionary or message.
        return {"error": f"Error: {response.status_code}, {response.text}"}
