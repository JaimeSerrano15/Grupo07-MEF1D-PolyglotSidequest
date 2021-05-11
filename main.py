from math_tools import *
from classes import *
from tools import *
from sel  import *

# Función Main la cual contiene el procedimiento general del algoritmo del MEF1D
def main() :

    m = mesh() #Creación de un objeto de la clase Mesh, que definirá la malla con la cual se trabajará
    
    #Se crean variables tipo List() que harán referencia a las matrices locales para la K y la b
    localKs, localbs = list(), list()

    #Se prepara la malla 'm' con toda la información necesaria para su utilización
    leerMallayCondiciones(m)

    #Con la ayuda a la malla 'm' se construyen las matrices locales para K y b de cada elemento
    crearSistemasLocales(m,localKs, localbs)

    #Se preparan las matrices K y b globales, tratándolas como una matriz de cero de primer momento
    K = zeroesMatrix(m.getSize(sizes.NODES.value))
    b = zeroesVector(m.getSize(sizes.NODES.value))

    # Comienza al proceso de ensamblaje las matrices K y b globales
    ensamblaje(m, localKs, localbs, K, b)

    #Se aplican las condiciones de Neumann definidas
    applyNeumann(m,b)

    #Se aplican las condiciones de Dirichlet definidas
    applyDirichlet(m,K,b)

    #Se prepara el vector de ceros T que servirá para almacenar las respuestas obtenidas
    T = zeroesVector(len(b))

    #Se calcula la información de T mediante la resolución del SEL
    T = calculate(K,b)

    #Se presentan los resultados obtenidos
    print("La respuesta es: ")
    print(T)

#Llamada al método Main() para poder correr el código de implementación del algoritmo del MEF1D
main()