import os  # Importa el módulo 'os' que permite interactuar con el sistema operativo, por ejemplo, para limpiar la consola.

# Practica 2: Variables
print(input("------Presiona Enter Para Continuar-----"))  # Espera a que el usuario presione Enter antes de continuar.
print("Practica 2")  # Imprime el título de la práctica.
msj = "Que onda raza"  # Asigna una cadena de texto a la variable 'msj'.
num1 = 15  # Asigna el número 15 a la variable 'num1'.
num2 = 10  # Asigna el número 10 a la variable 'num2'.
sum = num1 + num2  # Suma los valores de 'num1' y 'num2' y los asigna a la variable 'sum'.
print("Este es mi mensaje pa el que cheque el codigo:", msj)  # Imprime el mensaje almacenado en 'msj'.
print("Numero 1:", num1)  # Imprime el valor de 'num1'.
print("Numero 2:", num2)  # Imprime el valor de 'num2'.
print("La suma:", sum)  # Imprime el resultado de la suma de 'num1' y 'num2'.
print(input("------Presione enter para pasar a la siguiente practica-----"))  # Espera a que el usuario presione Enter antes de continuar.
os.system("cls")  # Limpia la consola.

# Practica 3: Strings
print("\nPractica 3")  # Imprime el título de la práctica con un salto de línea.
msj2 = 'Esto fue impreso con comillas simples, osea estas:'  # Asigna un mensaje con comillas simples a 'msj2'.
msj3 = "Y este com comillas dobles, osea estas:"  # Asigna un mensaje con comillas dobles a 'msj3'.
xd = 'Para imprimir en la consola se usa el comando "print()"'  # Almacena un mensaje que describe el uso de 'print()'.
print(msj2, "''")  # Imprime 'msj2' y muestra un par de comillas simples.
print(msj3, '""')  # Imprime 'msj3' y muestra un par de comillas dobles.
print(xd)  # Imprime el mensaje de la variable 'xd'.
print(input("------Presione enter para pasar a la siguiente practica-----"))  # Espera a que el usuario presione Enter antes de continuar.
os.system("cls")  # Limpia la consola.

# Practica 4: Como concatenar
print("\nPractica 4")  # Imprime el título de la práctica con un salto de línea.
p1 = "Izi"  # Asigna el valor "Izi" a la variable 'p1'.
p2 = "pici"  # Asigna el valor "pici" a la variable 'p2'.
com = p1 + " " + p2 + " "  # Concatena 'p1' y 'p2' con un espacio entre ellos y lo asigna a 'com'.
n = "Santiago"  # Asigna el nombre "Santiago" a la variable 'n'.
ap = "Ruiz"  # Asigna el apellido paterno "Ruiz" a la variable 'ap'.
am = "Flores"  # Asigna el apellido materno "Flores" a la variable 'am'.
print(p1 + p2)  # Concatena e imprime 'p1' y 'p2' sin espacios.
print(com)  # Imprime la concatenación de 'p1' y 'p2' con espacios.
print(p1 + "pici")  # Concatena 'p1' con la cadena "pici" e imprime el resultado.
print(n + " " + ap + " " + am + " ")  # Concatena el nombre completo y lo imprime.
print("Dos numeros concatenados:\n""10" + "12")  # Concatena las cadenas "10" y "12" y las imprime.
print(input("------Presione enter para pasar a la siguiente practica-----"))  # Espera a que el usuario presione Enter antes de continuar.
os.system("cls")  # Limpia la consola.

# Practica 5: Los métodos upper(), lower() y title en Python
print("\nPractica 5")  # Imprime el título de la práctica con un salto de línea.
fra1 = "enrique barros fernandez".title()  # Capitaliza la primera letra de cada palabra en la cadena y lo asigna a 'fra1'.
fra2 = "Esta Es Una Frase Para Ser Formateada".lower()  # Convierte toda la cadena a minúsculas y lo asigna a 'fra2'.
fra3 = "Esta Es Una Frase Para Ser Formateada".upper()  # Convierte toda la cadena a mayúsculas y lo asigna a 'fra3'.
print(fra1)  # Imprime 'fra1' con la primera letra de cada palabra en mayúsculas.
print(fra2)  # Imprime 'fra2' completamente en minúsculas.
print(fra3)  # Imprime 'fra3' completamente en mayúsculas.
print(input("------Presione enter para terminar-----"))  # Espera a que el usuario presione Enter antes de continuar.
os.system("cls")  # Limpia la consola.

# Practica 6: Saltos de Línea y Tabulaciones
print("\nPractica 6")  # Imprime el título de la práctica con un salto de línea.
print("-Python.\n-JavaScript.\n-Java.\n-PHP.\n-TypeScript.\n-SQL.\n-COBOL.")  # Imprime una lista de lenguajes de programación, cada uno en una nueva línea.
print(input("------Presione enter para terminar-----"))  # Espera a que el usuario presione Enter antes de terminar.
os.system("cls")  # Limpia la consola.
