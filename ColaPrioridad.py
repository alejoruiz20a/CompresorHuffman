class ColaPrioridad:
    def __init__(self):
        self.items = []

    def insertar(self, nodo):
        self.items.append(nodo)
        self.items.sort()  

    def extraer_minimo(self):
        return self.items.pop(0)  

    def vacia(self):
        return len(self.items) == 0

