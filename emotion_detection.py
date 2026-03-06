"""
Emotion detection module using IBM Watson NLP endpoint.
"""

import requests


WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyze):
    """
    Analyze the input text and return emotion scores along with the dominant emotion.

    Args:
        text_to_analyze (str): Text provided by the user.

    Returns:
        dict: A dictionary containing anger, disgust, fear, joy, sadness,
              and dominant_emotion. If input is invalid, returns None values.
    """
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            WATSON_URL,
            json=payload,
            headers=HEADERS,
            timeout=10
        )
    except requests.exceptions.RequestException:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if response.status_code != 200:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    try:
        response_json = response.json()
        emotions = response_json["emotionPredictions"][0]["emotion"]
    except (KeyError, IndexError, ValueError, TypeError):
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions.get("anger"),
        "disgust": emotions.get("disgust"),
        "fear": emotions.get("fear"),
        "joy": emotions.get("joy"),
        "sadness": emotions.get("sadness"),
        "dominant_emotion": dominant_emotion
    }
