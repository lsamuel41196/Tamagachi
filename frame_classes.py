import tkinter as tk
from tkinter import ttk
from pathlib import Path
from utils.general_functions import getImagePath
from utils.button_functions import start_game, load_game


from utils.widgets import *


class StartFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.game_world_widget = CanvasWidget(self, 
                                              pet_image_name=controller.Tamagachi.image_name, 
                                              pet_image_size=controller.Tamagachi.image_size,
                                              bg_image_name="front_lawn.jpg",
                                              bg_image_size=(300,300)
                                              )
        self.game_world_widget.canvas.grid(row=0, column=0)
        self.game_world_widget.grid()

        NewGameButton = ttk.Button(
            self, 
            text="New Game", 
            command=lambda: controller.show_frame("NewGameSetupFrame")
            )
        NewGameButton.grid(row=1, column=0)

        
        LoadGameButton = ttk.Button(
            self, 
            text="Load Game", 
            command=lambda:[controller.show_frame("LoadGameSetupFrame"), load_game()]
            )
        LoadGameButton.grid(row=2, column=0)

        
        self.quitbuttonwidget = QuitGameButtonWidget(self)
        self.quitbuttonwidget.Quit_button.grid(row=3, column=0)
        self.quitbuttonwidget.grid()

class NewGameSetupFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # # image widget
        # self.cat_image_widget = ImageWidget(self, image_name="orange_cat2.png", image_size=(300, 300))
        # self.cat_image_widget.image_label.grid(row=0, column=0)
        # self.cat_image_widget.grid()

        self.game_world_widget = CanvasWidget(self, 
                                              pet_image_name=controller.Tamagachi.image_name, 
                                              pet_image_size=controller.Tamagachi.image_size,
                                              bg_image_name="front_lawn.jpg",
                                              bg_image_size=(300,300)
                                              )
        self.game_world_widget.canvas.grid(row=0, column=0)
        self.game_world_widget.grid()

        #Pet info widget
        self.petinfo_widget = PetEntryWidget(self)
        self.petinfo_widget.Pet_name_label.grid(row=1, column=0)
        self.petinfo_widget.Pet_name_entry.grid(row=1, column=1)
        self.petinfo_widget.Pet_gender_label.grid(row=2, column=0)
        self.petinfo_widget.Pet_gender_male_button.grid(row=2, column=1)
        self.petinfo_widget.Pet_gender_female_button.grid(row=2, column=2)
        self.petinfo_widget.grid()


        #start button
        self.startbuttonwidget = StartButtonWidget(self, self.petinfo_widget)
        self.startbuttonwidget.Start_button.grid(row=3, column=0)
        self.startbuttonwidget.grid()

        #back button
        self.backbuttonwidget = BackButtonWidget(self, prev_frame="StartFrame")
        self.backbuttonwidget.Back_button.grid(row=4, column=0)
        self.backbuttonwidget.grid()

class LoadGameSetupFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #TODO: Complete this frame

        #back button
        self.backbuttonwidget = BackButtonWidget(self, prev_frame="StartFrame")

        self.backbuttonwidget.Back_button.grid(row=3, column=0)
        self.backbuttonwidget.grid()

        pass

class GameWorldFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.game_world_widget = CanvasWidget(self, 
                                              pet_image_name=controller.Tamagachi.image_name, 
                                              pet_image_size=controller.Tamagachi.image_size,
                                              bg_image_name="front_lawn.jpg",
                                              bg_image_size=(300,300)
                                              )
        self.game_world_widget.canvas.grid(row=0, column=0)
        self.game_world_widget.grid()

        self.tamagachi_info_widget = TamagachiInfoWidget(self)
        self.tamagachi_info_widget.Tamagachi_name_label.grid(row=1, column=0)
        self.tamagachi_info_widget.Tamagachi_gender_label.grid(row=2, column=0)
        self.tamagachi_info_widget.grid()

        self.backbuttonwidget = BackButtonWidget(self, prev_frame="NewGameSetupFrame")

        self.backbuttonwidget.Back_button.grid(row=3, column=0)
        self.backbuttonwidget.grid()


        pass
