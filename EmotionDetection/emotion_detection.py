import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = json_obj, headers = headers)
    json_response = json.loads(response.text)
    emotions = json_response['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(emotions, key = emotions.get)
    return emotions