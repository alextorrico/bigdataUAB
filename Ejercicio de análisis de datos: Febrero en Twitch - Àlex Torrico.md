```python

import pandas as pd  
```
Primero de todo necesitamos importar la libreria de Pandas

### 1 ¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?  
#### Volem saber quan es fa la captura:  
```Python
  
df = pd.read_csv('feb_23_es_simple.csv',sep="\t")  
  
df_sum = df.groupby(['captured_at'])['viewer_count'].sum().reset_index()  

df_sum.to_csv('1.csv')  
```

Con la función grupby. nos permite seleccionar los datos que queremos utilizar del Data Seet orginal y combinarlos de una nueva forma que se adapte a lo que necesitamos; en este caso necesitamos saber Viewer Count y en que momento se realizo la captura

  
### 2 ¿Cuales son las categorías más vistas y en las que más horas de directo se han realizado?  
```Python
  
list_audiencia = []  
list_hores = []  
  
df = pd.read_csv('feb_23_es_simple.csv',sep="\t")  
  
df_audiencia = df.groupby('game_name')['viewer_count'].sum().reset_index()  
df_hores = df.groupby('game_name').size().transform(lambda x: x*0.25).reset_index(name='hores')  
  
  
list_audiencia.append(df_audiencia)  
list_hores.append(df_hores)  
  
df_audiencia_final = pd.concat(list_audiencia).groupby('game_name')['viewer_count'].sum().reset_index()  
df_hores_final = pd.concat(list_hores).groupby('game_name')['hores'].sum().reset_index()  
df_final = df_audiencia_final.merge(df_hores_final)  
  
df_final.to_csv('2.csv', decimal=',', index=False) #para substituir el "." por una ","
  
```

En este caso sucede igual que en el anterior, escogemos los datos que necesitamos, pero en esta parte del ejercicio necestiamos transformar las capturas para obtener las horas, ya que no tenemos este dato como tal, pero sabemos que cada captura es un cuarto de hora (asi que multiplicaresmo cada captura por 0.25) y obtendremos cuantas horas de directo tiene cada categoria.
Despues lo concatenaremos todo en una lista y exportaremos el .csv 
  
### 3 ¿Como han evolucionado (captura a captura) estas categorias a lo largo del mes?  
```Python
  
df = pd.read_csv('feb_23_es_simple.csv',sep="\t")  
  
df_sum3 = df.groupby(['captured_at','game_name'])['viewer_count'].sum().reset_index()  
df_sum3.to_csv('3.csv')  
```
Es realizar la misma operacion que en el 1 pero ahora necesitamos el nombre de la categoria (game_name) y el momento de la captura


### 4.¿Cuál es la distribución de los streamers si los clasificamos por volumenes de audiencia y horas realizadas?  
```Python
  
list_audiencia = []  
list_hores = []  
  
df = pd.read_csv('feb_23_es_simple.csv',sep="\t")  
  
df_audiencia = df.groupby('streamer_name')['viewer_count'].sum().reset_index()  
df_hores = df.groupby('streamer_name').size().transform(lambda x: x*0.25).reset_index(name='hores')  
  
  
list_audiencia.append(df_audiencia)  
list_hores.append(df_hores)  
  
df_audiencia_final = pd.concat(list_audiencia).groupby('streamer_name')['viewer_count'].sum().reset_index()  
df_hores_final = pd.concat(list_hores).groupby('streamer_name')['hores'].sum().reset_index()  
df_final = df_audiencia_final.merge(df_hores_final)  
  
df_final.to_csv('4.csv', decimal=',', index=False)  
```

Aqui relizamos un poco el mismo proceso que el 2, pero en vez de utilizar las categorias, necesitamos el nombre de los Streamers, los relacionamos/agrupamos con Viewer_Count y hacemos el mismo porceso de conteo para obtener elas horas de directo que han realizado, multiplicando por 0.25.

  
### 5.¿Cuál ha sido la evolución (captura a captura) de la desviación estándar en el volúmen de espectadores? ¿En qué momentos las audiencias se encuentran más polarizadas y en qué momentos la distribución es más uniforme?  
```Python
  
  
df = pd.read_csv('feb_23_es_simple.csv',sep="\t")  
  
df_sum = df.groupby(['captured_at'])['viewer_count'].std().reset_index()  
  
df_sum.to_csv('5.csv', decimal=',', index=False)

```
Es realizar la misma operacion que en el 1 pero cambiando el - .sum().reset_index() - por - .std().reset_index() - para de esta forma obtener la desviación estandar 
