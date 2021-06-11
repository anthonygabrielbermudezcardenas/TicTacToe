import os
from class_board import Board


class Body:
    def __init__(self):
        self.board = Board()
        self.player_1_chooise = ""
        self.player_2_chooise = ""
        self.correct_chooise = False
        self.get_player_chooise()

    def reset(self):
        # Resetea el juego cuando un nuego juego empieza
        self.player_1_chooise = ''
        self.player_1_chooise = ''
        self.board.reset_board()

    def get_player_chooise(self):
        # Pregunta al jugador que simbolo quiere y lo verifica
        while True:
            print("BIENVENIDO A TICTACTOE!!!")
            player_1_chooise = input("Quieres jugar con X / O? ")
            print()
            if player_1_chooise == "X":
                self.player_1_chooise = "X"
                self.player_2_chooise = "O"
                print('Empezando jugando con X')
                break
            elif player_1_chooise == "O":
                self.player_1_chooise = "O"
                self.player_2_chooise = "X"
                print('Empezando jugando con O')
                break
            else:
                print('ERROR - la seleccion tiene que ser X / O!')

    def get_player_input(self, player_chooise):
        while True:
            while True:
                x = input(f"{player_chooise} Dónde quieres colocar tu simbolo?")
                if x.isdigit():
                    x = int(x)
                    break
                else:
                    print('ERROR: Tiene que ser un número, prueba de nuevo')

            if x > 0 and x < 10 and type(self.board.board[x]) != str:
                self.board.update(x, player_chooise)
                break
            else:
                print('Ese hueco ya ha sido seleccionado, prueba de nuevo:   ')

    def check_draw(self):
        if self.board.draw():
            self.board.game_over = True
            print("El juego esta empatado")
            return True
        return False

    def run(self):
        self.board.draw_board()

        while not self.board.game_over:
            self.correct_player1 = False
            self.correct_player2 = False

            self.get_player_input(self.player_1_chooise)
            if self.board.game_over:
                break
            if self.check_draw():
                break

            self.get_player_input(self.player_2_chooise)
            if self.board.game_over:
                break
            if self.check_draw():
                break
