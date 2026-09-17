print('BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA')

# Solicitar los nombres de los jugadores
player_1_name = input('JUGADOR 1 INGRESA TU NOMBRE: ')
player_2_name = input('JUGADOR 2 INGRESA TU NOMBRE: ')

# Opciones válidas para jugar
valid_moves = ['piedra', 'papel', 'tijera']

# Pedir la elección de cada jugador
player_1_move = input(player_1_name + ' elige: piedra, papel o tijera: ')
player_2_move = input(player_2_name + ' elige: piedra, papel o tijera: ')

# Comparar las elecciones y determinar el ganador
if player_1_move == player_2_move:
    print('Empate!')
elif (player_1_move == 'piedra' and player_2_move == 'tijera') or \
     (player_1_move == 'papel' and player_2_move == 'piedra') or \
     (player_1_move == 'tijera' and player_2_move == 'papel'):
    print('Ganó', player_1_name)
else:
    print('Ganó', player_2_name)
