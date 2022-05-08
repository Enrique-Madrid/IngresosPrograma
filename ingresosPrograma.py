import os
from datetime import datetime
from tkinter import E
import pymysql

global gastos
gastos = 0
global ingresos
ingresos = 0
cerrarPrograma = 0

tiempo = [datetime.today().strftime('%y'), datetime.today().strftime('%m'), datetime.today().strftime('%d')]



class BaseDeDatos:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='', db='ingresosprograma')
        self.cursor = self.connection.cursor()
        print ("Conección establecida exitosamente!")

    def seleccionarUsuario(self, id):
        sql = 'SELECT datos_id, ingresos, datos_descripcion, datos_fecha FROM datos_ingresos WHERE datos_id = {}'.format(id)
        
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            print("Id: ", user[0])
            print("Ingresos: ", user[1])
            print("Descripción: ", user[2])
            print("Fecha: ", user[3])
            print("_________________ \n")

        except Exception as e:
            raise

    def seleccionarTodos(self, id):
        sql = 'SELECT datos_id, ingresos, datos_descripcion, datos_fecha FROM datos_ingresos'
        
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
            
            for user in user:
                print("Id: ", user[0])
                print("Ingresos: ", user[1])
                print("Descripción: ", user[2])
                print("Fecha: ", user[3])
                print("_________________ \n")

        except Exception as e:
            raise

    def actualizarUsuarioIngresos(self, id, ingresos, descripcion):
        sql = "UPDATE datos_ingresos SET ingresos='{}', datos_descripcion='{}' WHERE datos_id = {}".format(ingresos, descripcion, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

while cerrarPrograma == 0:
    print ("Elije una de las siguientes opciones")
    print ("1. Gastos")
    print ("2. Ingresos")
    print ("3. Checar saldo actual")
    print ("4. Analizar futuras proyecciónes")
    opcion_1 = int(input("Ingresa un número del 1 al 4: "))
    if opcion_1 == 1:
        cant = int(input("Ingrese cuantos datos va a ingresar: "))
        for cant in range(0, cant): 
            os.system ("cls")
            nombre = input("Ingrese el nombre del producto/servicio: ")
            valor = int(input("Ingrese el gastos del producto/servicio en lps: "))
            print("El " , nombre ," fué comprado a un valor de " , valor , " lps, el día", tiempo[2])
            gastos = gastos + valor

    elif opcion_1 == 2:
        cant = int(input("Ingrese cuantos datos va a ingresar: "))
        for cant in range(0, cant):  
            os.system ("cls")
            nombre = input("Ingrese el nombre del producto/servicio: ")
            valor = int(input("Ingrese la cantidad de ingresos en lps: "))
            print("El " , nombre ," dió un total de ingresos de " , valor , " lps, el día", tiempo[2])
            ingresos = ingresos + valor        

    elif opcion_1 == 3:
        os.system ("cls")
        total = ingresos - gastos 
        print ("El saldo actual es: " , total , " lps")
        basededatos = BaseDeDatos()
        basededatos.seleccionarTodos(1)
        basededatos.actualizarUsuarioIngresos(2, '1000', 'prueba 1')
        basededatos.seleccionarTodos(2)


    elif opcion_1 == 4:
        print ("Proyecciones")
    
    elif opcion_1:
        print ("No elijiste una opción correcta")
    
    cerrarPrograma = int(input("Apreta 0 para repetir: "))
    os.system ("cls")



