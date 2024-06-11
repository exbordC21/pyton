from LISTA import by_name

super_heroes = [
    {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
    },
    {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
    },
    {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
    },
    {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
    },
    {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
    },
    {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
    },
    {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
    },
    {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
    },
    {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
    },
    {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
    },
    {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
    },
    {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, es un joven héroe con un traje y habilidades arácnidas tras ser picado por una araña radiactiva."
    },
    {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
    },
    {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
    },
    {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
    },
    {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
    },
    {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
    },
    {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
    },
    {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
    },
    {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
    },
    {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
    },
    {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
    },
    {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hank Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos."
    }
]


for index,element in enumerate(super_heroes):
    if super_heroes[index]['nombre']=='Linterna Verde':
        print("se elimino correctamente el nodo ",super_heroes.pop(index))
    else:
        None

print()

for index,element in enumerate(super_heroes):
    if (super_heroes[index]['nombre']=='Wolverine') and (super_heroes[index]['año_aparicion']==1974) :
        print("el año de aparicion de",super_heroes[index]['nombre'],"es",super_heroes[index]['año_aparicion'])
    else:
        None

print()

for index,element in enumerate(super_heroes):
    if (super_heroes[index]['nombre']=='Doctor Strange') :
        super_heroes[index]['casa_comic']="Marvel"
        print("se a cambiado la casa del super heroe",super_heroes[index]['nombre'],"su casa ahora es:",super_heroes[index]['casa_comic'])
    else:
        None

print()

mencion=[]
for index,element in enumerate(super_heroes):
    if ('traje' in super_heroes[index]['biografia'] or 'armadura' in super_heroes[index]['biografia'] ) :
        mencion.append(super_heroes[index]['nombre'])
    else:
        None
print("los super heroes que mencionar el traje o la armadura son:",mencion[-1],",",mencion[-2])

print()

print("los super heroes que aparecieron antes de 1963 son")
for index,element in enumerate(super_heroes):
    if (super_heroes[index]['año_aparicion']<1963) :
        print(super_heroes[index]['nombre'],"su casa es:",super_heroes[index]['casa_comic'])
    else:
        None

print()

for index,element in enumerate(super_heroes):
    if (super_heroes[index]['nombre']=='Mujer Maravilla') or (super_heroes[index]['nombre']=='Capitana Marvel') :
        print("la casa de",super_heroes[index]['nombre'],"es",super_heroes[index]['casa_comic'])
    else:
        None

print()

for index,element in enumerate(super_heroes):
    if (super_heroes[index]['nombre']=='Flash') or (super_heroes[index]['nombre']=='Star-Lord') :
        print("informacion de :",super_heroes[index]['nombre'], super_heroes[index])
        print()
    else:
        None

print()

nom=[]
super_heroes.sort(key=by_name)
for index,element in enumerate(super_heroes):
    if (super_heroes[index]['nombre'].startswith(('B','M','S'))):
        nom.append(super_heroes[index]['nombre'])
    else:
        None
print(nom)

print()

acm1=0
acm2=0
for index,element in enumerate(super_heroes):
    if (super_heroes[index]['casa_comic']=='DC Comics'):
        acm1+=1
    elif (super_heroes[index]['casa_comic']=='Marvel Comics'):
        acm2+=1
    else:
        None
print("la cantidad de super heores de DC comics es de :",acm1)
print("la cantidad de super heores de Marverl Comics es de :",acm2)
