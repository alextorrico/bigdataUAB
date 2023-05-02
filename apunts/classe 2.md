### Imprimir una llista amb bucle for
#### cadena:

```Python
llista = ['jaume', "carmen"]

for cada_cosa in llista:
    print(cada_cosa)
```
#### integers:
```Python

llista = [1, 2]

for cada_cosa in llista:
    print(cada_cosa + 4)

```
### Afegir elements a una llista:
##### Utilitzem un bucle for
```Python
llista = ['jaume', "carmen"]

for nom in llista:
    print(nom)

llista = ['jaume', "carmen"]

nou_nom = "rafa"

llista_nova = llista.append(nou_nom)

print(llista_nova)

```

### Condicionals:
##### Else / if:
```Python

llista_noms = ['joan', "carmen", "shakira"]
'''
per igualar el condicional: ==
'''

for nom in llista_noms:
    if nom == 'joan':
        print(nom + ' si que es en joan')
    else:
        print(nom + ' no es en joan')
        
        
    
numeros = [1,2,3,6,7,8,10,15]

```

#### Elif:
##### Més de dues alternatives:
```Python
for n in numeros:
    if n < 6:
        print(n , ' es menor que 6')
    elif n == 6:
        print (n , ' es igual a 6')
    else:
        print (n , 'es major que 6')
        
quants numeros hi ha en l'string:

numeros = [1,2,3,6,7,8,10,15,5]


print(len(numeros))

```

### Funció len:
##### Ens diu la longitud:
```Python
llargaria = len(numeros)
print(llargaria)

```

### Activitats:
```Python
texto = 'esto es un ejrcicio'

print(texto)

nota = 8,75

nom_classe = 'analitica digital'


print ('en la classe de ', nom_classe, 'he tret un', nota)

````
#### Activitat 1:
```Python
nota = 10
frase = 'en la classe de ', nom_classe, 'he tret un', nota

print(frase)
```

###### Pasos:
```Python 
notas = ["5","7","6","4","8","2"]
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]

'''
sumar 1 punto a todas las notas
'''

for nota in notas:
    nota_numerica = int(nota)
    print(nota_numerica + 1)

'''
sumar 1 punto a todas las notas y imprimir la nota al costat de cada alumne 
'''

for nota, nom in zip(notas, alumnos):
    nota_numerica = int(nota)
    nota_final = nota_numerica +1
    print(nota_final, nom)

esta el nom a la llista?
llista = ["jaume","carla","pere","adrià","rafael","agnès","joan"]

nom = 'joan'

if nom in llista:
    print('si')
    position = llista.index(nom)
    print(position)
else:
    print('no')


'''identifica valors duplicats per no contar mes dun cop
'''
llista = ["jaume","carla","pere","adrià","rafael","agnès","joan","carla"]

valors_unics = set(llista)
print(len(valors_unics))

mes optim:
print(len(set(llista)))

```

### Activitat 2:
```Python 

llista = [
    "david",
    "dani",
    "marta",
    "jaume",
    "adria",
    "carla",
    "joan",
    "pere",
    "carla",
    "pere",
    "adria",
    "quico",
    "pere",
    "joan",
    "agustí",
    "adria",
    "joan",
    "adria",
    "siscu",
    "carles",
    "dani",
    "carla"
]
```
#### Pasos:
```Python 
'''
cuantas personas han asistido?
'''
llista_unics= set(llista)
print(f"Han vingut {len(llista_unics)} alumnes")

'''
cuantas personas han assistido a mas de dos sesiones?
'''

llista_repetits = []
contador = 0

for nom in llista_unics:
    valor= llista.count(nom)
    if valor > 1:
        llista_repetits.append(nom)
        contador = contador+1
print(f"Han repetit {len(llista_repetits)} alumnes")
print(contador)


# qué porcentahe de os asistenetes accedena mas de dos sesiones

porcentaje = (contador/len(llista_unics))*100

print(f"El percentatge d'asistencia es del {porcentaje}%")


# Activitat B

notes = ["5","3","7","8","9.5","4","6,2"]
alumnes = ["adria","agnès","josep","rafa","cristina","Gemma","Eduard"]

# crea un codigo que imprima para cada alumno la nota correspondiente con el texto


notas_bones = notes[6].replace(",", ".")
print(notas_bones)

for nota, nom in zip(notes, alumnes):
   print (nota, nom)

# calcula el promig de notes del aula

notes_arreglades =[]
for nota, nom in zip(notes, alumnes):
   print (nota, nom)
   if "." in nota:
      nota_arreglada = float(nota)
      notes_arreglades.append(nota_arreglada)
   elif "," in nota:
      nota_arreglada = float(nota.replace(",","."))
      notes_arreglades.append(nota_arreglada)
   else:
      nota_arreglada = int(nota)
      notes_arreglades.append(nota_arreglada)
print(notes_arreglades)

#calcul del promig

nota_final = sum(notes_arreglades)/len(notes_arreglades)
print(round(nota_final,2))

#nota maxima

nota_maxima= max(notes_arreglades)
posicio = notes_arreglades.index(nota_maxima)
print(f"la maxima nota es un {nota_maxima}, i l'ha tret {alumnes[posicio]}")

#nota minima
nota_maxima= min(notes_arreglades)
posicio = notes_arreglades.index(nota_maxima)
print(f"la minima nota es un {nota_maxima}, i l'ha tret {alumnes[posicio]}")
