import tkinter as tk
import time
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path

from utils.general_functions import getImagePath
from utils.button_functions import *


class PhotoObject():
    def __init__(self, image_name, image_size):
        self.image_name = image_name
        self.image_size = image_size
        # for key, value in kwargs.items():
        #     setattr(self, key, value)

        self.image_path = getImagePath(self.image_name)
        self.image_object = Image.open(self.image_path)

        if hasattr(self, "image_size"):     #resize image if image_size is provided
            self.image_object = self.image_object.resize(self.image_size)

        self.photo_object = ImageTk.PhotoImage(self.image_object)

class ImageWidget(ttk.Frame):
        def __init__(self, parent, **kwargs):
            super().__init__(parent)
            self.parent = parent

            for key, value in kwargs.items():
                setattr(self, key, value)

            self.photo = PhotoObject(**kwargs).photo_object
            self.image_label = ttk.Label(self, image=self.photo)

class CanvasWidget(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self.parent = parent


        for key, value in kwargs.items():
            setattr(self, key, value)
        

        self.canvas = tk.Canvas(self, width=self.bg_image_size[0], height=self.bg_image_size[1])        #initialize canvas
        self.pet_photo = PhotoObject(self.pet_image_name, self.pet_image_size).photo_object             #initialize pet image
        self.bg_photo = PhotoObject(self.bg_image_name, self.bg_image_size).photo_object                #initialize background image

        self.canvas.bg_image=self.bg_photo
        self.canvas.pet_image=self.pet_photo

        self.canvas.create_image(0, 0, image=self.canvas.bg_image, anchor=tk.NW)
        self.pet = self.canvas.create_image(50, 150, image=self.canvas.pet_image, anchor=tk.CENTER)             #create pet image on canvas

class PetEntryWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


        self.Pet_name_label = ttk.Label(self, text=("Pet Name: "))
        self.Pet_name_entry = ttk.Entry(self)
        self.Pet_gender_label = ttk.Label(self, text=("Gender: "))

        # TODO: Add icons to the buttons, female button not working
        
        self.Pet_gender_male_button = ttk.Button(self, text = "Male", 
                                                 image=PhotoObject(image_name="icons8-male-50.png", image_size=(50,50)).photo_object, 
                                                 command=lambda:[parent.controller.Tamagachi.set_gender("Male")]
                                                 )
        
        self.Pet_gender_female_button = ttk.Button(self, text = "Female", 
                                                   image=PhotoObject(image_name="icons8-female-50.png", image_size=(50,50)).photo_object, 
                                                   command=lambda:[parent.controller.Tamagachi.set_gender("Female")]
                                                   )
        


        
        '''
        female icon link: https://img.icons8.com/?size=100&id=1816&format=png&color=000000
        male icon link: https://img.icons8.com/?size=100&id=1814&format=png&color=000000```
        '''

class TamagachiInfoWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


        self.Tamagachi_name_label = ttk.Label(self)
        self.Tamagachi_gender_label = ttk.Label(self)
        self.Tamagachi_happiness_label = ttk.Label(self)
        self.Tamagachi_time_label = ttk.Label(self, text = f"Play Time: {self.parent.controller.Tamagachi.print_play_time()}")

        self.update_info()

    def update_info(self):
        """Rfresh the displayed pet info"""

        self.Tamagachi_name_label.config(text=f"Name: {self.parent.controller.Tamagachi.name}")
        self.Tamagachi_gender_label.config(text=f"Gender: {self.parent.controller.Tamagachi.gender}")
        self.Tamagachi_happiness_label.config(text=f"Happiness: {self.parent.controller.Tamagachi.happiness}")

class StartButtonWidget(ttk.Frame):
    def __init__(self, parent, PetInfo):
        super().__init__(parent)
        self.parent = parent

        self.PetInfo = PetInfo

        self.Start_button = ttk.Button(self, text="Start", 
                                        command=self.start_game)
        
    def start_game(self):
        self.parent.controller.Tamagachi.set_name(self.PetInfo.Pet_name_entry.get())

        self.parent.controller.Tamagachi.start_time = time.time()
        print(self.parent.controller.Tamagachi.start_time)

        # Update the GameWorldFrame to reflect changes
        self.parent.controller.frames["GameWorldFrame"].tamagachi_info_widget.update_info()

        # Switch to the game world frame
        self.parent.controller.show_frame("GameWorldFrame")




class InteractionWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        choice = tk.StringVar()
        self.interaction_choice = ttk.Combobox(self, textvariable=choice)
        self.interaction_choice['values'] = parent.controller.Tamagachi.interactions

        self.interaction_button = ttk.Button(self, text="Interact", command=self.execute_interaction)

        self.game_message = ttk.Label(self)

    def execute_interaction(self):
        interaction = self.interaction_choice.get()
        if interaction == "Feed":
            interaction_msg = self.parent.controller.Tamagachi.feed()
            print("pet fed")
        elif interaction == "Hug":
            interaction_msg = self.parent.controller.Tamagachi.hug()
            print("pet hugged")
        elif interaction == "Check Status":
            interaction_msg = self.parent.controller.Tamagachi.check_status()
            print("pet check_status")
        else:
            interaction_msg = "invalid command"

        self.parent.controller.frames["GameWorldFrame"].tamagachi_info_widget.update_info()

        self.game_message.config(text=interaction_msg)
        self.after(10000, lambda: self.game_message.config(text="")) #clear message after 3 seconds
        print(interaction_msg)

class BackButtonWidget(ttk.Frame):
    def __init__(self, parent, prev_frame):
        super().__init__(parent)
        self.parent = parent

        self.Back_button = ttk.Button(
            self, 
            text="Back", 
            command=lambda: parent.controller.show_frame(prev_frame)
            )
        
class QuitGameButtonWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.Quit_button = ttk.Button(
            self,
            text="Quit",
            command=parent.controller.quit_game)