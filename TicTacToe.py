#!/usr/bin/python3
import sys
import tkinter
import tkinter.font


class Game:
    def __init__(self):
        self.player = "X"
        self.opponent = "O"
        return


class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Leo Tic-Tac-Toe")
        self.window.resizable(width=False, height=False)
        self.game = Game()

        self.button_width = None
        self.button_height = None
        self.button_font = None
        self.buttons = None
        self.add_buttons()

        return

    def add_buttons(self):
        self.button_width = "2"
        self.button_height = "1"
        self.button_font = tkinter.font.Font(family="Helvetica", size=72)

        self.buttons = []
        for x in range(3):
            but = []
            for y in range(3):
                button = tkinter.Button(master=self.window,
                                        width=self.button_width,
                                        height=self.button_height,
                                        text="",
                                        font=self.button_font,
                                        command=lambda n_x=x, n_y=y: self.button_click_event(n_x, n_y))
                button.grid(row=x, column=y)
                but.append(button)
            self.buttons.append(but)

        return

    def button_click_event(self, x, y):
        self.buttons[x][y].config(text="H", state='disabled', disabledforeground='black')
        return

    def mainloop(self):
        self.window.mainloop()
        return


def main():
    GUI().mainloop()
    return


if __name__ == "__main__":
    main()
    sys.exit(0)
