# CompresorHuffman

El algoritmo de Huffman es un método de compresión sin pérdida que asigna códigos de longitud variable a los símbolos, permitiendo así una eficiente compresión de archivos de texto. Este proyecto implementa este algoritmo junto con una interfaz grafica para ser una aplicación completa que permita abrir, editar, guardar, comprimir y descomprimir archivos de texto.

### **Características:**

* Apertura, edición y guardado de archivos de texto.
* Compresión del archivo abierto en el editor.
* Descompresión del archivo abierto en el editor.

## Instrucciones:

* **Botón Abrir:** Permite abrir un archivo de texto para cargarlo al editor de texto.
* **Botón Guardar**: Guarda el archivo que esté abierto en el momento en el editor. Si comenzaste a escribir en el editor sin estar trabajando sobre un archivo, se ejecuta la funcion Guardar Como.
* Botón Guardar Como: Guarda el texto que está en el editor en un nuevo archivo.
* **Botón Comprimir**:  Comprime el texto que se encuentre en el editor (sin importar si está guardado en un archivo o no) y lo guarda como un .huff en la ubicación deseada.
* **Botón Descomprimir**: Descomprime el archivo .huff de elección y lo carga al editor de texto. **Recuerda que solo está cargado en el editor, si quieres conservar la descompresión, debes usar los botones de guardado.**
* La checkbox permite elegir si incluir mayusculas en la compresión o pasar todo el archivo a minusculas.

## Funcionalidad:

### COMPRIMIR

1. Al presionar el botón Comprimir, se envía el texto que está cargado en el campo de texto a una función que retorna un diccionario con las frecuencias de cada caracter.
2. Con dicho diccionario, se crea el arbol de huffman por medio de una cola de prioridad que prioriza los caracteres con menor frecuencia, esta función retorna el nodo raiz del arbol.
3. Con este nodo, se recorre el arbol usando una función que guarda el camino de cada caracter, poniendo 1 a la derecha, 0 a la izquierda. Retornando así un diccionario con los caminos de cada caracter.
4. Haciendo uso de este diccionario de caminos, se codifica el mensaje original, dando como resultado una cadena de ceros y unos.
5. Esta cadena se envía a una función que transforma cada 8 bits en su representación en byte, creando así un bytearray. Por otro lado, el diccionario con los caminos se transforma en un JSON que se codifica en utf-8.
6. Por medio de With Open en modo escritura binaria, se escribe primero el JSON y luego el bytearray que contiene el mensaje, quedando así un archivo binario .huff.

### DESCOMPRIMIR

1. Al presionar descomprimir, se lee el archivo .huff y se extrae el JSON y el mensaje en bytearray.
2. Estos dos elementos se envían a una función que transforma el bytearray de nuevo a una cadena de unos y ceros, para luego decodificarla usando el JSON transformado a diccionario.
3. Esto nos da como resultado el mensaje original, el cual, se carga al campo de texto.


# NOTA
EN EL BRANCH DEVELOPMENT, SE EJECUTA CON EL ARCHIVO CLIENT.PY