from dagor import JuegoD10, JugadorD10Interactivo,JugadorD10Estrategico

if __name__ == '__main__':
    jugador1 = JugadorD10Estrategico('Maquina Lista')
    jugador2 = JugadorD10Estrategico('Maquina Tonta')
    juego = JuegoD10(jugador1,jugador2)
    juego.inicia(veces=1000)

