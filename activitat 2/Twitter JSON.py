# Tableau:
  

import pandas as pd
import json
import glob


files = glob.glob('api_responses/*.json') # Seleccionamos todos los archivos json com * los selecciona todos
llista_dfs = [] # Crear una lista vacía para almacenar el dataframe


for file in files:
    with open(file, encoding="utf-8") as jsonfiles: # bucle para abrir los archivo json
        dades = json.load(jsonfiles)
        tweets = dades["data"] # los datos que queremos estan en "data"
        print(len(tweets))  # dice la cantidad de tweets


        for tweet in tweets: # cogemos lo que queremos de cada tweet, las diferentes variables
            author_id = tweet["author_id"]
            text = tweet["text"]
            created_at = tweet["created_at"]
            possibly_sensitive = tweet["possibly_sensitive"]
            retweet_count = tweet["public_metrics"]["retweet_count"]
            reply_count = tweet["public_metrics"]["reply_count"]
            like_count = tweet["public_metrics"]["like_count"]
            quote_count = tweet["public_metrics"]["quote_count"]
            impression_count = tweet["public_metrics"]["impression_count"]
            lang = tweet["lang"]
            users = dades["includes"]["users"]
            hashtags = tweet["entities"]["hashtags"]["tag"]


            for user in users:
                if user["id"] == author_id:
                    user_name = user["username"] # cogemos el user que esta en un apartado diferente a los datos anteriores
                    print(user["id"], user["username"])
                    followers = user["public_metrics"]["followers_count"]
                else:
                    pass


            df = pd.DataFrame({  # creamos un dataframe con todos los datos que hemos extraido de los archvos jason
                "user_id": author_id,
                "user_name": user_name,
                "followers": followers,
                "text": text,
                "lang": lang,
                "created_at": created_at,
                "impression_count": impression_count,
                "retweet_count": retweet_count,
                "reply_count": reply_count,
                "quote_count": quote_count,
                "possibly_sensitive": possibly_sensitive,
                "hashtags": hashtags,

            }, index=[0])

            print(df)
            llista_dfs.append(df)  # ponemos el dataframe en una lista


df_final = pd.concat(llista_dfs) # concatenamos todos los dataframe de los archivos json en una lista
df_final.to_csv("final_tableau.csv") # exportamos el archivo csv


# Gephi:
  

import pandas as pd
import glob
import json

files = glob.glob('api_responses/*.json') # abrimos todos los archivos json amb *


users_mentions = {} # creamos un diccionario para meter todas las menciones 


for file in files:
    with open(file, encoding="utf-8") as jsonfiles:  # recorremos todos los archivos json para acceder a los datos
        dades = json.load(jsonfiles)

        tweets = dades["data"] # los datos que queremos estan en "data"
        users_data = dades["includes"]["users"]
        print(len(tweets))

        for tweet in tweets: # entramos en cada tweet, en los diferentes subapartados para encontrar las menciones 
            author_id = tweet["author_id"]
            for user in users_data:
                if user["id"] == author_id:
                    user_name = user["username"]
                    if user_name not in users_mentions:
                        users_mentions[user_name] = []
                    if "entities" in tweet and "mentions" in tweet["entities"]:
                        for mention in tweet["entities"]["mentions"]:
                            mention_name = mention["username"]
                            if mention_name not in users_mentions[user_name]:
                                users_mentions[user_name].append(mention_name)


data = {"target": [], "source": []} # creamos un dataframe para almacenar las menciones y los usuarios que mencionan
for user, mentions in users_mentions.items():
    for mention in mentions:
        data["target"].append(user) # los usuarios los llamamos target 
        data["source"].append(mention) # las menciones son source
df = pd.DataFrame(data)
df.to_csv("final_gephi.csv", index=False) # exportamos un csv


for user, mentions in users_mentions.items():
    for mention in mentions:
        print(f"{user} mencionó a {mention}")
