from clasificacion import clasificar_en_categ

"""Este módulo contiene una lista de nombres.
    Entre las personas que contiene la lista podemos encontrar magos, cientificos u otros.
    Se clasificará y se imprimirá cada categoria según corresponda.
"""


lista_nombres = [
    "Harry Houdini", "Newton", "David Blaine", "Hawking", 
    "Messi", "Teller", "Einstein", "Pele", "Juanes" 
]


#La función importada categoriza en un diccionario cada grupo de la lista de nombres asignada.
dicc_categorias= clasificar_en_categ(lista_nombres)



#Creación de función que agregue el "El gran mago" a cada mago de las lista de magos dentro del diccionario.
def hacer_grandioso (dicc_categorias):
    for indice in range(len(dicc_categorias["magos"])):
        dicc_categorias["magos"][indice] = "El gran mago " + dicc_categorias["magos"][indice]
    return dicc_categorias["magos"]



#Creación de función para imprimir cada nombre de la lista
def imprimir_nombres (lista_nombres):
    for nombre in lista_nombres:
        print(nombre)
        

#Creación de funcion para imprimir cada valor de cada categoria con un titulo correspondiente
def imprimir_categorias (dicc_categorias):
    for categoria, personas in dicc_categorias.items():
        print(f"\nLos {categoria} son:")
        for nombre in personas:
            print(nombre)


#Impresión de todas las categorias a traves de print y funciones    

print("Las celebridades incluidas en la lista principal son:")
imprimir_nombres(lista_nombres)
hacer_grandioso (dicc_categorias) #Ejecucion del codigo que modifica los nombres dentro de "magos" en el diccionario
imprimir_categorias(dicc_categorias)





