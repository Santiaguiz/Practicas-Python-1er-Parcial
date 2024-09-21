import os

# Practica 10: Cómo Crear Listas y Utilizarlas en Python
print(input("------ Presione Enter Para Iniciar ------"))
print("\nPractica 10")
# Definimos una lista de colores
colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]
print("De esta lista: ", colores, "\nEl que esta en la posicion numero 3 es: ")
# Imprimimos el color en la posición 3 (amarillo)
print(colores[3])
# Informamos las posiciones de rojo y rosa
print("Asi mismo los colores rojo y rosa se encuentran en la posicion 0 y 7 respectivamente")
print(input("------ Presione Enter Para Continuar ------"))
os.system("cls")

# Practica 11: Posiciones Negativas en Listas Python
print("\nPractica 11")
# Otra lista de colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("Mediante las listas negativas, imprimire 5 de los siguientes colores: ", colores)
# Imprimimos colores usando posiciones negativas
print(colores[-1])   # naranja
print(colores[-7])   # lila
print(colores[-5])   # marrón
print(colores[-2])   # blanco
print(colores[-10])  # rojo
print("Se imprimio cada color dependiendo de su posicion negativa, como ejemplo se ve asi 'print(colores[-1])'")
print(input("------ Presione Enter Para Continuar ------"))
os.system("cls")

# Practica 12: Eliminar Elementos con del()
print("\nPractica 12")
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("De la siguiente lista, usando el comando 'del' debo de elimiar elementos: ", colores)
# Eliminamos elementos usando sus posiciones
del colores[-9]  # rojo
del colores[4]   # marrón
del colores[-4]  # negro
del colores[-3]  # rosa
print("Ahora se impimira la lista sin los elementos que se debian de eliminar", colores)
print(input("------ Presione Enter Para Continuar ------"))
os.system("cls")

# Practica 13: Eliminar Elementos con remove()
print("\nPractica 13")
print("De la siguiente lista de colores se debe de eliminar elementos usando unicamente 'remove': ", colores)
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
# Usamos 'remove' para eliminar elementos por su valor
colores.remove('amarillo')
colores.remove('rojo')
print("Ahora se imprimira la lista sin los colores que se eliminaron usando el 'remove': ", colores)
print(input("------ Presione Enter Para Continuar ------"))
os.system("cls")

# Practica 14: Eliminar Elementos con pop()
print("\nPractica 14")
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("Usando el metodo 'pop', debo de eliminar 2 elementos asi mismo se deben de almacenar")
# Eliminamos y almacenamos colores usando 'pop'
color1 = colores.pop(1)  # azul
color2 = colores.pop(7)  # rosa
print("Ahora se imprimiran los valores eliminados y guardados: ", color1, color2)
print(input("------ Presione Enter Para Continuar ------"))
os.system("cls")

# Practica 15: Insertar Elementos con append()
print("\nPractica 15")
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("De la siguiente lista, debere añadir 2 colores los cuales son 'fuxia' y 'celeste': ", colores)
# Añadimos nuevos colores al final de la lista
colores.append('fuxia')
colores.append('celeste')
print("Ahora aparecera la lista de los colores con los 2 que se agregaron: ", colores)
print(input("------ Presione Enter Para Continuar ------"))
os.system("cls")

# Practica 16: Insertar Elementos con insert()
print("\nPractica 16")
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("De la siguiente lista, debere añadir 2 colores usando el metodo 'insert' en dos posiciones diferentes: ", colores)
# Insertamos colores en posiciones específicas
colores.insert(6, 'magenta')  # posición 6
colores.insert(-1, 'turquesa')  # antes de 'naranja'
print("Ahora la lista se vera modificada con los 2 nuevos colores que se agregaron en 2 posiciones especifias: ", colores)
print(input("------ Presione Enter Para Continuar ------"))
os.system("cls")

# Practica 17: Ordenar Elementos con sort() y sorted()
print("\nPractica 17")
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("De la siguiente lista se deben de acomodar los nombres den orden alfabetico de forma descendente: ", colores)
# Ordenamos la lista en orden descendente
colores.sort(reverse=True)
# Obtenemos la cantidad de colores
cantidad_colores = len(colores)
print("Ahora se impiran en orden alfabetico de la z - a: ", colores)
print("Adicionalmente mencionare la cantidad de colores que hay en la lista: ", cantidad_colores)
print(input("------ Presione Enter Para Terminar ------"))
os.system("cls")
