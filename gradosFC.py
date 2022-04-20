
def promedio():
    print("Conoceremos el promedio")
    dato=0
    i=1
    while i<=4:
        num=int(input(f"Digita un numero {i}: "))
        dato=num+dato
        i+=1
    print(f"El resultado de sus numeros agregados es de {dato}")
if __name__== '__main__':
    promedio()

    