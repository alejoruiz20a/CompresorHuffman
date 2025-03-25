from ColaPrioridad import ColaPrioridad

class NodoHuffman:
    def __init__(self, simbolo, frecuencia, izquierdo=None, derecho=None):
        """
        Parámetros:
        simbolo (char): Caracter que contiene el nodo.
        frecuencia (int): Frecuencia de la suma de los nodos hijos.
        izquierdo (NodoHuffman): Nodo hijo izquierdo.
        derecho (NodoHuffman): Nodo hijo derecho
        """
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierdo = izquierdo
        self.derecho = derecho

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(frecuencias={}):
    """
    Construye el arbol de huffman.
    
    Parámetros:
    frecuencias (dict): Diccionario de frecuencias de caracteres.
    
    Retorna:
    NodoHuffman: Raiz del arbol de huffman.
    
    """
    cola = ColaPrioridad()
    
    for simbolo, frecuencia in frecuencias.items(): 
        nodo = NodoHuffman(simbolo, frecuencia)
        cola.insertar(nodo)
    
    while len(cola.items) > 1: #CREA EL ARBOL
        izquierdo = cola.extraer_minimo()
        derecho = cola.extraer_minimo()
        nodo_padre = NodoHuffman(None, izquierdo.frecuencia + derecho.frecuencia, izquierdo, derecho)
        cola.insertar(nodo_padre)

    return cola.extraer_minimo()

def obtener_codigos_huffman(nodo, codigo_actual="", codigos=None):
    """
    Obtiene los caminos de cada caracter a partir de la raiz del arbol.
    
    Parámetros:
    nodo (NodoHuffman): Raiz del arbol de huffman.
    
    Retorna:
    dict: Diccionario que contiene los caminos de cada aracter
    
    """
    if codigos is None:
        codigos = {}

    if nodo.simbolo is not None:
        codigos[nodo.simbolo] = codigo_actual
    else:
        if nodo.izquierdo is not None:
            obtener_codigos_huffman(nodo.izquierdo, codigo_actual + "0", codigos)
        
        if nodo.derecho is not None:
            obtener_codigos_huffman(nodo.derecho, codigo_actual + "1", codigos)

    return codigos