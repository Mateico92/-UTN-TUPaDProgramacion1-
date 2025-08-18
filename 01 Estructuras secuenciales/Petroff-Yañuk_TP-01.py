#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
# Saludo = "Hola Mundo!"
# print(f"{Saludo}")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

# nombre = input("Por favor ingrese su nombre: ")
# print(f"Hola {nombre} es un gusto saludarte")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# residencia = input("Ingrese su lugar de residencia: ")

# print(f"Soy {nombre} {apellido} tengo {edad} años vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.                                                                                                                                                                                                                  

# radio = input("Ingrese el radio de un círculo: ")
# radio = float(radio)
# pi = 3.1416

# perimetro = 2 * pi * radio

# # perimetro = int(perimetro)
# area = pi * (radio * radio)

# print(f"El perimetro es: {perimetro} ")
# print(f"El área de un círculo es: {area}")


# radio = input("Ingrese el radio de un círculo: ") 
# radio = int(radio) 
# diametro = (2 * radio) 
# diametro = int(diametro) 
# perimetro = (diametro * 3.1416) 
# perimetro = int(perimetro) 
# area = (3.1416 * (radio * radio)) 
# print(f"El diametro es: {diametro}") 
# print(f"El perimetro es: {perimetro} ") 
# print(f"El área de un círculo es: {area}")


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

# segundos = input("Ingresa un número: ")
# segundos = float(segundos)
# hora = segundos / 3600

# print(hora)

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

# num = input("Ingresá un número del 0 al 9")

# num = int(num)





# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

# num1 = float(input("Ingresa un número: "))
# num2 = float(input("Ingresa otro número: "))
# suma = num1 + num2
# resta = num1 - num2
# multiplicacion = num1 * num2
# division = num1 / num2
# print(f"La suma de {num1} y {num2} es: {suma}")
# print(f"La resta de {num1} y {num2} es: {resta}")
# print(f"La multiplicacion de {num1} y {num2} es: {multiplicacion}")
# print(f"La division de {num1} y {num2} es: {division}")


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

# altura = float(input("Ingresa tu altura: "))
# peso = float(input("Ingresa tu peso: "))

# IMC = peso / altura

# print(f"Tu índice de masa corporal es: {IMC} ")



# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =9/5.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

# temC = float(input("Ingresa la temperatura en Celcius: "))

# temF = 9/5 * temC + 32

# print(f"La temperatura en Farenheit es:  {temF}"  )

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingresá otro número: "))
num3 = float(input("Ingresá otro número: "))

suma = num1 + num2 + num3
promedio = suma / 3
print(f"El promedio de {num1}, {num2}, {num3} es: {promedio}")
