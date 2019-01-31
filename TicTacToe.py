#!/usr/bin/python3
import sys
import tkinter
import tkinter.font


class Game:
    def __init__(self):
        self.player = "X"
        self.opponent = "O"

        self.board = []
        for i in range(3):
            self.board.append(["", "", ""])
        return

    def update_board(self, x, y, symbol):
        self.board[x][y] = symbol
        self.check_win()
        return

    def check_win(self):
        for row in self.board:
            string_row = row[0] + row[1] + row[2]
            if string_row == "XXX":
                print("X wins")
            elif string_row == "OOO":
                print("O wins")

        for col in range(3):
            string_col = ""
            for row in self.board:
                string_col += row[col]
            if string_col == "XXX":
                print("X wins")
            elif string_col == "OOO":
                print("O wins")

        for i in range(2):
            string_board = ""
            for j in range(3):
                string_board += self.board[j][abs((2 * i) - j)]
            if string_board == "XXX":
                print("X wins")
            elif string_board == "OOO":
                print("O wins")

        return


class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Leo Tic-Tac-Toe")
        self.window.resizable(width=False, height=False)
        self.game = Game()

        self.buttons = None
        self.add_buttons()

        self.turn = "X"
        return

    def add_buttons(self):
        button_width = "2"
        button_height = "1"
        button_font = tkinter.font.Font(family="Helvetica", size=72)

        self.buttons = []
        for x in range(3):
            but = []
            for y in range(3):
                button = tkinter.Button(master=self.window,
                                        width=button_width,
                                        height=button_height,
                                        text="",
                                        font=button_font,
                                        command=lambda n_x=x, n_y=y: self.button_click_event(n_x, n_y))
                button.grid(row=x, column=y)
                but.append(button)
            self.buttons.append(but)

        return

    def button_click_event(self, x, y):
        self.buttons[x][y].config(text=self.turn, state='disabled', disabledforeground='black')
        self.game.update_board(x, y, self.turn)
        self.turn = self.swap_turn(self.turn)
        return

    def mainloop(self):
        self.window.mainloop()
        return

    @staticmethod
    def swap_turn(turn):
        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X"
        else:
            sys.exit("Error: Turn \"" + turn + "\" not valid")
        return turn


def main():
    GUI().mainloop()
    return


if __name__ == "__main__":
    main()
    sys.exit(0)
