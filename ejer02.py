'''Implemente un programa para convertir un número decimal a hexadecimal
ejm. el número 8642 en forma hexadecimal es: 21C2
'''
def DecimalAHexadecimal(): 
    numero = int(input("Introduce un numero en base 10 => ")) # Pedimos numero en base 10 
    hexadecimal = "" # En esta variable almacenaremos el valor hexadecimal que representa base 16
    while numero != 0:  # comparamos el valaor decimal sea diferente a 0
        # Cambiamos los digitos por los hexadecimales
        renombrado = Cambiar(numero % 16)
        
        hexadecimal = str(renombrado) + hexadecimal # Llenamos la variable "hexadecimal" con los nuevos valores 
        numero = int(numero / 16)   #queda alamcenado el valor dividido entre 16
    print("Resultado: " + hexadecimal) # Mostramos el resultado
#ceamos otra funcion para que nos ayude a traducir los digitos a hexadecimales
def Cambiar(digitos): 
    numero =     [10 , 11 , 12 , 13 , 14 , 15,16,17] #numeros en base 10
    hexadecimal = ["A", "B", "C", "D", "E", "F","G","H"]  #caambiamos de notacion solamente een hexagecimal
    for i in range(9):  # recorremos hasta 9 ya que en numero le dimos 9 numeros y cambiando notacion
        if digitos == numero[i - 1]:  #comparamos si el numero es ihgual a su iteracion anterior 
            digitos = hexadecimal[i - 1]  # si fuera el caso lo almacenamos dentro de ella 
    return digitos                  # deevolvemos el vlor almacenado

DecimalAHexadecimal()    #imprimimos la conversion de base 10 a base 16

