import sys

#Función que devuelve una matriz cuadrada de ceros de un tamaño solicitado
def zeroesMatrix(n) :
    return [ [0.0 for i in range(n)] for j in range(n)]

#Función que devuelve un vector de ceros de un tamaño solicitado
def zeroesVector(n) :
    return [0.0 for i in range(n)]

#Función de devuelve la copia de una matriz especificada
def copyMatrix(M) :
    return M[:]

#Función que devuelve el resultado (Vector) de un producto MatrizXVector
def productMatrixbyVector(M, V) :
    R = zeroesVector(len(V))
    for f in range(len(M)) :
        cell = 0.0

        for c in range(len(V)) :
            cell += M[f][c] * V[c]
        
        R[f] += cell
    
    return R

#Función que devuelve el resultado (Matriz) del un producto MatrizXReal
def productRealbyMatrix(real, M) :
    R = zeroesMatrix(len(M))

    for f in range(len(M)) :
        for c in range(len(M[0])) :
            R[f][c] = M[f][c] * real
    
    return R

#Función que determina y devuelve el Menor de una matriz, recibiendo la fila y columna a eliminar
def MatrixMinor(M,f,c) :
    return [row[:c] + row[c+1:] for row in (M[:f] + M[f+1:])]

#Función que calcula y devuelve del determinante de una Matriz
def determinant(M) :
    if len(M) == 1 :
        return M[0][0]
    else :
        det = 0.0

        for i in range(len(M[0])) :
            minor = copyMatrix(M)
            minor = MatrixMinor(minor,0,i)

            det += ((-1)**i) * M[0][i] * determinant(minor)

        return det

#Función que calcula la matriz de cofactores de una Matriz solicitada
def cofactors(M) :
    cof = zeroesMatrix(len(M))

    for f in range(len(M)) :
        for c in range(len(M[0])) :
            minor = copyMatrix(M)
            minor = MatrixMinor(minor,f,c)

            cof[f][c] = ((-1)**(f+c)) * determinant(minor)
    
    return cof

#Función que calcula la transpuesta de una matriz solicitada
def transpose(M) :
    T = zeroesMatrix(len(M))

    for i in range(len(M)) :
        for j in range(len(M[0])) :
            T[j][i] = M[i][j]
    
    return T

#Función que calcula la inversa de una Matriz solicitada
def inverseMatrix(M) :
    det = determinant(M)

    if det == 0 :
        sys.exit("Divide by zero? NO!")
    
    cof = cofactors(M)
    adj = transpose(cof)

    inv = productRealbyMatrix(1/det, adj)

    return inv
