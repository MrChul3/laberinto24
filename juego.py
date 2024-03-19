from laberinto import Laberinto, Habitacion, Puerta, Pared, ParedBombardera, Bomba, Norte, Este, Sur, Oeste
from bicho import Bicho, Modo, Agresivo, Perezoso
from threadManager import GestorHilos
import time

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []
        self.gestorHilos = GestorHilos()

    def iniciarHilos(self):
        for bicho in self.bichos:
            self.gestorHilos.agregarHilo(bicho)
        self.gestorHilos.iniciar()

    def detenerHilos(self):
        self.gestorHilos.detener()
        self.gestorHilos.unir()

    def crearPared(self):
        return Pared()
    
    def crearPuerta(self, habitacion1, habitacion2):
        puerta = Puerta(habitacion1, habitacion2)
        return puerta

    def crearHabitacion(self, id):
        habitacion = Habitacion(id)
        habitacion.agregarOrientacion(self.crearNorte())
        habitacion.agregarOrientacion(self.crearEste())
        habitacion.agregarOrientacion(self.crearSur())
        habitacion.agregarOrientacion(self.crearOeste())
        habitacion.norte = self.crearPared()
        habitacion.este = self.crearPared()
        habitacion.sur = self.crearPared()
        habitacion.oeste = self.crearPared()
        return habitacion

    def crearNorte(self):
        return Norte().obtener_instancia()

    def crearEste(self):
        return Este.obtener_instancia()
    
    def crearSur(self):
        return Sur().obtener_instancia()
    
    def crearOeste(self):
        return Oeste().obtener_instancia()

    def crearLaberinto2Habitaciones(self):
        laberinto = Laberinto()
        self.laberinto = laberinto
        habitacion1 = Habitacion(1)
        habitacion2 = Habitacion(2)

        puerta = Puerta(habitacion1, habitacion2)

        habitacion1.sur = puerta  
        habitacion2.norte = puerta

        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)

    def crear4Habitaciones4BichosFM(self):
        habitacion1 = self.crearHabitacion(1)
        habitacion2 = self.crearHabitacion(2)
        habitacion3 = self.crearHabitacion(3)
        habitacion4 = self.crearHabitacion(4)
        
        puerta12 = self.crearPuerta(habitacion1, habitacion2)
        puerta13 = self.crearPuerta(habitacion1, habitacion3)
        puerta24 = self.crearPuerta(habitacion2, habitacion4)
        puerta34 = self.crearPuerta(habitacion3, habitacion4)
        
        habitacion1.sur = puerta12
        habitacion2.norte = puerta12
        
        habitacion1.este = puerta13
        habitacion3.oeste = puerta13
        
        habitacion2.este = puerta24
        habitacion4.oeste = puerta24
        
        habitacion3.sur = puerta34
        habitacion4.norte = puerta34
        
        laberinto = Laberinto()
                
        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        laberinto.agregarHabitacion(habitacion3)
        laberinto.agregarHabitacion(habitacion4)
        self.laberinto = laberinto

        bicho1 = self.crearBichoAgresivo(habitacion1)
        bicho2 = self.crearBichoPerezoso(habitacion2)  
        bicho3 = self.crearBichoAgresivo(habitacion3)
        bicho4 = self.crearBichoPerezoso(habitacion4)
       
        self.agregarBicho(bicho1)
        self.agregarBicho(bicho2)
        self.agregarBicho(bicho3)
        self.agregarBicho(bicho4)

        return laberinto


    def crearLaberinto2HabitacionesFM(self):
        habitacion1 = self.crearHabitacion(1)
        habitacion2 = self.crearHabitacion(2)
        puerta = self.crearPuerta(habitacion1, habitacion2)
        laberinto = Laberinto()
        self.laberinto = laberinto
        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)
      
        habitacion1.sur = puerta 
        habitacion2.norte = puerta

        return laberinto
    
    def agregarBicho(self, bicho):
        bicho.num = len(self.bichos) + 1
        self.bichos.append(bicho)        

    def removerBicho(self, bicho):
        self.bichos.remove(bicho)
    
    def crearBichoAgresivo(self, habitacion):
        bicho = Bicho(Agresivo())
        bicho.poder = 5
        bicho.posicion = habitacion
        return bicho
    
    def crearBichoPerezoso(self, habitacion):
        bicho = Bicho(Perezoso())
        bicho.poder = 1
        bicho.posicion = habitacion
        return bicho
    
    def imprimir(self):
        print("Juego")

# BombedGame.py
class JuegoConBombas(Juego):
    def crearPared(self):
        return ParedBombardera()

    def imprimir(self):
        print("Juego con Bombas")
