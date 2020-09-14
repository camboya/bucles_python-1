#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''
    numero_1 =int(input('Ingrese el numero inicial:'))
    numero_2 =int(input('Ingrese el numero final:'))
    numeros_ = [numero_1, numero_2]
    

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
       

    # inicio = ....
    # fin = ....

    # cantidad_numeros ....
    # sumatoria ....

    # bucle.....

    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros

    # Imprimir resultado en pantalla


def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''

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
    


def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''

    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
              # Ya le hemos inicializado en 0

          # Aquí debe contar cuantas notas válidas encontró
       # Aquí debe contar cuantos ausentes hubo

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

    # Imprima en pantalla al cantidad de ausentes

    sumatoria = 0
    cantidad_notas = 0
    cantidad_ausentes = 0



    puntaje = 70
    print('ingrese calificacion 1:')
    calificacion_1 = int(input())
    print("ingrese calificacion 1:",calificacion_1)

    print('ingrese calificacion 2:')
    calificacion_2 = int(input())
    print("ingrese calificacion 2:",calificacion_2)

    print('ingrese calificacion 3:')
    calificacion_3 = int(input())
    print("ingrese calificacion 3:",calificacion_3)

    print('ingrese calificacion 4:')
    calificacion_4 = int(input())
    print("ingrese calificacion 4:",calificacion_4)

    print('ingrese calificacion 5:')
    calificacion_5 = int(input())
    print("ingrese calificacion 5:",calificacion_5)

    if puntaje <= calificacion_1:
     print('A')
    
    if puntaje <= calificacion_2:
     print('B')

    if puntaje >= calificacion_3:
     print('C')

    if puntaje >= calificacion_4:
     print('D')

    if calificacion_5 < puntaje:
     print('F')


    sumatoria = 0
    notastotales_ = [calificacion_1,calificacion_2,calificacion_3,calificacion_4,calificacion_5]

    for elemento in notastotales_:
        sumatoria += elemento    
        print("la suma de las calificaciones desde 0 a sumatoria es:", sumatoria)

 
    sumatoria = calificacion_1 + calificacion_2 + calificacion_3 + calificacion_4 + calificacion_5

    promedio = sumatoria / 5
    print('el promedio  es:', promedio)

    if promedio >=70:
        print('C')
    else:
        print('D')

    

    
   


def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.
    
    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''


    # Colocar el bucle aqui......
    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en   la lista
    temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,14.7, 19.6, 11.2, 18.4]

   

    suma = 0
    i = 0

    temperatura_max = max(temp_dataloger)
    print("temperatura maxima = ", temperatura_max)

    temperatura_min = min(temp_dataloger)
    print('temperatura minima = ', temperatura_min )

    for i in range(0, len(temp_dataloger)):
        temperatura_sumatoria += temp_dataloger[i]   
        print( "sumatoria de temperaturas =", temperatura_sumatoria)


    for elemento in temp_dataloger:
       suma += elemento
       i += 1

    temperatura_promedio = suma / i
    print('la temperatura promedio es', temperatura_promedio)

    print(len(temp_dataloger))


    temperatura_sumatoria = sum(temp_dataloger)
    print("sumatoria de temperaturas = ", temperatura_sumatoria)

    verano = 0
    otoño = 0
    invierno = 0
    primavera = 0
    temperaturaverano_minima = 19
    temperaturaverano_maxima = 28
    temperaturasverano_ = (temperaturaverano_minima, temperaturaverano_maxima)
    
    temperaturaotoño_minima = 11
    temperaturaotoño_maxima = 24
    temperaturasotoño_ = (temperaturaotoño_minima, temperaturaotoño_maxima)

    temperaturainvierno_minima = 8
    temperaturainvierno_maxima = 14
    temperaturasinvierno_ = (temperaturainvierno_minima, temperaturainvierno_maxima)

    temperaturaprimavera_minima = 10
    temperaturaprimavera_maxima = 24
    temperaturasprimavera_ = (temperaturaprimavera_minima, temperaturaprimavera_maxima)

    print('Ingrese temperatura minima de hoy:')
    temperaturaminima_hoy = float(input())
    print('temperatura ingresada:', temperaturaminma_hoy)

    print('Ingrese temperatura maxima de hoy:')
    temperaturamaxima_hoy = float(input())
    print('temperatura ingresada:', temperaturamaxima_hoy)

    if temperaturaminima_hoy <= temperaturasverano_ and temperaturamaxima_hoy <= temperaturasverano_:
       print('la estacion es verano', verano)
    elif temperaturaminima_hoy <= temperaturasotoño_ and temperaturamaxima_hoy <= temperaturasotoño:
       print('la estacion es otoño', otoño)
    if temperaturaminima_hoy <= temperaturasprimavera_ and temperaturamaxima_hoy <= temperaturasprimavera_:
       print('la estacion es primavera', primavera)
    elif temperaturaminima_hoy <= temperaturasinvierno_ and temperaturamaxima_hoy <= temperaturasinvierno_:
        print('la estacion es invierno', invierno)
    


    

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    
    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

  '''



print('Ingrese palabra 1: ')
    palabra_1 = str(input())
    print('palabra ingresada:', palabra_1)

    print('Ingrese palabra 2:')
    palabra_2 = str(input())
    print('palabra ingresada:', palabra_2)

    print('Ingrese palabra 3:')
    palabra_3 = str(input())
    print('palabra ingresada:', palabra_3)

    if palabra_1 > palabra_2  and palabra_3:
        print('{} es mayor que {}'.format(palabra_1, palabra_2, palabra_3))
    else:
        print('{} es mayor que {}'.format(palabra_2, palabra_1, palabra_3))
    
    
    print('palabra 1:', palabra_1)

    palabra_1_len = len(palabra_1)
    print(palabra_1, 'tiene', palabra_1_len, 'caracteres')

    palabras_=[palabra_1,palabra_2,palabra_3]
    palabras_.sort()
    print (palabras_)

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
