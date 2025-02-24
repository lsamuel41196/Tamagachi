import inspect
from pathlib import Path


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

def start_game():
     print("Start button pressed!")

def getImagePath(image_name):

     imagePath = str(Path().absolute() / "images" / image_name)

     return imagePath