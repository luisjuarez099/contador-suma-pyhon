def sumadepts():
    '''Se hara la suma por departamentos
    de marketing. '''
    num=0
    i=1
    print("Digita los RECURSOS que usaste para CAPTURAR clientes, (seo,mkt,email mkt, etc) \n")
    while i<=3:
        cmkt=int(input("Digita costos: "))
        num=cmkt+num
        i+=1
    print(num)
    cliente=int(input("Diigta los clientes que capturaste: "))
    cac=num/cliente
    print(f"Su costo por cliente es de : {cac}")

if __name__=='__main__':
    sumadepts()
    