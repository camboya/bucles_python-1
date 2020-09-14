numero_1 =int(input('Ingrese el numero 1:'))
numero_2 =int(input('Ingrese el numero 2:'))
numeros_=[numero_1, numero_2]

for numeros_ in range(1,6):
    print(numeros_)

sumatoria = 0
numero = [1,2,3,4,5]
for i in range (0, len (numero)):
    sumatoria += numero [i]    
    print("la suma de los numeros desde 0 a sumatoria es:", sumatoria)
i = 0
for i in numero:
    sumatoria += i
    i += 1

promedio = sumatoria / i
print('el promedio  es:', promedio)

print("Ingrese numero 4:")
numero_4 = int(input())
print("ingrese numero 4:",numero_4)

print("Ingrese numero 5:")
numero_5 = int(input())
print("ingrese numero 5:",numero_5)


if (numero_4 >= 0) or (numero_5 >= 0):
    suma = numero_4 + numero_5
    print('La suma entre {} y {} es {}'.format(numero_4, numero_5, suma))

if (numero_4 >= 0) or (numero_5>= 0):
    resta = numero_4 - numero_5
    print('La resta entre {} y {} es {}'.format(numero_4, numero_5, resta))

if (numero_4 >= 0) or (numero_5>= 0):
    multiplicacion = numero_4 * numero_5
    print('La multiplicacion entre {} y {} es {}'.format(numero_4, numero_5, multiplicacion))

if (numero_4 >= 0) or (numero_5>= 0):
    division = numero_4 / numero_5
    print('La division entre {} y {} es {}'.format(numero_4, numero_5, division))

if (numero_4 >= 0) or (numero_5>= 0):
    exponente = numero_4 ** numero_5
    print('El exponente entre {} y {} es {}'.format(numero_4, numero_5, exponente))

while True:   
    if (numero_4 >= 7) or (numero_5 >= 8):
      break   # Salgo del bucle!
    print('Este es el final')

    
   