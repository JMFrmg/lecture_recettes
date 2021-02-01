import os
import pickle
import pandas as pd
from isolate_photo import Photo
from form_recognizer import Recipe
import sidetable as stb



recipe = Recipe()

#Récupérer les données texte d'une recette:
df_results = recipe.get_data("IMG-2779.jpg", local=False)
print(df_results.head(20))

#Créer un nouveau fichier pickel:
#recipe.new_pickel_file("IMG-2777.jpg")


recipe_photo = Photo()

#Récupérer la photo d'une seule recette dans le dossier "recettes":
#recipe_photo.get_photo(["marmiton.png"])

#Récupérer les photos de toutes les recettes dans le dossier "recettes":
#for root, dirs, files in os.walk(os.getcwd() + "\\recettes\\"):
#    my_photo.get_photo(files)


