from classes import *
from math_tools import *

#La función recibe: Un elemento y la malla con la que se está trabajando
#La función se encarga de construir la matriz K local para el elemento enviado,
#que de acuerdo a la formulación planteada, tiene la forma: (k/l) * [1 -1 ; -1 1]
def createLocalK(element, m) :
    K, row1, row2 = list(), list(), list()

    k = m.getParameter(parameters.THERMAL_CONDUCTIVITY.value)
    l = m.getParameter(parameters.ELEMENT_LENGTH.value)

    row1.append(k/l)
    row1.append(-k/l)
    row2.append(-k/l)
    row2.append(k/l)

    K.append(row1)
    K.append(row2)

    return K

#La función recibe: Un elemento y la malla con la que se está trabajando
#La función se encarga de construir la matriz b local para el elemento enviado,
#que de acuerdo a la formulación planteada, tiene la forma: (Q*l/2) * [1 ; 1]
def createLocalb(element, m) :
    b = list()

    q = m.getParameter(parameters.HEAT_SOURCE.value)
    l = m.getParameter(parameters.ELEMENT_LENGTH.value)
    b.append(q * l/2)
    b.append(q * l/2)

    return b

#La función recibe: La malla con la que se trabaja, la lista que contiene las matrices locales de K
# y una lista que contiene los vectores locales de b. La función construye para cada elementos la matriz K
# y el vector b, almacenándolos en sus respectivas listas
def crearSistemasLocales(m, localKs, localbs) :
    for i in range(m.getSize(sizes.ELEMENTS.value)) :
        localKs.append(createLocalK(i,m))
        localbs.append(createLocalb(i,m))

#La función recibe: El elemento en el que se trabaja, su matriz local K y la matriz global K
#La función se encarga de incorporar, referente al elemento trabajo, la matriz local K en la matriz global K
def assemblyK(e, localK, K) :
    index1 = e.node1 - 1
    index2 = e.node2 - 1

    K[index1][index1] += localK[0][0]
    K[index1][index2] += localK[0][1]
    K[index2][index1] += localK[1][0]
    K[index2][index2] += localK[1][1]

#La función recibe: El elemento en el que se trabaja, su matriz local b y la matriz global b
#La función se encarga de incorporar, referente al elemento trabajo, la matriz local b en la matriz global b
def assemblyb(e, localb, b) :
    index1 = e.node1 - 1
    index2 = e.node2 - 1

    b[index1] += localb[0]
    b[index2] += localb[1]

#La función recibe: La malla con la que se está trabajando, las listas de las Ks y bs locales, y la K y b globales
#La función proceda a ensamblar cada sistema local, referente a cada uno de los elementos, dentro del sistema global
def ensamblaje(m, localKs, localbs, K, b) :
    for i in range(m.getSize(sizes.ELEMENTS.value)) :
        e = m.getElement(i)

        assemblyK(e, localKs[i], K)
        assemblyb(e, localbs[i], b)

#La función recibe: La malla con la que se está trabajando y el vector b global.
#La función aplica las condiciones de Neumann establecidas, en las posiciones (nodos) de la b global que se definieron
def applyNeumann(m, b) :
    for i in range(m.getSize(sizes.NEUMANN.value)) :
        c = m.getCondition(i, sizes.NEUMANN.value)

        b[c.node1 - 1] += c.value


#La función recibe: La malla con la que se está trabajando, la matriz global K y el vector global B
#La función aplica las condiciones de Dirichlet establecidas, donde se elimina la fila correspondiente y cambiando de lado
#de la ecuación las columnas correspondientes
def applyDirichlet(m, K, b) :
    for i in range(m.getSize(sizes.DIRICHLET.value)) :
        c = m.getCondition(i, sizes.DIRICHLET.value)

        index = c.node1 - 1
        del K[index]
        del b[index]

        for row in range(len(K)) :
            cell = K[row][index]

            del K[row][index]

            b[row] += -1 * c.value * cell

#La función recibe: La K global y la b global
#En esta función se define el procedimiento para calcular el vector T de resultados
def calculate(K, b) :

    Kinv = inverseMatrix(K)

    T = productMatrixbyVector(Kinv, b)
    return T


