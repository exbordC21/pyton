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


pilaepi5 = Stack()
pilaepi7 = Stack()
pila_iguales = Stack()
pila_aux2 = Stack()

nombresepi5=["Anakin Skywalker","Princess Leia","Han Solo"]
nombresepi7=["R2-D2","Luke Skywalker","Anakin Skywalker"]

for element in nombresepi5:
    pilaepi5.push(element)

for element2 in nombresepi7:
    pilaepi7.push(element2)

def interseccion_pilas(pilaepi5, pilaepi7):
    return list(set(pilaepi5.elements) & set(pilaepi7.elements))

print(interseccion_pilas(pilaepi5,pilaepi7))
