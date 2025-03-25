import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename
from tkinter import simpledialog, messagebox, PhotoImage
from Compresor import comprimir, bytesToString, descomprimir
import json, os, sys

def resource_path(relative_path):
    """ Obtiene la ruta absoluta al archivo de recurso, sea en el directorio de ejecución o empaquetado. """
    try:
        # PyInstaller crea una carpeta temporal y almacena el ejecutable en ella
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Client():
    def __init__ (self):
        super().__init__()
        self.ventana = tk.Tk()
        self.ventana.title("Compresor de Texto")
        self.campoDeTexto = tk.Text(self.ventana,wrap=tk.WORD)
        self.ventana.resizable(0,0)
        self.archivo = None
        self.ventana.iconphoto(False,PhotoImage(file=resource_path("icon.png")))
        self.archivoAbierto = None
        self.ventana.geometry("900x700")
        self.ventana.configure(bg="#2c3e50")
        self.caps = tk.BooleanVar()
        self.crearComponentes()
        self.ventana.mainloop()
    
    def crearComponentes(self):
        # Colores y estilos
        boton_bg = "#34495e"  # Color de fondo de los botones
        boton_fg = "#ecf0f1"  # Color del texto de los botones
        boton_hover = "#1abc9c"  # Color al pasar el cursor sobre los botones
        boton_font = ("Cascadia Code", 12, "bold")  # Fuente de los botones
        
        texto_bg = "#ecf0f1"  # Fondo de campo de texto
        texto_fg = "#2c3e50"  # Color del texto

        frame_botones = tk.Frame(self.ventana, bg="#2c3e50", bd=2)
        
        boton_abrir = tk.Button(frame_botones, text="Abrir", command=self.abrirArchivo, bg=boton_bg, fg=boton_fg, font=boton_font, relief=tk.FLAT)
        boton_guardar = tk.Button(frame_botones, text="Guardar", command=self.guardarArchivo, bg=boton_bg, fg=boton_fg, font=boton_font, relief=tk.FLAT)
        boton_guardar_como = tk.Button(frame_botones, text="Guardar como", command=self.guardarArchivoComo, bg=boton_bg, fg=boton_fg, font=boton_font, relief=tk.FLAT)
        boton_comprimir = tk.Button(frame_botones, text="Comprimir", command=self.comprimirArchivo, bg=boton_bg, fg=boton_fg, font=boton_font, relief=tk.FLAT)
        boton_descomprimir = tk.Button(frame_botones, text="Descomprimir", command=self.descomprimirArchivo, bg=boton_bg, fg=boton_fg, font=boton_font, relief=tk.FLAT)
        self.campoDeTexto = tk.Text(self.ventana, wrap=tk.WORD, height=35, width=64, bg=texto_bg, fg=texto_fg, font=("Arial", 12))
        scroll = tk.Scrollbar(self.ventana, command=self.campoDeTexto.yview)
        checkCaps = tk.Checkbutton(frame_botones, text="Incluir mayúsculas en la compresión", variable=self.caps, bg="#2c3e50", fg=boton_fg, font=("Arial", 11, "italic"), selectcolor=boton_bg, relief=tk.FLAT)
        label = tk.Label(self.ventana,text="DESARROLLADO POR ALEJANDRO AMADOR RUIZ",bg=boton_bg,fg=boton_fg,font=boton_font)

        boton_abrir.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        boton_guardar.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        boton_guardar_como.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        boton_comprimir.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        boton_descomprimir.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        checkCaps.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
        label.grid(row=1, column=0, padx=5, pady=5, sticky="ew",columnspan=2)
        
        frame_botones.grid(row=0, column=0, sticky="n")
        self.campoDeTexto.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        self.campoDeTexto.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=2, sticky="ns")
        
        # Aplicar un hover effect a los botones
        for boton in [boton_abrir, boton_guardar, boton_guardar_como, boton_comprimir, boton_descomprimir]:
            boton.bind("<Enter>", lambda e, b=boton: b.config(bg=boton_hover))
            boton.bind("<Leave>", lambda e, b=boton: b.config(bg=boton_bg))
        
    def abrirArchivo(self):
        """
        Abre un archivo de texto del dispositivo y lo inserta en el campo de texto.
        """
        try:
            self.archivoAbierto = askopenfile(mode="r+").name
            with open(self.archivoAbierto,"r+",encoding='utf-8') as self.archivo:
                self.campoDeTexto.delete(1.0,tk.END)
                texto = self.archivo.read()
                self.campoDeTexto.insert(1.0,texto)
                self.ventana.title(f"Compresor de Texto - {self.archivo.name}")
        except:
            return
            
    def guardarArchivo(self):
        """
        Guarda el archivo abierto, si no es un archivo abierto, llama a guardarArchivoComo.
        """
        if self.archivoAbierto:
            with open (self.archivoAbierto,"w", encoding='utf-8') as self.archivo:
                self.archivo.write(self.campoDeTexto.get(1.0,tk.END))
                simpledialog.messagebox.showinfo("Éxito","Archivo guardado con éxito")
        else:
            self.guardarArchivoComo()
    
    def guardarArchivoComo(self):
        """
        Guarda un archivo con el contenido del campo de texto.
        """
        self.archivoAbierto = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")], 
            title="Guardar Archivo",
        )        
        if self.archivoAbierto: 
            with open(self.archivoAbierto, 'w', encoding='utf-8') as self.archivo:
                self.archivo.write(self.campoDeTexto.get(1.0,tk.END))
            simpledialog.messagebox.showinfo("Archivo guardado con éxito",f"Archivo guardado en: {self.archivoAbierto}")
            self.ventana.title(f"Editor de Texto - {self.archivo.name}")
        else:
            return
    
    def comprimirArchivo(self):
        """
        Guarda un archivo binario creado a partir del mensaje comprimido en huffman y los caminos generados por el mismo.
        """
        texto = self.campoDeTexto.get(1.0,tk.END)
        if not self.caps.get():
            texto = texto.lower()
        size = len(texto.encode('utf-8'))*8
        huff = comprimir(texto)
        self.archivoAbierto = asksaveasfilename(
            defaultextension=".huff",
            filetypes=[("Archivos Comprimidos Huffman","*.huff")],
            title="Comprimir Archivo"
        )
        if self.archivoAbierto:
            with open(self.archivoAbierto, 'wb') as self.archivo:
                dicc = json.dumps(huff.dicc)
                self.archivo.write(dicc.encode('utf-8') + b'\r\n')
                self.archivo.write(huff.msg)
                self.archivo.seek(0,2)
                sizeNow = self.archivo.tell()*8
            simpledialog.messagebox.showinfo("Archivo comprimido con éxito",f"Archivo guardado en: {self.archivoAbierto}\nTamaño original: {size} bits\nTamaño comprimido: {sizeNow} bits")
            self.archivoAbierto = None
            self.archivo = None
            self.campoDeTexto.delete(1.0,tk.END)
            self.ventana.title("Compresor de Texto")
            
    def descomprimirArchivo(self):
        """
        Descomprime un archivo del dispositivo.
        """
        msg = ''
        decoded = ''
        dicc = object
        self.campoDeTexto.delete(1.0,tk.END)
        self.archivoAbierto = askopenfile(
            defaultextension=".huff",
            filetypes=[("Archivos Comprimidos Huffman","*.huff")],
            title="Descomprimir Archivo"
        )
        if self.archivoAbierto:
            with open(self.archivoAbierto.name,'rb') as self.archivo:
                dicc = json.loads(self.archivo.readline()[:-2].decode('utf-8').strip())
                msg = self.archivo.read()
            decoded = descomprimir(msg,dicc)
            self.campoDeTexto.insert(1.0, decoded) 
            self.archivoAbierto = None
            self.archivo = None
            simpledialog.messagebox.showinfo("Éxito","Archivo descomprimido con éxito")
              
if __name__ == "__main__":
    editor = Client()