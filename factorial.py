def calcularfactorial(numero):
    contador=1
    if numero==0: 
        resultado=1
    else:
        resultado=numero
    while contador<numero:
        resultado=resultado*contador
        contador=contador+1
    print(f"el factorial de {numero} es {resultado}")

def rangofactorial(numfinal):
    for inicio in range(numfinal+1):
        calcularfactorial(inicio)

numero=int(input("ingrese el numero para calcular el factorial"))
#calcularfactorial(numero)
rangofactorial(numero)