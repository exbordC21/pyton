# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
from grafo import Graph


# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

ambientes = ["cocina", "comedor", "cochera", "quincho" ," baño 1" , "baño 2", "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

grafos = Graph(dirigido=False)
for ambiente in ambientes:
    nodo = {
        'value': ambiente,
        'aristas': [],
        }
    grafos.insert_vertice(ambiente)


# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

grafos.insert_arista('cocina','comedor',1)
grafos.insert_arista('cocina','cochera',2)
grafos.insert_arista('cocina','baño 1',3)
grafos.insert_arista('cocina','baño 2',4)
grafos.insert_arista('cocina','quincho',5)
grafos.insert_arista('comedor','cochera',1)
grafos.insert_arista('comedor','quincho',2)
grafos.insert_arista('comedor','baño 2',3)
grafos.insert_arista('comedor','habitacion 1',4)
grafos.insert_arista('comedor','baño 1',5)
grafos.insert_arista('cochera','quincho',1)
grafos.insert_arista('cochera','baño 1',2)
grafos.insert_arista('cochera','baño 2',3)
grafos.insert_arista('quincho',' baño 1',1)
grafos.insert_arista('quincho','baño 2',2)
grafos.insert_arista('quincho','habitación 1',3)
grafos.insert_arista('baño 1','baño 2',1)
grafos.insert_arista('baño 1','habitación 1',2)
grafos.insert_arista('baño 1','habitación 2',3)
grafos.insert_arista('baño 2','habitación 1',1)
grafos.insert_arista('baño 2','habitación 2',2)
grafos.insert_arista('baño 2','sala de estar',3)
grafos.insert_arista('habitación 1','habitación 2',1)
grafos.insert_arista('habitación 1','baño 1',2)
grafos.insert_arista('habitación 1','terraza',3)
grafos.insert_arista('habitación 2','sala de estar',1)
grafos.insert_arista('habitación 2','terraza',2)
grafos.insert_arista('habitación 2','cocina',3)
grafos.insert_arista('sala de estar','terraza',1)
grafos.insert_arista('sala de estar','cocina',2)
grafos.insert_arista('sala de estar','comedor',3)
grafos.insert_arista('terraza','cocina',1)
grafos.insert_arista('terraza','comedor',2)
grafos.insert_arista('terraza','cochera',3)
grafos.insert_arista('patio','cocina',1)
grafos.insert_arista('patio','comedor',2)
grafos.insert_arista('patio','cochera',3)


grafos.show_graph()

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes

arbol_expansion_minima = grafos.kruskal('baño 1')

total_cable = 0



for arista in arbol_expansion_minima[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")

print()


def mostrar_metros_cables():
    total_cable = 0

    for arista in arbol_expansion_minima[0].split(';'):
        if arista is not None:
            lista_arista = arista.split('-')
            if len(lista_arista) == 3:
                origen, destino, peso = lista_arista
                peso = int(peso)  
                total_cable += peso
                print(f"origen: {origen} -> destino: {destino} peso: {peso}")

    print(f"Total de metros de cable necesarios: {total_cable} metros")

mostrar_metros_cables()


print()

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
def mostrar_camino_corto(origen, destino):
    camino = grafos.dijkstra(origen)
    destino = destino
    peso_total = None
    camino_completo = []
    while camino.size() > 0:
        value = camino.pop()
        if value[1][0] == destino:
            if peso_total is None:
                peso_total = value[0]
            camino_completo.append(value[1][0])
            destino = value[1][2]
    camino_completo.reverse()
    print(f"el camino mas corto es: {'-'.join(camino_completo)} y los metros necesarios de cable es de {peso_total}m")

mostrar_camino_corto('habitación 1', 'sala de estar')






