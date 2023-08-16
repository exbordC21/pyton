regularizados=int(input("ingrese los alumnos regularez"))
desaprobados=int(input("ingrese los alumnos desaprobados"))
promocionado=int(input("ingrese los alumnos promocionados"))
libres=int(input("ingrese los alumnos libres"))
totalalum= regularizados + desaprobados + promocionado + libres

regulares= regularizados * 100 / totalalum
desaproba= desaprobados * 100 / totalalum
promocion= promocionado * 100 / totalalum
chorros= libres * 100 / totalalum

print ("%",round(regulares,2))
print ("%",round(desaproba,2))
print ("%",round(promocion,2))
print ("%",round(chorros,2))
