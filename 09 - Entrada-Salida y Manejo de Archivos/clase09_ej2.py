#2) Crear un script con el nombre "clase09_ej2.py2" 
#que reciba como un valor de temperatura en grados centígrados, 
#un valor de humedad y por último si llovio (Con True o False). 
#Y que cada vez que sea invocado, cargue en el archivo provisto "clase09_ej2.csv" 
#una marca de tiempo y esa información.

#Para trabajar con tipos de datos relacionados con la medición del tiempo, 
#como ser fechas, horarios o marcas de tiempo se puede utilizar la clase *datetime*


import sys
# Comprobación de seguridad, ejecutar sólo si se recibe 3 argumentos
if (len(sys.argv) == 4):
    import datetime
    import os

    marca_de_tiempo = datetime.datetime.now()
    marca_de_tiempo = int(datetime.datetime.timestamp(marca_de_tiempo))

    temperatura = sys.argv[1]
    humedad = sys.argv[2]
    lluvia = sys.argv[3]
    
    #temperatura = input('Ingrese la temperatura en grados centígrados')
    #humedad = input('Ingrese el porcentaje de humedad')
    linea = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia

    #lo abro y puedo agregar info sin borrar lo que ya esta
    logs_lluvia = open('clase09_ej2.csv', 'a') 
    logs_lluvia.write(linea+'\n')
    logs_lluvia.close() #siempre cierro

else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py <temperatura> <humedad> <True o False>')