import os
import pickle
import pandas as pd
from azure_client import form_recognizer_client

class Recipe:
    def data_load(self, file, local=False):
        if local:
            with open(file.split(".")[0] + '_pickel', 'rb') as f:
                page = pickle.load(f)
            return page
        else:
            recettes_dir = os.getcwd() + "\\recettes\\" + file
            with open(recettes_dir, "rb") as fd:
                image_data = fd.read()
            poller = form_recognizer_client().begin_recognize_content(image_data)
            return poller.result()

    def get_data(self, file, local):
        data = self.data_load(file, local)
        return pd.DataFrame({
                   "text": [l.text for l in data[0].lines],
                   "chars": [len(l.text) for l in data[0].lines],
                   "x": [l.bounding_box[0].x for l in data[0].lines],
                   "y": [l.bounding_box[0].y for l in data[0].lines],
                   "size": [l.bounding_box[2].y - l.bounding_box[0].y for l in data[0].lines]
        })

    def new_pickel_file(self, file):
        data = self.data_load(file)
        with open(file.split(".")[0] + '_pickel', 'wb') as f1:
            pickle.dump(data, f1)