class Stack:

        def __init__(self):
            self.elements =[]

        def push(self,element):
            self.elements.append(element)

        def pop(self):
            if len(self.elements) > 0:
                return self.elements.pop()
            else:
                return None

        def on_top(self):
            if len(self.elements) > 0:
                return self.elements[-1]
            else:
                return None

        def size(self):
            return len(self.elements)


dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": 7000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": 6000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": 15,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": 56000,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": 5000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": 10000,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": 2000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": 23000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": 15000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": 6000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": 2500,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": 1500,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": 2700,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": 5000,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": 25,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": 200,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": 450,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": 15000,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

pila=Stack()
pila_aux=Stack()
pila_A_Q_S=Stack()

for element in dinosaurios:
    pila.push(element)


# a) Contar cuantas especies hay;
print()
def especies(pila,pila_aux):
    lista_dinosaurios=[]
    while pila.size() > 0:
            if lista_dinosaurios.count(pila.on_top()['especie'])==0:
                lista_dinosaurios.append(pila.on_top()['especie'])
                pila_aux.push(pila.pop())
            else:
                pila_aux.push(pila.pop())
    return len(lista_dinosaurios)
print("la cantidad de especies es de :",especies(pila,pila_aux))

def Ordenarpila(pila, pila_aux):
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
Ordenarpila(pila, pila_aux)


# b) Determinar cuantos descubridores distintos hay;
print()
def descubridores(pila,pila_aux):
    lista_dinosaurios=[]
    while pila.size() > 0:
            if lista_dinosaurios.count(pila.on_top()['descubridor'])==0:
                lista_dinosaurios.append(pila.on_top()['descubridor'])
                pila_aux.push(pila.pop())
            else:
                pila_aux.push(pila.pop())
    return len(lista_dinosaurios)
print("la cantidad de descubridores es de :",descubridores(pila,pila_aux))

def Ordenarpila(pila, pila_aux):
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
Ordenarpila(pila, pila_aux)


# c) Mostrar todos los dinosaurios que empiecen con T;
print()
def nombre_con_T(pila,pila_aux):
    nombre_T = []
    for i in range(pila.size()):
        if pila.on_top()['nombre'].startswith(('T')):
            nombre_T.append(pila.on_top()['nombre'])
            pila_aux.push(pila.pop())
        else:
            pila_aux.push(pila.pop())
    return(nombre_T)
print("los nombres que empiezan con T son:",nombre_con_T(pila,pila_aux))

def Ordenarpila(pila, pila_aux):
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
Ordenarpila(pila, pila_aux)


# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
print()
def por_peso(pila,pila_aux):
    lista_men_275 = []
    for i in range (pila.size()):
        if pila.on_top()['peso']<275:
            lista_men_275.append(pila.on_top()['nombre'])
            pila_aux.push(pila.pop())
        else:
            pila_aux.push(pila.pop())
    return(lista_men_275)
print("Los que pesan menos de 275 son",por_peso(pila,pila_aux))

def Ordenarpila(pila, pila_aux):
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
Ordenarpila(pila, pila_aux)


# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;
print()
def nombre_A_Q_S(pila,pila_A_Q_S,pila_aux):
    for i in range(pila.size()):
        if pila.on_top()['nombre'].startswith(('A','Q','S')):
            pila_A_Q_S.push(pila.on_top()['nombre'])
            pila_aux.push(pila.pop())
        else:
            pila_aux.push(pila.pop())
    return()
nombre_A_Q_S(pila,pila_A_Q_S,pila_aux)
print("los nombres que empiezan con A, Q y S son:",pila_A_Q_S.elements)

def Ordenarpila(pila, pila_aux):
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
Ordenarpila(pila, pila_aux) 