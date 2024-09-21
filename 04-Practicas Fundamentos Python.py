import os

# Practica 19: Crear y Manejar Tuplas
print(input("------Presione Enter Para Iniciar------"))
print("\nPractica 19")
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
numeros = (10, 1, 5, 11)
# Muestra información sobre las operaciones a realizar
print("Usando las Tuplas así como con las 2 listas se deben de realizar 2 diferentes acciones")
# Accede al color en la posición 1 (índice 1) de la tupla 'colores'
print("Primero acceder al color en la posición 1 el cual es: ", colores[1])
# Realiza una operación matemática usando elementos de la tupla 'numeros'
operacion = numeros[0] + numeros[2] + numeros[3] - numeros[1]
# Muestra el resultado de la operación
print("Segundo, se debe realizar una operación con la lista de números dando como resultado el 25: ", operacion)
print(input("------Presione Enter Para Pasar A La Siguiente Practica"))
os.system("cls")  # Limpia la consola

# Practica 20: Como Convertir Tuplas a Listas y Viceversa
print("\nPractica 20")
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
# Muestra la lista de colores actual
print("Usando la siguiente lista debo de convertirla a tupla usando el comando 'tuple':\n", colores)
# Convierte la lista 'colores' en una tupla
tupla = tuple(colores)
# Muestra la tupla creada a partir de la lista
print("Ahora se mostrara como una tupla: ", tupla)
# Explica cómo convertir una tupla de vuelta a lista usando el comando 'list'
print("Así mismo si quiero regresar una tupla a una lista usaría el comando 'list(x)'")
print(input("------Presione Enter Para Pasar A La Siguiente Practica"))
os.system("cls")  # Limpia la consola

# Practica 21: El Condicional IF y Operadores de Comparación
print("\nPractica 21")
print("Se deben de cambiar los operadores para que se conviertan tanto en true como false")
num1 = 15
num2 = 20

# Comparación usando el operador '!=' (diferente)
if num1 != num2:
    print('Se ejecuta el if.', "Se ejecutó porque 15 es diferente de 20")

num3 = 1450
num4 = 60

# Comparación usando el operador '>' (mayor que)
if num3 > num4:
    print('Se ejecuta el if.', "Se ejecutó porque 1450 es mayor que 60")

num5 = 1450
num6 = 60

# Comparación usando el operador '!=' (diferente)
if num5 != num6:
    print('Se ejecuta el if.')

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))
os.system("cls")  # Limpia la consola

# Practica 22: El Condicional IF Else
print("\nPractica 22")
print("Para esta práctica se me da un condicional IF Else que se debe corregir, este termina quedando de la siguiente forma: ")

color = 'rojo'
# Condicional if-else que verifica si el color es 'rojo'
if color == 'rojo':
    print("El color es rojo.")
else:
    print("El color no es rojo.")

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))
os.system("cls")  # Limpia la consola

# Practica 23: El condicional if elif else y entrada de datos
print("\nPractica 23")
print("Al siguiente código añadele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120")

# Solicita la edad del usuario
edad = int(input('¿Cuál es tu edad?\n'))
# Verifica si la edad es menor o igual a 0
if edad <= 0:
    print('Nadie puede tener esa edad.')
# Verifica si la edad está entre 1 y 18 años
elif edad >= 1 and edad <= 18:
    print('Eres menor de edad.')
# Verifica si la edad está entre 18 y 45 años
elif edad >= 18 and edad <= 45:
    print('Eres de joven aun. Sigue así.')
# Verifica si la edad está entre 45 y 100 años
elif edad >= 45 and edad <= 100:
    print('Eres Entre Adulto o Mayor de edad.')
# Verifica si la edad está entre 100 y 120 años
elif edad >= 100 and edad <= 120:
    print('Felicidades eres de los seres más viejos del planeta. ¿Cómo fue conocer a Moisés?')
else:
    print('Edad no válida.')

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))
os.system("cls")  # Limpia la consola

# Practica 24: Comprobar Datos en Listas y Tuplas
print("\nPractica 24")
# Solicita al usuario introducir un color y lo convierte a minúsculas
colores = input('Introduce un color:\n').lower()
lista_colores = ['rojo', 'azul', 'verde', 'amarillo']

# Verifica si el color introducido está en la lista
if colores in lista_colores:
    print(f'El color {colores} sí forma parte de la lista.')
else:
    print("El color introducido no forma parte de la lista")
    # Pregunta si desea agregar el color a la lista
    agregar = input("\n¿Gustas agregar este color o algún otro color? (s/n)").lower()
    # Si el usuario desea agregarlo, se añade el color a la lista
    if agregar == 's':
        lista_colores.append(colores)
        print(f'\nEl color {colores} ha sido añadido a la nueva lista de colores')
    else:
        print("Ah, bueno entonces no quieres ningún color nuevo.")

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))
os.system("cls")  # Limpia la consola

# Practica 27: El Bucle While
print("\nPractica 27")
# Descripción de las tareas a realizar
print("Aquí se harán 3 cosas\n1.- Se creará un bucle while hasta que llegue al 15 con incrementos de 5\n ")
x = 0

# Bucle while que incrementa x de 5 en 5 hasta llegar a 15
while x <= 15:
    print(x)
    x += 5

print("2.- Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.\n ")
x = 0

# Bucle while que decrementa x de 20 en 20 hasta llegar a -100
while x >= -100:
    print(x)
    x -= 20

print("3.- Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'")
x = 10

# Bucle while que decrementa x de 1 en 1 hasta llegar a 0
while x >= 0:
    print('El valor de x es: ', x)
    x -= 1

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))
os.system("cls")  # Limpia la consola

# Practica 28: El Bucle While con Condicional IF
print("\nPractica 28")
x = 0  # Valor inicial de x
# Bucle while que se ejecuta mientras x sea menor o igual a 30
while x <= 30:
    x += 1  # Incrementa x en 1 en cada iteración
    # Salta las ejecuciones cuando x es 4, 6 o 10
    if x == 4 or x == 6 or x == 10:
        print('Se saltó el valor ', x, ' de x')
        continue
    # Rompe el bucle cuando x es igual a 15
    if x == 15:
        print('Se rompió la ejecución del bucle cuando x valía: ', x)
        break
    # Imprime el valor de x en cada iteración que no se cumple con los if anteriores
    print(x)

# Practica 29: El Bucle For
print("\nPractica 29")
print("Se crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración: 'El color es: ' + color + '.'")
colores = ('rojo', 'azul', 'verde', 'amarillo')

# Bucle for que recorre la tupla 'colores'
for x in colores:
    print('El color es: ' + x + '.')
print(input("------Presione Enter Para Pasar A La Siguiente Practica"))
os.system("cls")  # Limpia la consola

# Practica 30: El Bucle For con range()
print("\nPractica 30")
print("Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. Basta con que imprimas el valor de cada iteración.")
# Bucle for que recorre valores desde 7 hasta 700 en incrementos de 100
for x in range(7, 700, 100):
    print(x)

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))
os.system("cls")  # Limpia la consola
