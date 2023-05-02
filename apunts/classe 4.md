###  Twitch API 
Hem d'importar la API de Twitch i tot el que necessitarem pel nostre projecte:
```Python

import pandas as pd
from twitchAPI.twitch import Twitch
from pprint import pprint
import json
import pandas as pd
import datetime
import time

now = datetime.datetime.now()
```
Per poder imporatr les dades ens hem de registrar com a desenvolupadors i utilitzar les nostres credencials personals:
```Python

twitch = Twitch('vj6x51xitd3q6lrrhsm47fzdzekmht', 'm1i5cbhzucnz8bvqf8thdmven2zpb3')
pprint(twitch.get_users(logins=['alexalexales']))

```
### Hem de decidir quines dades volem utilitzar i quines no, per optimitzar recursos:
```Python 

llista_dataframes=[]
cursor_dummy = None

def crida(cursor):
    streams = twitch.get_streams(first=20, language='ca', after=cursor) #funcio que ens baixa els streams de twitch


    dades = streams['data']



    for dada in dades:
        captured_at = now
        user_id = dada['user_id']
        user_name = dada['user_name']
        game_id = dada['game_id']
        game_name = dada['game_name']
        title = dada['title']
        viewer_count = dada['viewer_count']
        started_at = dada['started_at']
        is_mature = ['is_mature']

        df =pd.DataFrame({
            'captured_at': captured_at,
            'user_id': user_id,
            'user_name': user_name,
            'game_id': game_id,
            'game_name': game_name,
            'title': title,
            'viewer_count': viewer_count,
            'started_at:': started_at,
            'is_mature': is_mature,
        }, index=[0])
        llista_dataframes.append(df)

    print(len(llista_dataframes))

    try:
        cursor = streams['pagination']['cursor']
        print(cursor)
        print('dormint')
        time.sleep(1)
        crida(cursor)

    except KeyError:
        print('ultima pagina')
        pass



crida(cursor_dummy)

final_dataframe = pd.concat(llista_dataframes)
final_dataframe.to_csv('export.csv', index=False)
    #print(final_dataframe)

```
