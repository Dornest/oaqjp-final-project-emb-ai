import requests
import json
def emotion_detector(text_to_analyse):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json={"raw_document":{"text":text_to_analyse}}
    response=requests.post(url,Headers=Headers,json=Input_json)
    response=json.loads(response.text)
    emotions=response_dict['emotionPredictions'][0]['emotion']

    anger_score=emotions['anger']
    disgust_score=emotions['disgust']
    fear_score=emotions['fear']
    joy_score=emotion['joy']
    sadness_score=emotions['sadness']

    emotion_score={
        'anger':anger_score,
        'disgust':disgust_score,
        'fear':fear_score,
        'joy':joy score,
        'sadness':sadness_score
    }
    dominant_emotion=max(emotion_scores,key=emotion_scores.get)
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }