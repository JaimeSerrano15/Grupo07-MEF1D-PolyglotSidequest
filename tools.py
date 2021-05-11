from classes import *

#La función recibe:
# -El archivo que contiene la información con la cual se trabajará
# -Las lineas que se omitirán
# -El número de filas que contienen la información a extraer
# -Una lista de objetos para almacenar la información extraída
# -Un índice que indica el tipo de objeto que se almacenará
# La función se encarga de ir leyendo el archivo y almacenar los datos de los nodos, elementos y condiciones con las
# cuales se trabajará. El cómo se leerá el archivo y el tipo de dato que se irá extrayendo y almacenando dependerá de
# los parámetros que sean enviados
def obtenerDatos(file, nlines, n, mode, item_list, obj) :
    file.readline()
    
    if(nlines == lines.DOUBLELINE.value) :
        file.readline()
    
    for i in range(n) :
        if mode == modes.INT_FLOAT.value :
            if i == 0 and obj == 2 : file.readline()
            row = file.readline()
            data = row.split("\t")
            data[0] = int(data[0])
            data[1] = float(data[1].split("\n")[0])
            
            if obj == 0 :
                item_list.append(node())
                item_list[i].setIntFloat(data[0], data[1])
            
            elif obj == 2 :
                item_list.append(condition())
                item_list[i].setIntFloat(data[0], data[1])

        elif mode == modes.INT_INT_INT.value :
            if i == 0 :file.readline()
            row = file.readline()
            data = row.split(" ")
            data[0] = int(data[0])
            data[1] = int(data[1])
            data[2] = int(data[2].split("\n")[0])
            item_list.append(element())
            item_list[i].setIntIntInt(data[0], data[1], data[2])
    

#La función recibe: La malla con la que está trabajando
#En esta función se declara la variable que servirá para el manejo del archivo que contiene la información del problema
# Se procederá a leer y almacenar los datos de interés que se encuentran en dicho archivo, como lo son las variables l,k,q
# el número de nodos, elementos, etc.
def leerMallayCondiciones(m) :
    
    while True :
        fname = input("Ingrese el nombre del archivo que contiene los datos de la malla: ")
        try:
            file = open(fname, "r")
            break
        except:
            continue
    
    row = file.readline().split(" ")
    l = float(row[0])
    k = float(row[1])
    q = float(row[2].split("\n")[0])

    row = file.readline().split(" ")
    nnodes = int(row[0])
    neltos = int(row[1])
    ndirich = int(row[2])
    nneu = int(row[3].split("\n")[0])
    
    m.setParameters(l,k,q)
    m.setSizes(nnodes, neltos, ndirich, nneu)

    obtenerDatos(file, lines.DOUBLELINE.value, nnodes, modes.INT_FLOAT.value, m.getNode_list(), 0)
    obtenerDatos(file, lines.DOUBLELINE.value, neltos, modes.INT_INT_INT.value, m.getElement_list(),1)
    obtenerDatos(file, lines.DOUBLELINE.value, ndirich, modes.INT_FLOAT.value, m.getDirichlet_list(),2)
    obtenerDatos(file, lines.DOUBLELINE.value, nneu, modes.INT_FLOAT.value, m.getNeumann_list(),2)

    file.close()
