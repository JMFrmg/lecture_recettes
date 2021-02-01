from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
from azure.ai.formrecognizer import FormRecognizerClient
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from msrest.authentication import CognitiveServicesCredentials


def form_recognizer_client():
    form_recognizer_endpoint = "https://matthieuc-form-recognizer.cognitiveservices.azure.com/"
    form_recognizer_key = "107538cdca8b45d3851402c9363519c1"
    client = FormRecognizerClient(form_recognizer_endpoint,
                                  AzureKeyCredential(form_recognizer_key))
    return client

def computer_vision_client():
    computer_vision_key = "621e3f4f1e1041b3824cb77f4390e2bd"
    computer_vision_endpoint = "https://matthieuc-recipe-computer-vision.cognitiveservices.azure.com/"
    client = ComputerVisionClient(computer_vision_endpoint,
                                  CognitiveServicesCredentials(computer_vision_key))
    return client


