'''Convertir un Número Entero a Cualquier Base Numérica,
El programa debe pedir al usuario que ingrese un número n, y un número p,'''
#pedir el numero n y p respectivamente
n = int(input("Introduce un numero entero => "))
p = int(input("Introduce la basee a la qque sera convertido el primer numero=> "))

#creamos una funcion
def conversor(n,p):
    cadenas= '012345678ABCDEF' #creamos asi para devolver los valores en cadena de caracteres
    if n < p:   #comapramos que el entero sea menor  a la base introducida
        return cadenas[n]   #ese valor n lo almacenamos en cadenas iteradamente
    else:
        return conversor(n//p, p)+cadenas[n % p]  #usamos unaa funcion recursiva y lo pasamos el operador modulo
                                                    # de n con su base suamndo el resto de ny p sucesivamenete hasta que la condicion ya no se ecumpla
result =conversor(n,p) #solamaente lo renombramos la funcion recursiva
print("el resultado de",n,"en base ",p,"es",result) # imprimimos el valor  convertido



