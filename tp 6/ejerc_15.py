# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.

from grafo import Graph

grafo = Graph(dirigido=False)

# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);

maravillas = [
    {"nombre": "Chichen Itza", "pais": ["Mexico"], "tipo": "arquitectónica"},
    {"nombre": "Coliseo", "pais": ["Italia"], "tipo": "arquitectónica"},
    {"nombre": "Gran Muralla China", "pais": ["China"], "tipo": "arquitectónica"},
    {"nombre": "Petra", "pais": ["Jordania"], "tipo": "arquitectónica"},
    {"nombre": "Cristo Redentor", "pais": ["Brasil"], "tipo": "arquitectónica"},
    {"nombre": "Machu Picchu", "pais": ["Peru"], "tipo": "arquitectónica"},
    {"nombre": "Taj Mahal", "pais": ["India"], "tipo": "arquitectónica"},
    {"nombre": "Amazonas", "pais": ["Brasil", "Peru", "Colombia"], "tipo": "natural"},
    {"nombre": "Halong Bay", "pais": ["Vietnam"], "tipo": "natural"},
    {"nombre": "Iguazu Falls", "pais": ["Brasil", "Argentina"], "tipo": "natural"},
    {"nombre": "Jeju Island", "pais": ["Corea del Sur"], "tipo": "natural"},
    {"nombre": "Komodo Island", "pais": ["Indonesia"], "tipo": "natural"},
    {"nombre": "Puerto Princesa Underground River", "pais": ["Filipinas"], "tipo": "natural"},
    {"nombre": "Table Mountain", "pais": ["Sudáfrica"], "tipo": "natural"}
]

for maravilla in maravillas:
    grafo.insert_vertice(maravilla["nombre"])

# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;

grafo.insert_arista('Chichen Itza', 'Coliseo', 7)
grafo.insert_arista('Chichen Itza', 'Gran Muralla China', 10)
grafo.insert_arista('Chichen Itza', 'Petra', 12)
grafo.insert_arista('Chichen Itza', 'Cristo Redentor', 8)
grafo.insert_arista('Chichen Itza', 'Machu Picchu', 9)
grafo.insert_arista('Chichen Itza', 'Taj Mahal', 15)
grafo.insert_arista('Coliseo', 'Gran Muralla China', 5)
grafo.insert_arista('Gran Muralla China', 'Petra', 6)
grafo.insert_arista('Petra', 'Cristo Redentor', 4)
grafo.insert_arista('Cristo Redentor', 'Machu Picchu', 3)
grafo.insert_arista('Machu Picchu', 'Taj Mahal', 10)

grafo.insert_arista('Amazonas', 'Halong Bay', 5)
grafo.insert_arista('Amazonas', 'Iguazu Falls', 6)
grafo.insert_arista('Amazonas', 'Jeju Island', 8)
grafo.insert_arista('Amazonas', 'Komodo Island', 7)
grafo.insert_arista('Amazonas', 'Puerto Princesa Underground River', 9)
grafo.insert_arista('Amazonas', 'Table Mountain', 10)
grafo.insert_arista('Halong Bay', 'Iguazu Falls', 4)
grafo.insert_arista('Iguazu Falls', 'Jeju Island', 5)
grafo.insert_arista('Jeju Island', 'Komodo Island', 6)
grafo.insert_arista('Komodo Island', 'Puerto Princesa Underground River', 3)
grafo.insert_arista('Puerto Princesa Underground River', 'Table Mountain', 9)


# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;

arbol_expansion_minima_arquitectonica = grafo.kruskal('Coliseo')

print("Árbol de expansión mínima de las maravillas arquitectónicas:")
for arista in arbol_expansion_minima_arquitectonica[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")


print()


arbol_expansion_minima_naturales = grafo.kruskal('Halong Bay')

print("Árbol de expansión mínima de las maravillas naturales:")
for arista in arbol_expansion_minima_naturales[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")

print()

# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;

paises_arquitectonicas = set()
paises_naturales = set()

for maravilla in maravillas:
    if maravilla['tipo'] == 'arquitectónica':
        paises_arquitectonicas.update(maravilla['pais'])

for maravilla in maravillas:
    if maravilla['tipo'] == 'natural':
        paises_naturales.update(maravilla['pais'])

paises_comunes = paises_arquitectonicas.intersection(paises_naturales)

if paises_comunes is not None:
    print("Los siguientes países tienen maravillas arquitectónicas y naturales:")
    for pais in paises_comunes:
        print(pais)
else:
    print("No existen países que contengan de maravillas arquitectónicas y naturales.")

print()

# e. determinar si algún país tiene más de una maravilla del mismo tipo;

def pais_con_multiples_maravillas(grafo, tipo):
    paises = []
    for nodo in grafo.elements:
        for maravilla in maravillas:
            if nodo['value'] == maravilla['nombre'] and maravilla['tipo'] == tipo:
                if isinstance(maravilla['pais'], list):
                    paises.extend(maravilla['pais'])
                else:
                    paises.append(maravilla['pais'])
    for pais in set(paises):
        if paises.count(pais) > 1:
            print(f"{pais} tiene más de una maravilla de tipo {tipo}")


pais_con_multiples_maravillas(grafo, 'arquitectónica')
pais_con_multiples_maravillas(grafo, 'natural')










