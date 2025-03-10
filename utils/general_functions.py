import inspect
import json
from pathlib import Path
from tkinter import messagebox, filedialog


def get_frame_classes(file_path):
    """
    Extracts classes from a given Python file.

    Args:
        file_path (str): The path to the Python file.

    Returns:
        list: A list of class objects found in the file.
    """
    
    try:
        module_name = file_path.replace(".py", "")  # Remove .py extension
        module = __import__(module_name)
    except ModuleNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []

    classes = [member[1] for member in inspect.getmembers(module, inspect.isclass)]
    return classes

def determineNextFrame():
     pass

def getImagePath(image_name) -> str:
     
     """
     Gets the file path of an image based on the image name.

     Args:
        image_name (str): The name of the image file.

     Returns:
        str: The file path of the image
     """

     imagePath = str(Path().absolute() / "images" / image_name)

     return imagePath

def clamp(value, min_value, max_value) -> int:
    """
    This method clamps the value in a certain range
    
    params:
        value - value to be clamped
        min_value - minimum bound
        max_value - maximum bound
    """
    return(max(min_value, min(value, max_value)))


def show_popup(title: str, message: str):
    """
    This method shows a pop up message in the game

    params:
        title[str]: title of the dialog window 
        message[str]: shows the message of the window
    """

    messagebox.showinfo(title, message)\
    

def save_game(tamagachi_info):
    """
    Function saves the game
    """

    filepath = filedialog.asksaveasfilename(
        title="Save game as...",
        initialdir= str(Path.cwd()) + r"\saved_games",
        filetypes = (
        ("JSON Files","*.json"),
        ),
        defaultextension="json"
    )

    if filepath:
        with open(filepath, 'w') as f:
            json.dump(
                tamagachi_info,
                f
                )
            show_popup("Game Message", "Game saved!")


def quit_game(self):
    self.destroy()