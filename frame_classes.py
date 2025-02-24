import tkinter as tk
from tkinter import ttk
from pathlib import Path
from utils.functions import getImagePath


from utils.widgets import ImageWidget, PetInfoWidget, StartButtonWidget, BackButtonWidget, QuitGameButtonWidget


class StartFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.cat_image_widget = ImageWidget(self, image_name="orange_cat.jpg")

        NewGameButton = ttk.Button(
            self, 
            text="New Game", 
            command=lambda: controller.show_frame("NewGameSetupFrame")
            )
        
        LoadGameButton = ttk.Button(
            self, 
            text="Load Game", 
            command=lambda: controller.show_frame("LoadGameSetupFrame")
            )
        
        self.quitbuttonwidget = QuitGameButtonWidget(self)
        #setup widgets
        self.cat_image_widget.image_label.grid(row=0, column=0)
        self.cat_image_widget.grid()

        NewGameButton.grid(row=1, column=0)
        LoadGameButton.grid(row=2, column=0)
        self.quitbuttonwidget.Quit_button.grid(row=3, column=0)
        self.quitbuttonwidget.grid()

class NewGameSetupFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # image widget
        self.cat_image_widget = ImageWidget(self, image_name="orange_cat.jpg")

        #Pet info widget
        self.petinfo = PetInfoWidget(self)

        #start button
        self.startbuttonwidget = StartButtonWidget(self)

        #back button
        self.backbuttonwidget = BackButtonWidget(self, prev_frame="StartFrame")

        #set widgets
        self.cat_image_widget.image_label.grid(row=0, column=0)
        self.cat_image_widget.grid()

        self.petinfo.Pet_name_label.grid(row=1, column=0)
        self.petinfo.Pet_name_entry.grid(row=1, column=1)
        self.petinfo.Pet_gender_label.grid(row=2, column=0)
        self.petinfo.Pet_gender_male_button.grid(row=2, column=1)
        self.petinfo.Pet_gender_male_button.grid(row=2, column=2)

        self.petinfo.grid()



        self.startbuttonwidget.Start_button.grid(row=3, column=0)
        self.startbuttonwidget.grid()

        self.backbuttonwidget.Back_button.grid(row=4, column=0)
        self.backbuttonwidget.grid()

class LoadGameSetupFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #back button
        self.backbuttonwidget = BackButtonWidget(self, prev_frame="StartFrame")

        self.backbuttonwidget.Back_button.grid(row=3, column=0)
        self.backbuttonwidget.grid()

        pass
