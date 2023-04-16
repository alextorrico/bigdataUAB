# Ejercicio de análisis de datos: Febrero en Twitch

#### 1 ¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?

Al analizar el volumen de espectadores de promedio diarios a lo largo del mes de febrero en Twitch nos encontramos el siguiente gráfico:

<img width="619" alt="image" src="https://user-images.githubusercontent.com/124086935/232320989-a074a0e7-a6c1-4784-a5c5-ca5d921dfb86.png">

Este nos muestra los diferentes picos de audiencia que se han producido y podemos ver cierta estabilidad, siempre rondando en picos máximos de unos 350.000 espectadores y picos mínimos de unos 250.000, excepto en alguna ocasión, como es el caso del 7 de febrero, con más de 350.000 mil espectadores o el 28 de febrero donde casi se alcanzaron los 450.000 mil (todos estos datos son un promedio de audiencia diario en Twitch España).

Si analizamos más en detalle estos datos, y establecemos la línea temporal en capturas de minuto a minuto podremos ver exactamente cuantos espectadores había en cada momento en Twitch, esto nos muestra **dos cosas**, podemos ver con más **detalle los diferentes picos de audiencia** producidos los días 7 de febrero (donde se llegó a alcanzar más de 800.000 mil espectadores en diversas ocasiones) o la noche del 27 al 28 de febrero donde se alcanza picos de más de 1.500.000 espectadores. Aparte nos muestra **la tendencia cíclica de la audiencia**; los mayores volúmenes de espectadores se producen por la noche, y es donde se concentra la mayor actividad en la plataforma, mientras que durante el día es cuando se producen los números más bajos de audiencia:

<img width="620" alt="image" src="https://user-images.githubusercontent.com/124086935/232321104-ff560ff9-4913-4d45-b6e6-880ca1236b6b.png">

Por último, en este gráfico se muestra una clasificación de los días con mayor promedio de audiencia durante el mes de febrero de 2023, aquí podemos ver de forma clara el efecto de los diferentes picos de audiencia que hemos visto anteriormente, siendo los días con más promedio de audiencia el día 7 de febrero y el día 28:

<img width="620" alt="image" src="https://user-images.githubusercontent.com/124086935/232321143-66d2a729-9a29-4d56-b51b-975748898d64.png">

#### 2 ¿Cuáles son las categorías más vistas y en las que más horas de directo se han realizado?

En el siguiente gráfico podemos ver las categorías más consumidas, ponemos un poco de contexto para explicar estos datos y comprenderlos mejor vemos que la categoría Just Chating está muy separada del resto con un margen de más de 110 millones de espectadores, esto se debe a que muchos directos de Twitch (la gran mayoría) antes de empezar con su propósito, como puede ser un GamePlay, primero aparece hablando el interlocutor, lo que hace que el directo ya sea clasificado como Just Chating.

Siguiendo con el análisis, otra información cuantitativa que nos proporciona este gráfico es una clasificación clara de los juegos que más interés despiertan o que son tendencia durante este mes, y esto hace que podamos comparar el impacto de juegos estrenados con anterioridad, como puede ser un Minecraft o un Valorant y compararlos con un juego recientemente estrenado como Hogwards Legacy y entender que para un juego nuevo, son números considerablemente bajos.

<img width="620" alt="image" src="https://user-images.githubusercontent.com/124086935/232321198-62d88c5c-2c68-42e1-a75c-6d13be09e1a2.png">


Después en el siguiente gráfico podemos ver de estas categorías anteriores, cuáles han tenido el mayor número de horas de directo, esto nos sirve para ver si coinciden las categorías más vistas con las que más horas se han producido, y podemos ver que por lo general sí que se cumple la norma de que las categorías más vistas son las que con más horas de directo cuentan.

<img width="620" alt="image" src="https://user-images.githubusercontent.com/124086935/232321240-51a28221-fc1d-44ef-ae0f-3a24079e3d24.png">

En el siguiente gráfico de dispersión podemos ver más claramente donde se sitúan las diferentes categorías teniendo en cuenta las horas de directo relacionadas con los espectadores. Podemos, por ejemplo, coger las dos categorías más vistas (sin contar Just Chating), Sports y Minecraft, si observamos estas dos categorías en el gráfico podemos observar que Sports (70 millones de visualizaciones) con muchas menos horas de directo obtiene casi 15 millones más de espectadores que Minecraft que cuenta con más de horas de directo y acumula 55 millones de visualizaciones

<img width="565" alt="image" src="https://user-images.githubusercontent.com/124086935/232321332-cebea6f8-510c-433c-a23d-3340ee5ce234.png">


### 3 ¿Cómo han evolucionado (captura a captura) estas categorías a lo largo del mes?

En el siguiente gráfico podemos ver cómo han ido evolucionando las diferentes categorías a lo largo del mes de febrero, a continuación analizaremos algunas categorías destacadas.

