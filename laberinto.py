import random

class ElementoMapa:
    def __init__(self):
        pass
    
    def entrar(self, alguien):
        pass

    def imprimir(self):
        print("ElementoMapa")
    
    def esHabitacion(self):
        return False

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones=[]

    def agregarHijo(self, componente):
        self.hijos.append(componente)

    def removerHijo(self, componente):
        self.hijos.remove(componente)
    
    def imprimir(self):
        print("Contenedor")
    
    def caminarAleatoriamente(self, alguien):
        pass
    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)
    
    def removerOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def caminarAleatoriamente(self, alguien):        
        orientacion = self.getOrientacionAleatoria()
        orientacion.caminarAleatoriamente(alguien)

    def getOrientacionAleatoria(self):
        return random.choice(self.orientaciones)
    
    def irNorte(self, alguien):
        self.norte.entrar(alguien)
    def irEste(self, alguien):
        self.este.entrar(alguien)
    def irSur(self, alguien):
        self.sur.entrar(alguien)
    def irOeste(self, alguien):
        self.oeste.entrar(alguien)
    def establecerEMinOr(self, em, orientacion):
        orientacion.establecerEMinOr(em, self)

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def agregarHabitacion(self, habitacion):
        self.agregarHijo(habitacion)

    def entrar(self, alguien):
        self.hijos[0].entrar(alguien)

    def imprimir(self):
        print("Laberinto")   
    
    def obtenerHabitacion(self, id):
        for habitacion in self.hijos:
            if habitacion.id == id:
                return habitacion
        return None
   

class Habitacion(Contenedor):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
    def entrar(self, alguien):
        print(alguien + " entra a la habitación", self.id)
    
    def imprimir(self):
        print("Habitación")

    def esHabitacion(self):
        return True
    
class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()
    
    def imprimir(self):
        print("Hoja")

class Decorador(Hoja):
    def __init__(self):
        super().__init__()
        self.comp = None
    
    def imprimir(self):
        print("Decorador")

class Bomba(Decorador):
    def __init__(self):
        super().__init__()
        self.activa = False

    def imprimir(self):
        print("Bomba")

    def entrar(self, alguien):
        print(alguien + " chocó contra una bomba")

class Pared(ElementoMapa):
    def __init__(self):
        pass
    
    def imprimir(self):
        print("Pared")

    def entrar(self, alguien):
        print(alguien , " chocó contra una pared")

# bombedwall.py

class ParedBombardera(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False
    
    def imprimir(self):
        print("ParedBombardera")

# door.py

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False
    
    def entrar(self, alguien):
        if self.abierta:
            self.lado2.entrar()
        else:
            print("La puerta está cerrada")
    def imprimir(self):
        print("Puerta")

class Orientacion:
    def __init__(self):
        pass
    def caminarAleatoriamente(self, alguien):
        pass
    def establecerEMinOr(self, em, unContenedor):
        pass

class Norte(Orientacion):
    _instancia = None
    def __init__(self):
        if not Norte._instancia:
            super().__init__()
            Norte._instancia = self
    def establecerEMinOr(self, em, unContenedor):
        unContenedor.norte = em

    @classmethod
    def obtener_instancia(cls):
        if not cls._instancia:
            cls._instancia = Norte()
        return cls._instancia

    def imprimir(self):
        print("Norte")
    
    def caminarAleatoriamente(self, alguien):
        alguien.irNorte()


class Sur(Orientacion):
    _instancia = None
    def __init__(self):
        if not Sur._instancia:
            super().__init__()  
            Sur._instancia = self

    @staticmethod 
    def obtener_instancia():
        if not Sur._instancia:
            Sur()
        return Sur._instancia
    
    def imprimir(self):
        print("Sur")
    
    def caminarAleatoriamente(self, alguien):
        alguien.irSur()
    
    def establecerEMinOr(self, em, unContenedor):
        unContenedor.sur = em

class Este(Orientacion):
    _instancia = None
    def __init__(self):
        raise RuntimeError('Llamar a instancia() en lugar de esto')


    @classmethod
    def obtener_instancia(cls):
        if cls._instancia is None:
            print('Creando nueva instancia')
            cls._instancia = cls.__new__(cls)
        return cls._instancia
    
    def caminarAleatoriamente(self, alguien):
        alguien.irEste()
    
    def establecerEMinOr(self, em, unContenedor):
        unContenedor.este = em

        
class Oeste(Orientacion):
    _instancia = None
    def __init__(self):
        if not Oeste._instancia:
            super().__init__()
            Oeste._instancia = self

    @staticmethod
    def obtener_instancia():
        if not Oeste._instancia:
            Oeste()
        return Oeste._instancia
    
    def imprimir(self):
        print("Oeste")
    
    def caminarAleatoriamente(self, alguien):
        alguien.irOeste()

    def establecerEMinOr(self, em, unContenedor):
       unContenedor.oeste = em