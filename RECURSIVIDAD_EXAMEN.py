lista=[1,2,3,4,5,6,7,8,9,10]

def Inversa(lista):
    if (len(lista)-1) < 0:
        return 0
    else:
        print(lista[-1])
        return Inversa(lista[:-1])
Inversa(lista) 