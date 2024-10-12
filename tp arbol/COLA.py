class colas:
    def __init__(self):
        self.elements= []

    def arrive(self,elements):
        self.elements.append(elements)

    def attention(self):
        if len(self.elements) >0:
            return self.elements.pop(0)
        else:
            return None
        
    def size(self):
        return len(self.elements)
    
    def on_front(self):
        if len(self.elements) >0:
            return self.elements[0]
        else:
            return None
        
    def move_to_end(self):
        element=self.attention()
        if element is not None:
            self.arrive(element)
    
# # arrive: agrega elementos
# # attention: elimina el primer elemento pero lo puede devolver
# # size: me devuelve el tamaño de mi cola
# # on_front: me devuelve el valor inicial pero no lo elimina
# # move_to_end: me mueve el primer elemento de la cola al final, y el 2 pasa a ser el primero