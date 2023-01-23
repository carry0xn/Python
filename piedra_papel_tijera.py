
import random 

def jugar():
    jugador = input("¿Que vas a ejegir? P para piedra, A para papel, T para tijera\n")
    computadora = random.choice(['p', 'a', 't'])

    if es_Empate(jugador, computadora):
        return 'Es un Empate'
    
    if usuario_es_Ganador(jugador, computadora):
        return '¡Ganaste!'

    return 'Perdiste :('


def es_Empate(usuario, oponente):
    if usuario == oponente:
        return True
        

def usuario_es_Ganador(usuario, oponente):
    if (usuario == 'p' and oponente == 't') or (usuario == 't' and oponente == 'a') or (usuario == 'a' and oponente == 'p'):
        return True