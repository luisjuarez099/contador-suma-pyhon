# def sumatoria(a,b):
#     result=a+b
#     print(result)
# a=int(input("Digita un numero: "))
# b=int(input("Digita un numero: "))



# def name(name):
#     return name
# name=input("Digita tu nombre: ")
# print(f"Hola {name}")

def promedio():
    print("Conoceremos el promedio")
    dato=0
    i=1
    while i<=4:
        num=int(input(f"Digita un numero {i}: "))
        dato=num+dato
        print(dato)
        i+=1
    print(f"El resultado de sus numeros agregados es de {dato}")
if __name__== '__main__':
    # sumatoria(a,b)
    # name
    promedio()

    