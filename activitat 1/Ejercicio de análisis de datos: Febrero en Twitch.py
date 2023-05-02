import pandas as pd

# 1 ¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?

df = pd.read_csv('feb_23_es_simple.csv',sep="\t") # lee el archivo .csv

df_sum = df.groupby(['captured_at'])['viewer_count'].sum().reset_index() #grupby nos permite coger los datos que necesitamos i agruparlos
df_sum.to_csv('1.csv') #exporta en .csv un nuevo dataset


# 2 ¿Cuales son las categorías más vistas y en las que más horas de directo se han realizado?

list_audiencia = []
list_hores = []

df = pd.read_csv('feb_23_es_simple.csv',sep="\t")

df_audiencia = df.groupby('game_name')['viewer_count'].sum().reset_index() # cogemos los archivos que necesitamos y agrupamos
df_hores = df.groupby('game_name').size().transform(lambda x: x*0.25).reset_index(name='hores') #sabemso que cada captura son 15 min i transformamos el numero por 0.25 para obtener el numero de horas


list_audiencia.append(df_audiencia) # añadimos a la lista el df(dataframe)
list_hores.append(df_hores) #añadimos a la lista el df

df_audiencia_final = pd.concat(list_audiencia).groupby('game_name')['viewer_count'].sum().reset_index()
df_hores_final = pd.concat(list_hores).groupby('game_name')['hores'].sum().reset_index()
df_final = df_audiencia_final.merge(df_hores_final) # juntamos las listas

df_final.to_csv('2.csv', decimal=',', index=False) #exportamos



#3 ¿Como han evolucionado (captura a captura) estas categorias a lo largo del mes?

df = pd.read_csv('feb_23_es_simple.csv',sep="\t")

df_sum3 = df.groupby(['captured_at','game_name'])['viewer_count'].sum().reset_index() #como en el primero pero con las categorias (game_name)
df_sum3.to_csv('3.csv')


#4.¿Cuál es la distribución de los streamers si los clasificamos por volumenes de audiencia y horas realizadas?

list_audiencia = []
list_hores = []

df = pd.read_csv('feb_23_es_simple.csv',sep="\t")

df_audiencia = df.groupby('streamer_name')['viewer_count'].sum().reset_index()
df_hores = df.groupby('streamer_name').size().transform(lambda x: x*0.25).reset_index(name='hores') #hacemos igual que en el 2 pero con los streamers (streamer_name)


list_audiencia.append(df_audiencia)
list_hores.append(df_hores)

df_audiencia_final = pd.concat(list_audiencia).groupby('streamer_name')['viewer_count'].sum().reset_index()
df_hores_final = pd.concat(list_hores).groupby('streamer_name')['hores'].sum().reset_index()
df_final = df_audiencia_final.merge(df_hores_final)

df_final.to_csv('4.csv', decimal=',', index=False)



#5.¿Cuál ha sido la evolución (captura a captura) de la desviación estándar en el volúmen de espectadores? ¿En qué momentos las audiencias se encuentran más polarizadas y en qué momentos la distribución es más uniforme?


df = pd.read_csv('feb_23_es_simple.csv',sep="\t")

df_sum = df.groupby(['captured_at'])['viewer_count'].std().reset_index()#funcion std nos promorciona la desviacion estandar, la substitumos por .suma

df_sum.to_csv('5.csv', decimal=',', index=False) # subtituimos el "." por ","
