from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
from azure.ai.formrecognizer import FormRecognizerClient
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from msrest.authentication import CognitiveServicesCredentials

def get_api_creds(ressource):
    f = open("keys.txt", "r")
    keys = f.readlines()
    f.close()
    creds_dict = {l.split(" ")[0].strip(): l.split(" ")[1].strip() for l in keys}
    return (creds_dict[ressource + "_endpoint"], creds_dict[ressource + "_key"])

def form_recognizer_client():
    creds = get_api_creds("form_recognizer")
    form_recognizer_key = creds[1]
    client = FormRecognizerClient(creds[0],
                                  AzureKeyCredential(form_recognizer_key))
    return client

def computer_vision_client():
    creds = get_api_creds("computer_vision")
    computer_vision_key = creds[1]
    computer_vision_endpoint = creds[0]
    client = ComputerVisionClient(computer_vision_endpoint,
                                  CognitiveServicesCredentials(computer_vision_key))
    return client


