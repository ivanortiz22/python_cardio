


def juego(jugador1,jugador2):

    if jugador1 == 'piedra' and jugador2 == 'papel':
        print(" gana el jugador 2")
    elif jugador1 == 'piedra' and jugador2 == 'tijera':
        print("gana el jugador 1")
    elif jugador1 == 'papel' and jugador2 == 'piedra':
        print("gana el jugador 1")
    elif jugador1 == 'papel' and jugador2 == 'tijera':
        print("gana el jugador 2")
    elif jugador1 == 'tijera' and jugador2 == 'papel':
        print("gana el jugador 1")
    elif jugador1 == 'tijera' and jugador2 == 'piedra':
        print("gana el jugador 2")
    elif jugador1 == jugador2 :
        print("es un empate")





def run (): 
    jugador1=str(input(" jugador 1 escoge : piedra - papel - tijera: "))
    jugador2=str(input("jugador 2 escoge : piedra - papel - tijera: "))
    juego(jugador1,jugador2)
    
    
    


if __name__ == '__main__':
    run() 