<img width="610" alt="image" src="https://user-images.githubusercontent.com/124086935/232321411-7dcd0071-6c75-4e07-8504-b15535436231.png">

Como por ejemplo Sports:

Como hemos visto anteriormente, con relativamente pocas horas de directo ha acumulado unos números de audiencia muy favorables con picos de audiencia que han alcanzado los más de 1.3 millones de espectadores y por lo general la categoría ha mantenido una línea de tendencia ascendiente:

<img width="498" alt="image" src="https://user-images.githubusercontent.com/124086935/232321450-fa25ea32-9cbd-4d8a-8bce-5ce6034b0e92.png">

Sí observamos Minecraft:

También ha mantenido una tendencia creciente y ha tenido algún pico de más de un millón de espectadores:

<img width="498" alt="image" src="https://user-images.githubusercontent.com/124086935/232321491-92dd681f-7cb4-49f6-bc7a-e140456e3870.png">

En contraste, si observamos Hogwards Legacy, un juego recién estrenado:

Podemos ver que no solo no ha conseguido unos picos de audiencia relevantes, sino que con el tiempo su línea de tendencia ha ido en descenso y prácticamente tiene una actividad nula respecto a otras categorías:

<img width="497" alt="image" src="https://user-images.githubusercontent.com/124086935/232321548-565e11eb-5622-4eb8-b21f-35aa669a6e2e.png">

En el gráfico siguiente podemos ver como se han distribuido los volúmenes de audiencia según las diferentes categorías, vemos que las categorías principales nombradas anteriormente se quedan con la mayoría de los espectadores, mientras que el resto se reparte en muchas categorías más pequeñas que dejan una distribución de la audiencia muy polarizada:

<img width="563" alt="image" src="https://user-images.githubusercontent.com/124086935/232321575-0ac766e4-7933-4764-b362-e16740009996.png">

### 4.¿Cuál es la distribución de los streamers si los clasificamos por volúmenes de audiencia y horas realizadas?

Para entender el siguiente gráfico hay que tener presente que un mes cuenta con aproximadamente 730 horas.

En la siguiente tabla se muestran los canales de Twitch que más horas de directo han realizado durante el mes de febrero, podemos ver que muchos de ellos alcanzan las más de 600 horas, lo que nos indica que han estado en directo sin parar durante todo el mes:

Horas:

<img width="596" alt="image" src="https://user-images.githubusercontent.com/124086935/232321650-1e9891c5-417a-47a9-88ba-4fc31f813a97.png">

En el siguiente gráfico se muestran los canales de twitch que más audiencia han acumulado durante el mes de febrero de 2023, como podemos ver ninguno de los canales anteriores aparece en el siguiente gráfico, lo que nos indica que por muchas horas de directo que realices no te garantiza tener audiencia.

Los dos canales más destacados con KingsLeague y Ibai, ambos pertenecen a alguna de las categorías con más espectadores que hemos visto anteriormente, la KingsLeague e Ibai a Sports y Ibai a JustChating y otras categorías también importantes

Audiencia:
<img width="606" alt="image" src="https://user-images.githubusercontent.com/124086935/232321680-a58bb363-f309-47bf-a97c-359aea1e6406.png">

En este gráfico de dispersión se sitúan los canales más visualizados respecto a las horas de directo que han realizado, vemos como la gran mayoría de canales rondan las 100 horas en adelante y no tienen un nivel de audiencia que destaque del grupo.

Pero después observamos los canales más importantes como pueden ser: Kings League, Ibai, El Spreen, juansguarnizo, AuronPlay, El Xokas, etc. que sin realizar un número disparatado de horas, alcanzan niveles de audiencia importantes:

Comparación:

<img width="606" alt="image" src="https://user-images.githubusercontent.com/124086935/232321723-8d17bcff-1d3d-428e-a939-54ce12d872b0.png">

### 5.¿Cuál ha sido la evolución (captura a captura) de la desviación estándar en el volúmen de espectadores? ¿En qué momentos las audiencias se encuentran más polarizadas y en qué momentos la distribución es más uniforme?

Como podemos observar, la desviación estándar ha seguido un patrón cíclico a lo largo del mes, siendo en la tarde-noche los momentos donde esta ha sido más grande y durante el día la desviación estándar tenía unos números más bajos, siempre rondando 40, con una mínima de 33 el día 26 de febrero
En los momentos donde la desviación estándar era más alta se pueden observar picos, como por ejemplo en los días 7, 13 y 20 de febrero, con una máxima el día 26, donde la desviación estándar alcanzo 8.332

<img width="533" alt="image" src="https://user-images.githubusercontent.com/124086935/232321763-1dbf3e24-8563-422a-85e0-0ec074eed579.png">




