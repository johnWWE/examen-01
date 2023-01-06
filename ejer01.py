'''implemente un algoritmo, usando una función recursiva, que resuelva la
siguiente
sumatoria: K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + ... + n ∗ p'''

#ingreso de datos
n=int(input("Ingrese un valor 'n' => "))
p=int(input("Ingrese un valor  'p'=> "))

#definimos una funcion recursiva
def sumaRecursiva(n,p,i=1):  # i=1 ya quqe la premisa del ejercicio eel numero incremente en 1, 1*p + 2*p + 3*p....
    #el caso base
    if n==0:
        return 0  # no habria ninguna operacion
    elif p==0:
        return 0   #siempre seran un numero n veces 0 >> 0+0+0...

    # el caso recursivo
    else:
        return (p*i) + sumaRecursiva(n-1,p,i+1)  # devuelve el mismo p sumada con sumaRecur(n-1,p,i+1)
                                                #sucesivamente hasta que las condicionales iniciales ya no se cumplan
#imprimiremos el valor de la sumatoria
print("el resultado de valores ", n,"y",p," es =>", sumaRecursiva(n,p))