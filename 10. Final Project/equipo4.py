#----------------------------------------------------------
# Project: Knight’s Dance
#
# Date: 29-Nov-2023
# Authors:
#           A01747869 Gustavo Gutiérrez
#           A01777771 Ericxzin Navarro
#----------------------------------------------------------

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
        if maxPlayer: 
            for nextPos in self.posiciones_siguientes(posicion):
                resultado: float = self.MinimaxAlphaBeta(nextPos,profundidad-1,False,alfa,beta)
                alfa = max(alfa,resultado)
                if beta <= alfa:
                    break
            return alfa
        else: 
            for nextPos in self.posiciones_siguientes(posicion):
                resultado = self.MinimaxAlphaBeta(nextPos,profundidad-1,True,alfa,beta)
                beta = min(beta,resultado)
                if beta <= alfa:
                    break
            return beta
        
        
if __name__ == '__main__':
    jugador1 = JugadorCaballosBailadoresEquipo4('Erickxzin')
    jugador2 = JugadorCaballosBailadoresAleatorio('Player 2')
    juego = JuegoCaballosBailadores(jugador1,jugador2,5,8)
    juego.inicia(veces=100,delta_max=2)
    
