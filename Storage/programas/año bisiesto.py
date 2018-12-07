print("ingrese el año: ")
año = int(input())

if año % 400 == 0:
    print("Es Bisiesto")
elif año % 4 == 0 and año % 100 != 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")
