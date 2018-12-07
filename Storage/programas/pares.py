numeros = []
pares = []
N = int(input("ingrese la cantidad de numeros que desea ingresar: "))

for I in range(N):
    numeros.append(input("ingrese un numero: "))
print("Los numeros ingresados son: ", numeros)
numeros.sort()
print("Los numeros ordenados ascendentemente son: ", numeros)

for I in numeros:
    if int(I) % 2 == 0:
        pares.append(I)
print(pares)
