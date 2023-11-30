#----------------------------------------------------------
# Project: Knight’s Dance
#
# Date: 29-Nov-2023
# Authors:
#           A01747869 Gustavo Gutiérrez
#           A01746219 Ericx Navarro
#----------------------------------------------------------

from dagor import JuegoCaballosBailadores, JugadorCaballosBailadores, JugadorCaballosBailadoresAleatorio
import math

class JugadorCaballosBailadoresEquipo4(JugadorCaballosBailadores):
   
    def heuristica(self, posicion):
        best_eval  = -math.inf
        best_pos = posicion
        for movimiento in self.posiciones_siguientes(posicion):
            resultado = self.MinimaxAlphaBeta(movimiento,4,False)
            if resultado > best_eval:
                best_eval = resultado
                best_pos = movimiento
        return best_pos
        
    
    def tira(self, posicion):
        return self.heuristica(posicion)
        
    def evaluate(self,posicion) -> float:
        if self.triunfo(posicion) == self.simbolo:
            return 1
        elif self.triunfo(posicion) == self.contrario.simbolo:
            return -1
        else:
            return 0
        
    def MinimaxAlphaBeta(self,posicion,profundidad : int, maxPlayer: bool, alfa: float = -math.inf, beta: float = math.inf) -> float:
        if self.triunfo(posicion) or profundidad == 0:
            return self.evaluate(posicion)
        if maxPlayer: 
            maxRes = -math.inf
            for nexMov in self.posiciones_siguientes(posicion):
                resultado: float = self.MinimaxAlphaBeta(nexMov,profundidad-1,False,alfa,beta)
                alfa = max(alfa,resultado)
                if beta <= alfa:
                    break
            return alfa
        else: 
            minRes = math.inf
            for nexMov in self.posiciones_siguientes(posicion):
                resultado = self.MinimaxAlphaBeta(nexMov,profundidad-1,True,alfa,beta)
                beta = min(beta,resultado)
                if beta <= alfa:
                    break
            return beta
        
        
if __name__ == '__main__':
    jugador1 = JugadorCaballosBailadoresEquipo4('Equipo 4')
    jugador2 = JugadorCaballosBailadoresAleatorio('Player 2')
    juego = JuegoCaballosBailadores(jugador1,jugador2, 8,8)
    juego.inicia(veces=1000,delta_max=2)
    
