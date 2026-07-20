""" sentiment analysis module """
import json
import requests

def sentiment_analyzer(text_to_analyze):
    """ run a sentiment analysis on on text
    Input (str): text to analyze 
    Outputs: tuple (label, score) 
        """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/\
    v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = {"raw_document":{"text":text_to_analyze}}
    response = requests.post(url, json = myobj, headers=headers, timeout=10)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    else:
        label = None
        score = None
    return {'label':label,'score':score}
