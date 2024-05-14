# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c. Utilizar un vector para representar la mochila.


mochila=["sable","comida","posion","papa"]

def usarlafuerza(mochila,i=0):
    if len(mochila)==0:
        return print("la mochila esta vacia")
    elif len(mochila)==i:
        return print("no se encontro el sable ")
    elif mochila[i]=="sable":
        return print("se encontro el sable de luz, la cantidad de elementos eliminados para poder encontrarlo fueron de: ",i)
    else:
        return usarlafuerza(mochila,i+1)

objetos=usarlafuerza(mochila)
    
    
    
