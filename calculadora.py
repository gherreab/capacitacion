# Calculadora
import math
import sys
import time
import numpy as np

#Tiempo de espera para simular que esta procesando
espera = time.sleep
 #Variable para pasar el nombre del operador seleccionado
operador = ""

#Funcion de operaciones
def operaciones(a,b,c):
    try:
        if c == 1:        
            resultado = a + b
        elif c == 2:
            resultado = a - b 
        elif c == 3:
            resultado = a * b 
        elif c == 4:
            resultado = a // b 
        elif c == 5:
            resultado = np.sqrt(a) 
        elif c == 6:
            resultado = np.power(a,b)
        elif c == 7:
            resultado = np.sin(a) 
        elif c == 8:
            resultado = np.cos(a) 
        else:
            resultado = np.arctan(a) 
        return resultado
    except Exception:
        print("Error al momento del calulo")
    
#Lista de operadores
operadoresList = ["1 Sumar","2 Restar","3 Multiplicar","4 Dividir","5 Raiz n","6 Exponente n", "7 Seno", "8 Coseno","9 Tangente"]

#Ciclo While
while True:    
    print(" ")
    print("******GERMAN HERRERA BAZAN*****")
    print("******  CALCULADORA  ***** \n")
    #Seleccion de las operaciones permitidas
    print(""">Seleccione una operación a usar:
    """ + operadoresList[0] + """
    """ + operadoresList[1] + """
    """ + operadoresList[2] + """
    """ + operadoresList[3] + """
    """ + operadoresList[4] + """
    """ + operadoresList[5] + """
    """ + operadoresList[6] + """
    """ + operadoresList[7] + """
    """ + operadoresList[8] + """
    10 Apagar/Terminar
    >...""")

    #Entrada de la operacion seleccionada.
    operacionSelec = int(input())

    #Ciclo IF ELSE
    if operacionSelec ==10:
        print("Apagando Calculadora...")
        espera(4)
        quit()
    
    #Operaciones a realizar
    else:
        #Entrada de operaciones de dos numeros o uno
        if operacionSelec == 1 or operacionSelec == 2 or operacionSelec == 3 or operacionSelec == 4 or operacionSelec == 6:
            print("Ingresar el primer numero: ")
            num1 = int(input())
            print("Ingresar el segundo numero: ")
            num2 = int(input())
        else:
            print("Ingresar el numero: ")
            num1 = int(input())
    
        print("El resultado de esta operacion és:")
        #Suma
        if operacionSelec == 1:            
            print(operaciones(num1,num2,1))            
            print("")
            operador = "suma"
        #Resta
        if operacionSelec == 2:
            #result = num1 - num2  
            #print(result)  
            print(operaciones(num1,num2,2))        
            print("")
            operador = "resta"
        #Multiplicar
        if operacionSelec == 3:
            #result = num1 * num2  
            #print(result)          
            print(operaciones(num1,num2,3))
            print("")
            operador = "multiplicacion"
        #Dividir
        if operacionSelec == 4:
            #result = num1 // num2  
            #print(result)           
            print(operaciones(num1,num2,4))
            print("")
            operador = "división"
        #Raiz n
        if operacionSelec == 5:
            #result = np.sqrt(num1)   
            #print(result)                        
            print(operaciones(num1,0,5))
            print("")
            operador = "raiz cuadrada"
        #Exponente n
        if operacionSelec == 6:
            #result = np.power(num1,num2)   
            #print(result) 
            print(operaciones(num1,num2,6))                       
            print("")
            operador = "exponencial"
        #Seno
        if operacionSelec == 7:
            #result = np.sin(num1)   
            #print(result)  
            print(operaciones(num1,0,7))                      
            print("")
            operador = "seno"
        #Coseno
        if operacionSelec == 8:
            #result = np.cos(num1)   
            #print(result)       
            print(operaciones(num1,0,8))                 
            print("")
            operador = "coseno"
        #Tangente
        if operacionSelec == 9:
            #result = np.arctan(num1)   
            #print(result)    
            print(operaciones(num1,0,9))                    
            print("")
            operador = "tangente"

        #Impresión final de la operación
        #print("El resultado de la " + operador + " es: " + str(result))





