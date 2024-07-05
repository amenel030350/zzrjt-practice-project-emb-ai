from sentiment_analysis import sentiment_analyzer
import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.sentiment'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow"}
    response = requests.post(url, json=myobj, headers=header)
    return response.json()  # Assuming the response is in JSON format
