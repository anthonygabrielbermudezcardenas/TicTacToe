import os


class Board:
    # Representa el tablero del juego
    def __init__(self):
        self.board = [i for i in range(10)]
        self.win_combinations = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 5, 9),
            (3, 5, 7),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),
        ]
        self.game_over = False

    def draw_board(self):
        # Dinuja el tablero en el terminal
        print('=========')
        print(self.board[7], '|', self.board[8], '|', self.board[9])
        print(self.board[4], '|', self.board[5], '|', self.board[6])
        print(self.board[1], '|', self.board[2], '|', self.board[3])
        print('=========')

    def check_if_won(self, player):
        # Comprueba si el movimiento del jugador se ha hecho, y le hace ganar
        for a, b, c in self.win_combinations:
            if self.board[a] == self.board[b] == self.board[c]:
                print(f"Se acabo el juego, jugador {player} gana la partida")
                self.game_over = True

    def update(self, input, choice):
        # Actualiza el tablero actual
        self.board[input] = choice
        self.draw_board()
        self.check_if_won(choice)

    def reset_board(self):
        # Resetea el trablero
        self.board = [i for i in range(10)]

    def draw(self):
        # Para el juego si se empata
        list = [x for x in self.board if type(x) != int]
        return len(list) == 9