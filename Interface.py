import Sensores as s
import Registros_MongoDB
import sys 
import time

def read():
    x = input()
    if x == "a" or x == "A": 
        values()
        menu()
    if x == "b" or x == "B": 
        values()
        opciones()
    if x == "c" or x == "C": 
       print("Adios")
       sys.exit()

def readd():
    x = input()
    if x == "a" or x == "A": 
        r = Registros_MongoDB
        r.addRegistro()
    if x == "b" or x == "B": 
        print("No")
    if x == "c" or x == "C": 
       print("No")
    if x == "d" or x == "B": 
        menu()

def menu():
    print("----------------Menú-----------------")
    print(".....................................")
    print("a) Ver sensores......................")
    print("b) Guardar valores...................")
    print("c) Salir.............................")
    print(".....................................")
    print(".....................................")
    read()

def values():
    print("----------------Sensores-------------")
    print(".....................................")
    sensores = Registros_MongoDB
    data = sensores.getValores()
    for x in data:
        print("............Valores.............")
        print("Ultrasonico:" + x[3])
        print("PRI:" + x[2])
        print("Temperatura:" + x[1])
        print("Humedad:" + x[0])
    print(".....................................")
    print(".....................................")
    time.sleep(5)

def opciones():
    print("----------------Menú-----------------")
    print(".....................................")
    print("a) Guardar en mongoDB................")
    print("b) Guardar en Mysql..................")
    print("c) Guardar de manera local...........")
    print("d) Atras.............................")
    print(".....................................")
    print(".....................................")
    readd()

menu()