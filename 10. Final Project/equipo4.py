#----------------------------------------------------------
# Project: Knight’s Dance
#
# Date: 29-Nov-2023
# Authors:
#           A01770771 Gustavo Gutiérrez
#           A01777771 Ericxzin Navarro
#----------------------------------------------------------


'''Toda clase que represente un jugador del juego de Caballos
bailadores debe heredar de esta clase.

La posición que maneja un juego de Caballos bailadores es
una tupla de la siguiente forma:

    (T, #R, #C, rB, rN, cB, cN)

En donde:

    T:  turno actual (símbolo del jugador asignado por la clase
        de JuegoCaballosBailadores: B y N [blanco y negro])
    #R: Número de renglones (fijo durante todo el juego)
    #C: Número de columnas (fijo durante todo el juego)
    rB: Tupla (r, c) con la coordenada del rey blanco (fija
        durante todo el juego)
    rN: Tupla (r, c) con la coordenada del rey negro (fija
        durante todo el juego)
    cB: Tupla (r, c) con la coordenada del caballo blanco
    cN: Tupla (r, c) con la coordenada del caballo negro

Por ejemplo:

    ('B', 5, 6, (4, 0), (4, 1), (0, 5), (0, 1))

Esta posición indica que el jugador actual es 'B' y que
el tablero en este momento es:

    0    1    2    3    4    5
0     | cN |    |    |    | cB
    ----+----+----+----+----+----
1     |    |    |    |    |
    ----+----+----+----+----+----
2     |    |    |    |    |
    ----+----+----+----+----+----
3     |    |    |    |    |
    ----+----+----+----+----+----
4  rB | rN |    |    |    |
'''

from dagor import JuegoCaballosBailadores, JugadorCaballosBailadores, JugadorCaballosBailadoresAleatorio
import math

class JugadorCaballosBailadoresEquipo7(JugadorCaballosBailadores):
    #Debe regresar true si el siguiente tiro es un tiro ganador, en caso contrario regresará
    def heuristica(self, posicion):
        
        return self.evaluate(self.Minimax(posicion,3,-math.inf,math.inf))
    
    def tira(self, posicion):
        alternativas = self.posiciones_siguientes(posicion)
        for pos in alternativas:
            if self.heuristica(pos):
                return pos
            return alternativas[0]
        
    def evaluate(self,posicion):
        if self.triunfo(posicion) == self.simbolo:
            return 1
        elif self.triunfo(posicion) != None and self.triunfo(posicion) != self.simbolo:
            return -1
        
    def Minimax(self,posicion,profundidad,alfa,beta):
        if self.triunfo(posicion) != None or profundidad == 0:
            return self.evaluate(posicion)
        if posicion[0] == self._simbolo: #Turno del MaxPlayer
            maxValue = -math.inf
            for nextPos in self.posiciones_siguientes(posicion):
                value = self.Minimax(nextPos,profundidad-1,alfa,beta)
                maxValue = max(maxValue,value)
                alfa = max(alfa,value)
                if beta <= alfa:
                    break
            return maxValue
        if posicion[0] != self._contrario: #Turno del MinPlayer
            minValue = math.inf
            for nextPos in self.posiciones_siguientes(posicion):
                value = self.Minimax(nextPos,profundidad-1,alfa,beta)
                minValue = min(minValue,value)
                beta = min(beta,value)
                if beta <= alfa:
                    break
            return minValue
        
        
        
if __name__ == '__main__':
    jugador1 = JugadorCaballosBailadoresEquipo7('Player 1')
    jugador2 = JugadorCaballosBailadoresAleatorio('Player 2')
    juego = JuegoCaballosBailadores(jugador1,jugador2,10,10)
    juego.inicia(veces=100,delta_max=2)
    
