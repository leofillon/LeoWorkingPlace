def menu():
    print("respondió dani?")
    print("ingrese las posibliledades [1(si) o 2(no), 0 para salir]:")
    pos = int(input())
    return pos

def Leo_Response():
    print("escribe tu rta")
    response = input()
    print("mensaje enviado: " + response)
    pass


while True:
    pos = menu()
    if pos == 1:
        Leo_Response()
    elif pos == 2:
        print("adios vaquero :'(")
    elif pos == 0:
        break;
    else:
        print("opcion invalida pt")
        