#----------------------------------------------------------
# Project: Knight’s Dance
#
# Date: 29-Nov-2023
# Authors:
#           A01770771 Gustavo Gutiérrez
#           A01777771 Ericxzin Navarro
#----------------------------------------------------------

from dagor import JuegoCaballosBailadores, JugadorCaballosBailadores, JugadorCaballosBailadoresAleatorio

class JugadorCaballosBailadoresEquipo7(JugadorCaballosBailadores):
    def heuristica(self, posicion):
        return 0
    
    def tira(self, posicion):
        posibles = self.posiciones_siguientes(posicion)
        for p in posibles:
            if self.heuristica(p):
                return p
            return posibles[0]
