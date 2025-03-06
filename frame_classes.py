import tkinter as tk
from tkinter import ttk
from pathlib import Path
from utils.general_functions import getImagePath
from utils.button_functions import load_game
from game_dictionaries import tamagachi_avatars, background_images
from utils.widgets import *



#TODO figure out why canvas widget is not working right
#TODO figure out why the game time and play time attributes aren't working right
#TODO Add logo to startframe



class StartFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.logo_image_widget = ImageWidget(self, image_name = "GameLogo.png", image_size = (300,300))
        self.logo_photo = self.logo_image_widget.photo
        self.logo_image_widget.image_label.grid(row=0, column=0)
        self.logo_image_widget.grid()


        # self.game_world_widget = CanvasWidget(self, 
        #                                       pet_image_name=tamagachi_avatars[controller.Tamagachi.avatar]["default"], 
        #                                       pet_image_size=controller.Tamagachi.image_size,
        #                                       bg_image_name=background_images["Front Lawn"],
        #                                       bg_image_size=(300,300)
        #                                       )
        # self.game_world_widget.canvas.grid(row=0, column=0)
        # self.game_world_widget.grid()

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

        self.game_world_widget = CanvasWidget(self, 
                                              pet_image_name=tamagachi_avatars[controller.Tamagachi.avatar]["default"], 
                                              pet_image_size=controller.Tamagachi.image_size,
                                              bg_image_name=background_images["Front Lawn"],
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
        self.petinfo_widget.Pet_avatar_label.grid(row=3, column=0)
        self.petinfo_widget.Pet_avatar_choice.grid(row=3, column=1)
        self.petinfo_widget.Game_background_label.grid(row=4, column=0)
        self.petinfo_widget.Game_background_choice.grid(row=4, column=1)
        self.petinfo_widget.grid()


        #start button
        self.startbuttonwidget = StartButtonWidget(self, self.petinfo_widget)
        self.startbuttonwidget.Start_button.grid(row=5, column=0)
        self.startbuttonwidget.grid()

        #back button
        self.backbuttonwidget = BackButtonWidget(self, prev_frame="StartFrame")
        self.backbuttonwidget.Back_button.grid(row=6, column=0)
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

        #TODO: Figure out why attributes are not updating

        #game world widget
        self.game_world_widget = CanvasWidget(self, 
                                              pet_image_name=tamagachi_avatars[controller.Tamagachi.avatar]["default"], 
                                              pet_image_size=controller.Tamagachi.image_size,
                                              bg_image_name=background_images["Front Lawn"],
                                              bg_image_size=(300,300)
                                              )
        self.game_world_widget.canvas.grid(row=0, column=0)
        self.game_world_widget.grid()

        #tamagachi info widget
        self.tamagachi_info_widget = TamagachiInfoWidget(self)
        self.tamagachi_info_widget.Tamagachi_name_label.grid(row=1, column=0)
        self.tamagachi_info_widget.Tamagachi_gender_label.grid(row=2, column=0)
        self.tamagachi_info_widget.Tamagachi_happiness_label.grid(row=3, column=0)
        self.tamagachi_info_widget.Tamagachi_time_label.grid(row=4, column=0)
        self.tamagachi_info_widget.grid()

        #interact buttons
        self.interaction_widget = InteractionWidget(self)
        self.interaction_widget.interaction_choice.grid(row=5, column=0)
        self.interaction_widget.interaction_button.grid(row=5, column=1)
        self.interaction_widget.grid()

        #message widget
        self.interaction_widget.game_message.grid(row=6, column=0)
        self.interaction_widget.grid()

        #back buttons
        self.backbuttonwidget = BackButtonWidget(self, prev_frame="NewGameSetupFrame")
        self.backbuttonwidget.Back_button.grid(row=7, column=0)
        self.backbuttonwidget.grid()

        self.update_game()

    def update_game(self):

        #check pet happiness and update pet image accordingly
        if (self.controller.Tamagachi.get_happiness() >= 8):
            print("happy")
            self.game_world_widget.update_canvas(new_pet_image=tamagachi_avatars[self.controller.Tamagachi.avatar]["happy"])
            pass
        elif (self.controller.Tamagachi.get_happiness() <= 3):
            print("sad")
            pass


        self.tamagachi_info_widget.update_info()                #update the tamagachi info widget
        self.after(1000, self.update_game)                      #call the update_tamagachi_info_widget again after 1 second. Recursion?
