import tkinter.filedialog
import tkinter as tk
import json
from frame_classes import *
from pathlib import Path
from Tamagachi_Class import Tamagachi
from utils.general_functions import show_popup


class App(tk.Tk):
    def __init__(self, *args, **kwargs): 

        # main setup
        super().__init__()

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="true")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.Tamagachi = Tamagachi()

        self.frames = {}

        for F in (StartFrame, NewGameSetupFrame, LoadGameSetupFrame, GameWorldFrame, GameAnimationFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartFrame")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        

    def quit_game(self):
        self.destroy()
 



if __name__ == "__main__":
    app = App()
    app.title("Tamagachi")
    app.mainloop()

