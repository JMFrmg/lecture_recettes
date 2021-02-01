import os
from PIL import Image
from azure_client import computer_vision_client


class Photo:
    def __init__(self):
        self.dir_path = ""

    def photos_coord(self, path):
        client = computer_vision_client()
        img = open(path, "rb")
        detected_obj = client.detect_objects_in_stream(img)

        return [(obj.rectangle.x,
                 obj.rectangle.y,
                 obj.rectangle.x + obj.rectangle.w,
                 obj.rectangle.y + obj.rectangle.h) for obj in detected_obj.objects]

    def get_photo(self, files):
        for f in files:
            f_path = os.getcwd() + "\\recettes\\" + f
            img = Image.open(f_path)
            boxes = self.photos_coord(f_path)
            if boxes:
                if len(boxes) > 1:
                    surfaces = [(b[2]-b[0])*(b[3]-b[1]) for b in boxes]
                    biggest = boxes[surfaces.index(max(surfaces))]
                elif len(boxes) == 1:
                    biggest = boxes[0]
                area = img.crop(biggest)
                area.save(os.getcwd() + "\\photos\\" + f.split(".")[0] + ".png", "PNG")