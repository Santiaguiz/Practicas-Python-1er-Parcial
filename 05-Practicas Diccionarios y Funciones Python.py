import os  # Importa el módulo os para limpiar la consola

# Practica 31: Diccionarios en Python
print(input("------Presione Enter Para Iniciar------"))  # Solicita al usuario que presione Enter para comenzar
print("Practica 31")
print("Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio con presentación en un print(). El resultado será esto en la consola:")

# Diccionario de teclados
teclado1 = {
    'Categoría': 'Teclados',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
}

teclado2 = {
    'Categoría': 'Teclados',
    'Modelo': 'Corsair K55 RGB',
    'Precio': '59,99'
}

# Imprime el modelo y el precio del teclado2
print('El modelo', teclado2['Modelo'], 'cuesta', teclado2['Precio'], '$.')

print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola

# Practica 32: Como usar Diccionarios en Bucle For
print("\nPractica 32")
print("Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola: ")

# Re-define el diccionario teclado1
teclado1 = {
    'Categoría': 'Teclados',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
}

# Itera sobre las claves del diccionario y las imprime con su valor
for x in teclado1:
    print(x, '=', teclado1[x] + '.')  # Imprime cada clave y su valor

print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola

# Practica 33: Metodos con Diccionarios
print("\nPractica 33")
print("Elimina el diccionario teclado1 entero. De teclado2 elimina las claves 'Categoría' y 'Precio'. Muestra la última clave ('Modelo') que queda en la consola. ")

# Re-define los diccionarios
teclado1 = {
    'Categoría': 'Teclados',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
}

teclado2 = {
    'Categoría': 'Teclados',
    'Modelo': 'Corsair K55 RGB',
    'Precio': '59,99'
}

# Elimina el diccionario teclado1
del teclado1
# Elimina las claves 'Categoría' y 'Precio' del diccionario teclado2
del teclado2['Categoría']
del teclado2['Precio']
# Imprime el modelo que queda en teclado2
print(teclado2['Modelo'])

print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola

# Practica 34: Crear y Llamar Funciones en Python
print("\nPractica 34")
print("Crea una función que realice una suma. Para ello, tendrás que añadir dos argumentos (numero1 y numero2).")

# Define la función de suma
def suma(numero1, numero2):
    print(numero1 + numero2)  # Imprime la suma de los dos números

# Llama a la función con diferentes argumentos
suma(10, 20)
suma(20, 30)
suma(50000, 7000)

print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola

# Practica 35: Argumentos Arbitrarios -args
print("\nPractica 35")
print("¿Cuántos argumentos se utilizan en cada una de estas llamadas?")

# Define una función que acepta un número arbitrario de argumentos
def colores(*args):
    pass  # No realiza ninguna acción

# Llama a la función con diferentes números de argumentos
colores('rojo', 'azul', 'verde', 'amarillo')  # 4 argumentos
colores('lila', 'negro', 'rojo')  # 3 argumentos
colores('rosa')  # 1 argumento
colores('marrón', 'naranja')  # 2 argumentos

print("La respuesta son 4 argumentos línea 4, 3 argumentos línea 5, 1 argumento línea 6, 2 argumentos línea 7")

print("\nCompleta el siguiente fragmento de código: ")
# Define la función colores que imprime el color favorito
def colores(*args):
    print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('rojo', 'azul')  # Llama a la función con dos argumentos
colores()  # Llama a la función sin argumentos

# Crea una función que suma cinco números utilizando *args
def suma(*args):
    resultado = args[0] + args[1] + args[2] + args[3] + args[4]  # Suma los cinco primeros argumentos
    print('El resultado de sumar estos cinco números es:', resultado)

suma(5, 7, 45, 8657, 3, 4)  # Llama a la función con seis argumentos

print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola
