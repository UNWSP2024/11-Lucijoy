# Author: Lucia Floan
# Date Written: 04/11/2025
# Program Title: Show Info GUI

import tkinter

class ShowInfoGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Show Info")
        self.address_lable = tkinter.Label(self.main_window, text="")
        self.address_label.pack()

        self.address_button = tkinter.Button(self.main_window, text="Show Info", command=self.show_info)
        self.address_button.pack()

        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.quit)
        self.quit_button.pack()

        tkinter.mainloop()

    def show_info(self):
        self.address_label.config(text="Lucia Floan\n15254 Bird Street\nCoon Rapids, MN 55303")

if __name__ == "__main__":
    show_info = ShowInfoGUI()