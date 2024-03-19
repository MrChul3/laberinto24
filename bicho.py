import time

class Bicho:
    def __init__(self, modo):
        self.modo = modo
        self.poder = 2
        self.vida = 10
        self.posicion = None
        self.modo = modo
        self.num = 0
    
    def __str__(self):
        plantilla = 'Bicho-{0.modo}{0.num}'
        return plantilla.format(self)
    
    def esAgresivo(self):
        return self.modo.esAgresivo()

    def esPerezoso(self):
        return self.modo.esPerezoso()
    
    def actuar(self):
        self.modo.actuar(self)
    
    def caminarAleatoriamente(self):
        self.posicion.caminarAleatoriamente(self)
    
    def irAlNorte(self):
        self.posicion.irAlNorte(self)
    def irAlEste(self):
        self.posicion.irAlEste(self)
    def irAlSur(self):
        self.posicion.irAlSur(self)
    def irAlOeste(self):
        self.posicion.irAlOeste(self)
    def comenzar(self):
        self.actuar()
    def detener(self):
        print(self, " está detenido")
        exit(0)

class Modo:
    def __init__(self):
        pass
    def __str__(self):    
        pass
    def esAgresivo(self):
        return False
    def esPerezoso(self):
        return False
    def actuar(self, bicho):
        self.dormir(bicho)
        self.caminar(bicho)
    def caminar(self, bicho):
        bicho.caminarAleatoriamente()
    def dormir(self, bicho):
        print(bicho, " está durmiendo")
        time.sleep(3)

class Agresivo(Modo):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "Agresivo"
    
    def esAgresivo(self):
        return True

    def imprimir(self):
        print("Bicho Agresivo")

class Perezoso(Modo):
    def __init__(self):
        super().__init__()
    
    def __str__(self):    
        return "Perezoso"
    
    def imprimir(self):
        print("Bicho Perezoso")

    def esPerezoso(self):
        return True
