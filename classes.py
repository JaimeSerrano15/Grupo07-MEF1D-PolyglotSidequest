import abc
from enum import Enum

#Clases Enum que servirán para darle un extra de legibilidad al código implementado
class lines(Enum) :
    NOLINE = 0
    SINGLELINE = 1
    DOUBLELINE = 2

class modes(Enum) :
    NOMODE = 0
    INT_FLOAT = 1
    INT_INT_INT = 2

class parameters(Enum) :
    ELEMENT_LENGTH = 0
    THERMAL_CONDUCTIVITY = 1
    HEAT_SOURCE = 2

class sizes(Enum) :
    NODES = 0
    ELEMENTS = 1
    DIRICHLET = 2
    NEUMANN = 3

#Clase abstracta de propósito general que sirve para representar un 'item' cualquiera dentro de una malla
class item :

    _id = 0 # Identificador
    _x = 0.0 # Posición en X
    _node1 = 0 # Identificador del primero nodo
    _node2 = 0 # Identificador del segundo nodp
    _value = 0 # Valor que contiene el objeto

    # Getters para los atributos
    @property
    def id(self) :
        return self._id
    
    @property
    def x(self) :
        return self._x
    
    @property
    def node1(self) :
        return self._node1
    
    @property
    def node2(self) :
        return self._node2
    
    @property
    def value(self) :
        return self._value

    # Métodos abstractos para instanciar ciertos atributos de acuerdo a lo que se necesite
    @abc.abstractmethod
    def setIntFloat(self,n,r) :
        pass

    @abc.abstractmethod
    def setIntIntInt(self,n1,n2,n3) :
        pass


#Clase que representa un nodo dentro de la malla. Hereda de la clase 'item'
class node(item) :

    def setIntFloat(self,identifier, x_coordinate):
        self._id = identifier
        self._x = x_coordinate
    
    def setIntIntInt(self, n1, n2, n3):
        return super().setIntIntInt(n1, n2, n3)

#Clase que representa un elemento dentro de la malla. Hereda de la clase 'item'
class element(item) :

    def setIntFloat(self, n, r):
        return super().setIntFloat(n, r)
    
    def setIntIntInt(self, identifier, firstnode, secondnode):
        self._id = identifier
        self._node1 = firstnode
        self._node2 = secondnode

#Clase que repsenta una condición establecida sobre un nodo de la malla. Hereda de la clase 'item'
class condition(item) :

    def setIntFloat(self, node_to_apply, prescribed_value):
        self._node1 = node_to_apply
        self._value = prescribed_value

    def setIntIntInt(self, n1, n2, n3):
        return super().setIntIntInt(n1, n2, n3)

#Clase que representa la malla a trabajar
class mesh :

    parameters = [0.0,0.0,0.0] #Los parametros del modelo a trabajar (Para este ejercicio: l,k y Q)
    sizes = [0,0,0,0] # El número de nodos, elementos y condiciones a aplicar (De Neumann y Dirichlet)
    node_list = list() # Lista de nodos
    element_list = list() # Lista de elementos
    dirichlet_list = list() # Lista de condiciones de Dirichlet
    neumann_list = list() # Lista de condiciones de Neumann

    #Método que se encarga de almacenar los parámetros l,k y Q
    def setParameters(self, l, k, q) :
        self.parameters[parameters.ELEMENT_LENGTH.value] = l
        self.parameters[parameters.THERMAL_CONDUCTIVITY.value] = k
        self.parameters[parameters.HEAT_SOURCE.value] = q
    
    #Método que se encarga de almacenar el número de nodos, elementos y condiciones (De Dirichlet y de Neumann)
    def setSizes(self, nnodes, neltos, ndirich, nneu) :
        self.sizes[sizes.NODES.value] = nnodes
        self.sizes[sizes.ELEMENTS.value] = neltos
        self.sizes[sizes.DIRICHLET.value] = ndirich
        self.sizes[sizes.NEUMANN.value] = nneu
    
    #Método para obtener una cantidad específica
    def getSize(self,s) :
        return self.sizes[s]
    
    #Método para obtener un parámetro específico
    def getParameter(self, p) :
        return self.parameters[p]
    
    def getNode_list(self) :
        return self.node_list
    
    #Getters de las listas atributo
    def getElement_list(self) :
        return self.element_list
    
    def getDirichlet_list(self) :
        return self.dirichlet_list
    
    def getNeumann_list(self) :
        return self.neumann_list
    
    #Método para obtener un nodo específico
    def getNode(self, i) :
        return self.node_list[i]
    
    #Método para obtener un elemento específico
    def getElement(self, i) :
        return self.element_list[i]
    
    #Método para obtener una condición específica
    def getCondition(self, i, con) :
        if con == sizes.DIRICHLET.value :
            return self.dirichlet_list[i]
        else :
            return self.neumann_list[i]
    

