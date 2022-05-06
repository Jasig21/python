# Exercice python | API Velib'

Objectif : 
Télécharger via le code les données de l'API Vélib pour faire une carte (folium) des stations (flux de localisation) en associant à chaque station le nombre de vélib disponibles lors de l'appel de l'API (flux sur le nombre de vélo disponibles). Il faut donc faire une "jointure" entre ces 2 sources.

Essai : Le code ci-dessus récupère la localisation et le nombre de stations Velib' à partir de l'API et elles sont lues sous format JSON. Pour faire une jointure je dois les convertir en dataframe. Pour celà j'utilise le module panda. Le dataframe issu du JSON de localisation est bien formaté pas celui du nombre de stations. La colonne "num_bikes_available_types" contient encore une structure complexe : un tableau. Il faudrait que "mechanical" et "ebike" forment deux colonnes distinctes. 

Je sais qu'il exite un module qui s'appelle flatten_json, je l'ai essayé mais j'ai eu un tableau où toutes les données sont sur une ligne donc bon...

