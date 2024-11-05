from grafo import Graph  
from arbol import BinaryTree
from arbol_avl import BinaryTree


grafo_star_wars = Graph(dirigido=False)

#A)D)
grafo_star_wars.insert_vertice("Luke Skywalker")
grafo_star_wars.insert_vertice("Darth Vader")
grafo_star_wars.insert_vertice("Leia Organa")
grafo_star_wars.insert_vertice("Han Solo")
grafo_star_wars.insert_vertice("Yoda")
grafo_star_wars.insert_vertice("Chewbacca")
grafo_star_wars.insert_vertice("Obi-Wan Kenobi")
grafo_star_wars.insert_vertice("Padmé Amidala")
grafo_star_wars.insert_vertice("Boba Fett")
grafo_star_wars.insert_vertice("C-3PO")
grafo_star_wars.insert_vertice("Rey")
grafo_star_wars.insert_vertice("Kylo Ren")
grafo_star_wars.insert_vertice("R2-D2")
grafo_star_wars.insert_vertice("BB-8")

grafo_star_wars.insert_arista("Luke Skywalker", "Darth Vader", 5)  
grafo_star_wars.insert_arista("Leia Organa", "Luke Skywalker", 4)  
grafo_star_wars.insert_arista("Han Solo", "Leia Organa", 3)  
grafo_star_wars.insert_arista("Yoda", "Luke Skywalker", 2)  
grafo_star_wars.insert_arista("Chewbacca", "Han Solo", 6)  
grafo_star_wars.insert_arista("Obi-Wan Kenobi", "Anakin Skywalker", 4)  
grafo_star_wars.insert_arista("Padmé Amidala", "Anakin Skywalker", 5)  
grafo_star_wars.insert_arista("R2-D2", "C-3PO", 9)                 
grafo_star_wars.insert_arista("BB-8", "Rey", 3)                    
grafo_star_wars.insert_arista("Rey", "Kylo Ren", 4)                
grafo_star_wars.insert_arista("Han Solo", "Kylo Ren", 1)           
grafo_star_wars.insert_arista("Chewbacca", "Leia Organa", 2)       

grafo_star_wars.show_graph()


#B)
print()
print("arbol expansion minimo")
arbol_expansion_minima = grafo_star_wars.kruskal(None)
print(arbol_expansion_minima)
print()
yoda_en_arbol = any("Yoda" in arbol for arbol in arbol_expansion_minima)
if yoda_en_arbol:
    print("Yoda está presente en el árbol de expansión mínima.")
else:
    print("Yoda NO está presente en el árbol de expansión mínima.")


#C)
print()
def find_max_shared_episodes(graph):
    max_episodes = 0
    characters = (None, None)
    
    for node in graph.elements:
        for adjacent in node['aristas']:
            if adjacent['peso'] > max_episodes:
                max_episodes = adjacent['peso']
                characters = (node['value'], adjacent['value'])
    
    return max_episodes, characters
max_episodes, (char1, char2) = find_max_shared_episodes(grafo_star_wars)
print(f"Los personajes que comparten el mayor número de episodios son: {char1} y {char2} con {max_episodes} episodios juntos.")


#Elian CrUZ 4/11/24 Hora: 22:36