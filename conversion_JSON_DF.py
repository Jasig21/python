#Importation des modules dont on aura besoin 
import requests
import pandas as pd
import json

url_local = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
url_nb = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"

#Récupération de la donnée à partir des liens de l'API Vélib'
localisation = requests.get(url_local) #Données relatives à la localisation des stations Vélib'
nombre = requests.get(url_nb) #Données relatives au nombre de vélos et de bornettes disponibles par station

#Chargement de la donnée sous format json
data_local = json.loads(localisation.content)
data_nb = json.loads(nombre.content)

#Normalisation de la donnée sous forme de data-frame afin de pouvoir les manipuler avec géopandas
df_local = pd.json_normalize(data_local['data'], record_path =['stations'])
df_nb = pd.json_normalize(data_nb['data'], "stations")
df_nb
