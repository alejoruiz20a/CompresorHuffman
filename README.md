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
* Botón Comprimir:  Comprime el texto que se encuentre en el editor (sin importar si está guardado en un archivo o no) y lo guarda como un .huff en la ubicación deseada.
* Botón Descomprimir: Descomprime el archivo .huff de elección y lo carga al editor de texto. **Recuerda que solo está cargado en el editor, si quieres conservar la descompresión, debes usar los botones de guardado.**
