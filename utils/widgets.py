import tkinter as tk
import time
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path

from utils.general_functions import getImagePath
from utils.button_functions import *
from game_dictionaries import tamagachi_avatars, background_images


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
        """
        Purpose of this class is to create an image label widget
        """
        def __init__(self, parent, **kwargs):
            """ 
            Initialize ImageWidget with given kwargs parameters
            image_name: file name of image
            image_size: image size
            """

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

        #get the keys and values from the initialization of the canvas widget. Usually pet_name, size, and background image name and size
        for key, value in kwargs.items():
            setattr(self, key, value)
        

        self.canvas = tk.Canvas(self, width=self.bg_image_size[0], height=self.bg_image_size[1])        #initialize canvas
        self.pet_photo = PhotoObject(self.pet_image_name, self.pet_image_size).photo_object             #initialize pet image
        self.bg_photo = PhotoObject(self.bg_image_name, self.bg_image_size).photo_object                #initialize background image

        self.canvas.bg_image=self.bg_photo
        self.canvas.pet_image=self.pet_photo

        self.bg = self.canvas.create_image(150, 150, image=self.canvas.bg_image)
        self.pet = self.canvas.create_image(150, 200, image=self.canvas.pet_image)     #create pet image on canvas

    def update_canvas(self, **kwargs):
        """
        update pet and background images dynamically

        **kwargs
        new_pet_image = pet_image
        new_bg_image = bg_image
        """

        if kwargs.get("new_pet_image"):
            self.pet_photo = PhotoObject(kwargs["new_pet_image"], self.pet_image_size).photo_object
            self.canvas.itemconfig(self.pet, image=self.pet_photo)
            self.canvas.pet_image = self.pet_photo  

        if kwargs.get("new_bg_image"):
            self.bg_photo = PhotoObject(kwargs["new_bg_image"], self.bg_image_size).photo_object
            self.canvas.itemconfig(self.bg, image=self.bg_photo)
            self.canvas.bg_image = self.bg_photo  


class PetEntryWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        #create pet name label and entry 
        self.Pet_name_label = ttk.Label(self, text=("Pet Name: "))
        self.Pet_name_entry = ttk.Entry(self)


        #create pet gender label and button
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
        
        #create pet avatar choice label and combobox
        self.Pet_avatar_label = ttk.Label(self, text=("Avatar: "))
        self.avatar_choice = tk.StringVar()
        self.Pet_avatar_choice = ttk.Combobox(self, textvariable=self.avatar_choice)
        petAvatarChoices = list(tamagachi_avatars.keys())
        self.Pet_avatar_choice['values'] = petAvatarChoices
        self.Pet_avatar_choice.set(petAvatarChoices[0])
        self.Pet_avatar_choice.bind("<<ComboboxSelected>>", self.update_game_world)

        #create background choice label and combobox
        self.Game_background_label = ttk.Label(self, text=("Background: "))
        self.background_choice = tk.StringVar()
        self.Game_background_choice = ttk.Combobox(self, textvariable=self.background_choice)
        gameBgChoices = list(background_images.keys())
        self.Game_background_choice['values'] = gameBgChoices
        self.Game_background_choice.set(gameBgChoices[0])
        self.Game_background_choice.bind("<<ComboboxSelected>>", self.update_game_world)
    
    def update_game_world(self, event=None):
        """
        Update the game world canvas when selections change
        """

        pet_image = tamagachi_avatars[self.avatar_choice.get()]["default"]
        bg_image = background_images[self.background_choice.get()]

        game_frame = self.parent.controller.frames["NewGameSetupFrame"]
        game_frame.game_world_widget.update_canvas(new_pet_image = pet_image, new_bg_image = bg_image)
        
        


class TamagachiInfoWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


        self.Tamagachi_name_label = ttk.Label(self)
        self.Tamagachi_gender_label = ttk.Label(self)
        self.Tamagachi_happiness_label = ttk.Label(self)
        self.Tamagachi_time_label = ttk.Label(self)

        self.update_info()

    def update_info(self):
        """Refresh the displayed pet info"""

        self.Tamagachi_name_label.config(text=f"Name: {self.parent.controller.Tamagachi.name}")
        self.Tamagachi_gender_label.config(text=f"Gender: {self.parent.controller.Tamagachi.gender}")
        self.Tamagachi_happiness_label.config(text=f"Happiness: {self.parent.controller.Tamagachi.happiness}")
        self.Tamagachi_time_label.config(text=f"Time Alive: {self.parent.controller.Tamagachi.print_alive_time()}")

class StartButtonWidget(ttk.Frame):
    def __init__(self, parent, PetInfo):
        super().__init__(parent)
        self.parent = parent
        self.PetInfo = PetInfo
        self.Start_button = ttk.Button(self, text="Start", command=self.start_game)
        
    def start_game(self):

        #get pet name
        self.parent.controller.Tamagachi.set_name(self.PetInfo.Pet_name_entry.get())

        #get pet birth time
        self.parent.controller.Tamagachi.birth_time = time.time()
        self.parent.controller.Tamagachi.update_alive_time()

        #Pass selected pet avatar and background to GameWorldFrame
        pet_image = tamagachi_avatars[self.PetInfo.avatar_choice.get()]["default"]
        bg_image = background_images[self.PetInfo.background_choice.get()]

        game_frame = self.parent.controller.frames["GameWorldFrame"]

        # Update the GameWorldFrame to reflect changes
        game_frame.game_world_widget.update_canvas(new_pet_image = pet_image,new_bg_image = bg_image)
        game_frame.tamagachi_info_widget.update_info()

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
        elif interaction == "Hug":
            interaction_msg = self.parent.controller.Tamagachi.hug()
        elif interaction == "Scold":
            interaction_msg = self.parent.controller.Tamagachi.scold()
        elif interaction == "Check Status":
            interaction_msg = self.parent.controller.Tamagachi.check_status()
        else:
            interaction_msg = "invalid command"

        self.parent.controller.frames["GameWorldFrame"].tamagachi_info_widget.update_info()

        self.game_message.config(text=interaction_msg)
        self.after(10000, lambda: self.game_message.config(text="")) #clear message after 3 seconds

class BackButtonWidget(ttk.Frame):
    def __init__(self, parent, prev_frame):
        super().__init__(parent)
        self.parent = parent

        self.Back_button = ttk.Button(
            self, 
            text="Back", 
            command=lambda: parent.controller.show_frame(prev_frame)
            )
        
class SaveGameButtonWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.Save_button = ttk.Button(
            self,
            text="Save Game",
            command=parent.controller.save_game)
        
class QuitGameButtonWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.Quit_button = ttk.Button(
            self,
            text="Quit",
            command=parent.controller.quit_game)
        
