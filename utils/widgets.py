import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path

from utils.general_functions import getImagePath
from utils.button_functions import start_game, set_gender


class PhotoObject():
    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.image_path = getImagePath(self.image_name)
        self.image_object = Image.open(self.image_path)

        if hasattr(self, "image_size"):     #resize image if image_size is provided
            self.image_object = self.image_object.resize(self.image_size)

        self.photo_object = ImageTk.PhotoImage(self.image_object)

class ImageWidget(ttk.Frame):
        def __init__(self, parent, **kwargs):
            super().__init__(parent)

            for key, value in kwargs.items():
                setattr(self, key, value)

            self.photo = PhotoObject(**kwargs).photo_object
            self.image_label = ttk.Label(self, image=self.photo)


class CanvasWidget(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.canvas = tk.Canvas(self, width=self.image_size[0], height=self.image_size[1], bg="white")
        self.photo = PhotoObject(**kwargs).photo_object
        self.canvas.create_image(0, 0, image=self.photo, anchor="nw")

class PetInfoWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.Pet_name_label = ttk.Label(self, text="Pet Name: " + parent.controller.Tamagachi.name)
        self.Pet_name_entry = ttk.Entry(self)
        self.Pet_gender_label = ttk.Label(self, text="Gender: " + parent.controller.Tamagachi.gender)

        # TODO: Add icons to the buttons
        
        self.Pet_gender_male_button = ttk.Button(self, text = "Male", 
                                                 image=PhotoObject(image_name="icons8-male-50.png").photo_object, 
                                                 command=lambda:[parent.controller.Tamagachi.set_gender("Male")]
                                                 )
        
        self.Pet_gender_female_button = ttk.Button(self, text = "Female", 
                                                   image=PhotoObject(image_name="icons8-female-50.png").photo_object, 
                                                   command=lambda:[parent.controller.Tamagachi.set_gender("Female")]
                                                   )
        


        
        '''
        female icon link: https://img.icons8.com/?size=100&id=1816&format=png&color=000000
        male icon link: https://img.icons8.com/?size=100&id=1814&format=png&color=000000```
        '''


class StartButtonWidget(ttk.Frame):
    def __init__(self, parent, PetInfo):
        super().__init__(parent)

        self.Start_button = ttk.Button(self, text="Start", 
                                        command=lambda: [
                                            parent.controller.show_frame("GameWorldFrame"),
                                            parent.controller.Tamagachi.set_name(PetInfo.Pet_name_entry.get()),
                                            start_game])

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