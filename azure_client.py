from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
from azure.ai.formrecognizer import FormRecognizerClient
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from msrest.authentication import CognitiveServicesCredentials


def form_recognizer_client():
    f = open("keys.txt", "r")
    keys = f.readlines()
    f.close()
    form_recognizer_endpoint = "https://matthieuc-form-recognizer.cognitiveservices.azure.com/"
    form_recognizer_key = keys[0].strip()
    client = FormRecognizerClient(form_recognizer_endpoint,
                                  AzureKeyCredential(form_recognizer_key))
    return client

def computer_vision_client():
    f = open("keys.txt", "r")
    keys = f.readlines()
    f.close()
    computer_vision_key = keys[1].strip()
    computer_vision_endpoint = "https://matthieuc-recipe-computer-vision.cognitiveservices.azure.com/"
    client = ComputerVisionClient(computer_vision_endpoint,
                                  CognitiveServicesCredentials(computer_vision_key))
    return client


