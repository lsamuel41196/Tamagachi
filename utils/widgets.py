import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path

from utils.functions import start_game, getImagePath

class PhotoObject():
    def __init__(self, image_name):
        
        self.image_path = getImagePath(image_name)
        self.image_object = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image_object)

class ImageWidget(ttk.Frame):
        def __init__(self, parent, image_name):
            super().__init__(parent)

            self.photo = PhotoObject(image_name).photo
            self.image_label = ttk.Label(self, image=self.photo)

'''
female icon link: https://img.icons8.com/?size=100&id=1816&format=png&color=000000
male icon link: https://img.icons8.com/?size=100&id=1814&format=png&color=000000```
'''

class PetInfoWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.Pet_name_label = ttk.Label(self, text="Pet Name:")
        self.Pet_name_entry = ttk.Entry(self)
        self.Pet_gender_label = ttk.Label(self, text="Gender:")
        self.Pet_gender_male_button = ttk.Button(self, image=PhotoObject("icons8-male-50.png").photo, command=start_game)
        self.Pet_gender_female_button = ttk.Button(self, image=PhotoObject("icons8-female-50.png").photo, command=start_game)


class StartButtonWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.Start_button = ttk.Button(self, text="Start", command=start_game)

class BackButtonWidget(ttk.Frame):
    def __init__(self, parent, prev_frame):
        super().__init__(parent)
        self.Back_button = ttk.Button(
            self, 
            text="Back", 
            command=lambda: parent.controller.show_frame(prev_frame)
            )
        
class QuitGameButtonWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.Quit_button = ttk.Button(
            self,
            text="Quit",
            command=parent.controller.quit_game)