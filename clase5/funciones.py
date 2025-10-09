#Ejemplo de funciones

def sumar(a,b):
    r=a+b
    return r
resultado=sumar(5,4)
print(f"El resultado de la suma es: {resultado}")


print("----------")
def suma(a,b):
    r=a+b 
    print(f"sumando dentro de la funcion: {a} + {b} = {r}")
    return r
a=5
b=1
resultado=suma(a,b)
print("fuera de la funcion")
print(f"el resultado de la funcin es: {resultado}")