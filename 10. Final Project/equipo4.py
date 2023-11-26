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

class JugadorCaballosBailadoresEquipo4(JugadorCaballosBailadores):
   
    def heuristica(self, posicion):
        return self.triunfo(posicion) == self.simbolo
    
    def tira(self, posicion):
        best_eval  = -math.inf
        best_pos = posicion
        for movimiento in self.posiciones_siguientes(posicion):
            resultado = self.MinimaxAlphaBeta(movimiento,3,True)
            if resultado > best_eval:
                best_eval = resultado
                best_pos = movimiento
        return best_pos
        
    def evaluate(self,posicion) -> float:
        if self.triunfo(posicion) == self.simbolo:
            return 1
        else:
            return -1
        
    def MinimaxAlphaBeta(self,posicion,profundidad : int, maxPlayer: bool, alfa: float = -math.inf, beta: float = math.inf) -> float:
        if self.triunfo != None or profundidad == 0:
            return self.evaluate(posicion)
        if maxPlayer: #Turno del MaxPlayer
            for nextPos in self.posiciones_siguientes(posicion):
                resultado: float = self.MinimaxAlphaBeta(nextPos,profundidad-1,False,alfa,beta)
                alfa = max(alfa,resultado)
                if beta <= alfa:
                    break
            return alfa
        else: #Turno del MinPlayer
            for nextPos in self.posiciones_siguientes(posicion):
                resultado = self.MinimaxAlphaBeta(nextPos,profundidad-1,True,alfa,beta)
                beta = min(beta,resultado)
                if beta <= alfa:
                    break
            return beta
        
        
if __name__ == '__main__':
    jugador1 = JugadorCaballosBailadoresEquipo4('Erickxzin')
    jugador2 = JugadorCaballosBailadoresAleatorio('Player 2')
    juego = JuegoCaballosBailadores(jugador1,jugador2,10,10)
    juego.inicia(veces=100,delta_max=2)
    
