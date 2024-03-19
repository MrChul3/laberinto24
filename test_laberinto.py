import unittest
from laberinto import Juego, JuegoBomba, ParedBomba

class TestJuego(unittest.TestCase):
    
    def test_crearHabitacion_returns_habitacion_con_paredes(self):
        juego = Juego()
        habitacion = juego.crearHabitacion(1)
        self.assertIsNotNone(habitacion.norte)
        self.assertIsNotNone(habitacion.sur)
        self.assertIsNotNone(habitacion.este)
        self.assertIsNotNone(habitacion.oeste)

    def test_crearHabitacion_returns_habitacion_con_id_correcto(self):
        juego = Juego()
        habitacion = juego.crearHabitacion(5)
        self.assertEqual(habitacion.id, 5)
        
    def test_crearHabitacion_returns_habitacion_con_paredes_bomba(self):
        juego = JuegoBomba()
        hab = juego.crearHabitacion(1)
        self.assertIsInstance(hab.norte, ParedBomba)
        self.assertIsInstance(hab.sur, ParedBomba)
        self.assertIsInstance(hab.este, ParedBomba)
        self.assertIsInstance(hab.oeste, ParedBomba)

class TestJuegoAdditional(unittest.TestCase):

    def test_crearHabitacion_norte_sur_same(self):
        juego = Juego()
        habitacion = juego.crearHabitacion(1)
        self.assertIsNot(habitacion.norte, habitacion.sur)

    def test_crearHabitacion_norte_este_same(self):
        juego = Juego()
        habitacion = juego.crearHabitacion(1)
        self.assertIsNot(habitacion.norte, habitacion.este)

    def test_crearHabitacion_norte_oeste_same(self):
        juego = Juego()
        habitacion = juego.crearHabitacion(1)
        self.assertIsNot(habitacion.norte, habitacion.oeste)

    def test_crearHabitacion_sur_este_same(self):
        juego = Juego()
        habitacion = juego.crearHabitacion(1)
        self.assertIsNot(habitacion.sur, habitacion.este)

    def test_crearHabitacion_sur_oeste_same(self):
        juego = Juego()
        habitacion = juego.crearHabitacion(1)
        self.assertIsNot(habitacion.sur, habitacion.oeste)

    def test_crearHabitacion_este_oeste_same(self):
        juego = Juego()
        habitacion = juego.crearHabitacion(1)
        self.assertIsNot(habitacion.este, habitacion.oeste)


    
