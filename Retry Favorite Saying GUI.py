# Author: Lucia Floan
# Date Written: 04/11/2025
# Program Title: Favorite Saying GUI

import tkinter

class FavoriteSayingGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Favorite Saying")
        self.label = tkinter.Label(self.main_window,
                                   text="You miss 100% of the shots you don’t take. – Wayne Gretzky")
        self.label.pack()
        self.main_window.mainloop()
if __name__ == '__main__':
    gui = FavoriteSayingGUI()