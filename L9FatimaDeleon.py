print ("Ejercicio 1: operaciones aritméticas")

#Entradas
numero1 = int(input("Ingrese un número entero"))
numero2 = int(input("Ingrese otro número entero"))

#Operaciones
suma = numero1 + numero2 
resta = numero1 - numero2 
divisionEntera = numero1 // numero2 
divisionModular = numero1 % numero2

#Salidas
print (numero1, "+", numero2, "=", suma)
print (numero1, "-", numero2, "=", resta)
print (numero1, "//", numero2, "=", divisionEntera)
print (numero1, "%", numero2, "=",divisionModular)

print ("Ejercicio 2: operaciones booleanas")
diferencia = numero1 != numero2
print(numero1, "!=", numero2, "=", diferencia)

