import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url , json=myobj, headers=header)
    jsoned = response.json()

    anger = jsoned['emotionPredictions'][0]['emotion']['anger']
    disgust = jsoned['emotionPredictions'][0]['emotion']['disgust']
    fear = jsoned['emotionPredictions'][0]['emotion']['fear']
    joy = jsoned['emotionPredictions'][0]['emotion']['joy']
    sadness = jsoned['emotionPredictions'][0]['emotion']['sadness']

    dominant = max(anger, disgust, fear, joy, sadness)

    result = {
        'anger' : anger,
        'disgust' : disgust,
        'fear' : fear,
        'joy' : joy,
        'sadness' : sadness,
        'dominant_emotion' : dominant 
    }


    return result