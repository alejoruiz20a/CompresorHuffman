from collections import defaultdict
from NodoHuffman import *
import json

class Huff():
    def __init__(self, compressed, codigos):
        self.msg = compressed
        self.dicc = codigos

def comprimir(text=""):
    """
    Comprime un texto por medio del algoritmo de huffman.
    
    Parámetros:
    text (string): Texto a comprimir
    
    Retorna:
    Huff: Objeto que contiene:
        msg = mensaje comprimido.
        dicc = diccionario con los caminos.
    """
    frecuencias = tablaFrecuencias(text)
    arbol = construir_arbol_huffman(frecuencias)
    codigos = obtener_codigos_huffman(arbol)
    compressed = ""
    for caracter in text:
        compressed = compressed + codigos.get(caracter)
    compressed = stringToBytes(compressed)
    
    return Huff(compressed, codigos)

def descomprimir(compressed,dicc={}):
    """
    descomprime un texto por medio del algoritmo de huffman.
    
    Parámetros:
    compressed (bytearray): Texto a descomprimir en forma bytearray.
    dicc (dict): Diccionario con los caminos del arbol.
    
    Retorna:
    string: mensaje decodificado
    """
    
    msg = bytesToString(compressed)
    invertedDicc = {v: k for k, v in dicc.items()}
    decoded = ''
    code = ''
    
    while (len(msg)>0):
        code += msg[0]
        msg = msg[1:]
        caracter = invertedDicc.get(code,None)
        if caracter != None:
            decoded += caracter
            code = ''
    
    return decoded

def tablaFrecuencias(text=""):
    """
    Extrae una tabla de frecuencias a partir de un texto.
    
    Parámetros:
    text (string): Texto al que se requiera extraer tabla de frecuencias.
    
    Retorna:
    dict: diccionario con las frecuencias
    """
    
    frecuencias = defaultdict(int)
    for caracter in text:
        frecuencias[caracter] += 1
    return dict(frecuencias)

def stringToBytes(text = ""):
    """
    Transforma un texto a bytearray.
    
    Parámetros:
    text (string): Texto al que se requiera transformar a bytearray.
    
    Retorna:
    bytearray
    """
    while len(text) % 8 != 0:
        text += '0'  
    
    byteArray = bytearray()
    for i in range(0, len(text), 8):
        byte = text[i:i+8] 
        byteArray.append(int(byte,2))  
    
    print(byteArray)
    return byteArray

def bytesToString(bytes=bytearray):
    """
    Transforma un bytearray a string.
    
    Parámetros:
    bytes (bytearray): bytearray a transformar.
    
    Retorna:
    string
    """
    bitString = ''
    bits = bin(0)
    for byte in bytes:
        bits = bin(byte)[2:] 
        bits = bits.zfill(8)
        bitString += bits
        
    return bitString