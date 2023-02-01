import random 

def jugar():
    jugador = input("¿Que vas a ejegir? P para piedra, A para papel, T para tijera\n")
    computadora = random.choice(['p', 'a', 't'])

    elegido_oponente = None    
    if computadora == 'p':        
        elegido_oponente = 'p'   
    elif computadora == 'a':
        elegido_oponente = 'a'   
    else:        
        elegido_oponente = 't' 

    if es_Empate(jugador, computadora):
        return 'computadora eligio: ' + elegido_oponente + ' Es un Empate'
    
    if usuario_es_Ganador(jugador, computadora):
        return 'computadora eligio: ' + elegido_oponente +' ¡Ganaste!'

    return 'computadora eligio: ' + elegido_oponente +' Perdiste :('


def es_Empate(usuario, oponente):
    if usuario == oponente:
        return True
        

def usuario_es_Ganador(usuario, oponente):
    if (usuario == 'p' and oponente == 't') or (usuario == 't' and oponente == 'a') or (usuario == 'a' and oponente == 'p'):
        return True
    
print(jugar())