from ast import literal_eval as make_tuple


def menu():
    print("-----------------------------------------------------------------------------------------------------")
    print("NUEVO BLACKBOARD PARA PROFES")
    print("-----------------------------------------------------------------------------------------------------")
    print("1. Ingresa las matriculas del primer grupo")
    print("2. Ingresa las matriculas del segundo grupo")
    print("3. Generar grupo con los dos grupos")
    print("4. Generar grupo con alumnos en ambos grupos")
    print("5. Mostrar todos los equipos posibles en algun grupo")
    print("6. Generar todas las parejas de estudio posibles entre ambos grupos")
    print("7. Ordenar matricualas de algun grupo de manera ascendente")
    print("8. Revisar si un grupo de matriculas pertenece parcialmente o por completo a alguno de los dos grupos")
    print("9. Salir del NUEVO BLACKBOARD PARA PROFESORES")
    print("-----------------------------------------------------------------------------------------------------")
    print("ingrese la opcion [1-9]: ")
    opcion = int(input())
    return opcion


def ingresar_matricula_primer_grupo():
    print("Ingrese las matriculas del primer grupo separadas por una coma \',\': ")
    g1 = open("g1", "w")
    g1.write(str(input()))
    g1.close()
    print("Grupo generado exitosamente")


def ingresar_matricula_segundo_grupo():
    print("Ingrese las matriculas del segundo grupo separadas por una coma \',\': ")
    g2 = open("g2", "w")
    g2.write(str(input()))
    g2.close()
    print("Grupo generado exitosamente")


def generar_grupo_unificado():
    g1 = open("g1", "r")
    g2 = open("g2", "r")
    g3 = open("g3", "w")
    t1 = make_tuple(g1.read())
    t2 = make_tuple(g2.read())
    tx = t1 + t2
    t3 = tuple(sorted(set(tx)))
    g3.write(str(t3))
    g1.close()
    g2.close()
    g3.close()
    print("Se genero un tercer grupo con los los grupos 1 y 2")


def generar_grupos_mixtos():
    g1 = open("g1", "r")
    g2 = open("g2", "r")
    g3 = open("g3", "r")
    g4 = open("g4", "w")
    t1 = make_tuple(g1.read())
    t2 = make_tuple(g2.read())
    t4 = tuple(set(t1).intersection(set(t2)))
    g4.write(str(t4))
    g1.close()
    g2.close()
    g3.close()
    g4.close()
    pass


def mostrar_todos_los_equipos_posibles_del_grupo():
    print("indique el grupo en el cual se generaran los equipos: (1,2) ")
    option = int(input())
    g1 = open("g1", "r")
    g2 = open("g2", "r")
    t1 = make_tuple(g1.read())
    t2 = make_tuple(g2.read())
    ps = tuple()
    if option == 1:
       for e1 in t1:
           for e2 in t1:
               p = (e1, e2)
               ps = ps + (p,)
       print(ps)
    if option == 2:
       for e1 in t2:
           for e2 in t2:
               p = (e1, e2)
               ps = ps + (p,)
       print(ps)
    g1.close()
    g2.close()
    pass


def generar_parejas_mixtos():
    g1 = open("g1", "r")
    g2 = open("g2", "r")
    t1 = make_tuple(g1.read())
    t2 = make_tuple(g2.read())
    ps = tuple()
    for e1 in t1:
        for e2 in t2:
            p = (e1, e2)
            ps = ps + (p,)
    print(ps)
    g1.close()
    g2.close()
    pass


def ordenar_matriculas_del_grupo():
    print("indique el grupo que desea ordenar (1, 2, 3): ")
    option = int(input())
    g1 = open("g1", "r")
    g2 = open("g2", "r")
    g3 = open("g3", "r")
    if option == 1:
      for lines in g1:
        matriculas = lines.split(", ")
        print(sorted(matriculas))
    elif option == 2:
      for lines in g2:
        matriculas = lines.split(", ")
        print(sorted(matriculas))
    elif option == 3:
      for lines in g3:
        matriculas = lines.split(", ")
        print(sorted(matriculas))
    else:
      print("opción invalida")
    g1.close()
    g2.close()
    g3.close()
    pass


def revisar_matriculas_entre_grupos():
    
    pass


while True:
    opcion = menu()
    if opcion == 9:
        break;

    if opcion == 1:
        ingresar_matricula_primer_grupo()
    elif opcion == 2:
        ingresar_matricula_segundo_grupo()
    elif opcion == 3:
        generar_grupo_unificado()
    elif opcion == 4:
        generar_grupos_mixtos()
    elif opcion == 5:
        mostrar_todos_los_equipos_posibles_del_grupo()
    elif opcion == 6:
        generar_parejas_mixtos()
    elif opcion == 7:
        ordenar_matriculas_del_grupo()
    elif opcion == 8:
        revisar_matriculas_entre_grupos()
    elif opcion == 9:
        break;
    else:
        print("Opcion invalida")
