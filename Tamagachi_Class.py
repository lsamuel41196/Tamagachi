import time
from game_dictionaries import tamagachi_avatars

class Tamagachi:
    def __init__(self):

        self.name = "Temp"
        self.gender = "Male"
        self.happiness = 5  # Starts with moderate happiness

        self.avatar = "Orange Cat 1"
        self.image_size = (150, 150)

        self.birth_time = float()
        self.alive_time = {
            "Hours": None,
            "Minutes": None,
            "Seconds": None
        }

        self.interactions = ["Feed", "Hug", "Check Status"]

    def set_name(self, name):
        """
        This function sets the name of your tamagachi pet
        """
        self.name = name
    
    def set_gender(self, gender:str):
        """
        This function sets the gender of the tamagachi object
        """

        allowed_genders = ["Male", "Female"]

        if gender not in allowed_genders:
            raise ValueError(f'Invalid gender: {gender}. Gender must be male or female')
        else:
            self.gender = gender

    def get_gender(self) -> str:
        return self.gender
    
    def get_happiness(self) -> int:
        """
        get happiness of pet

        Return: hapiness integer
        """

        return self.happiness

    def feed(self) -> str:
        self.happiness += 2

        message = f"{self.name} enjoys the food! 😋"

        return (message)

    def hug(self) -> str:
        self.happiness += 3

        message = f"{self.name} feels loved! 🤗"

        return (message)

    def check_status(self) -> str:
        if self.happiness >= 10:
            message = f"{self.name} is super happy! 😍"
        elif self.happiness >= 5:
            message = f"{self.name} is doing well! 😊"
        else:
            message = "{self.name} is feeling lonely... 😢 Give it some love!"
        
        return (message)

    def update_alive_time(self):
        current_time = time.time()
        elapsed_time = int(current_time - self.birth_time)

        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = elapsed_time % 60

        self.alive_time["Hours"] = hours
        self.alive_time["Minutes"] = minutes
        self.alive_time["Seconds"] = seconds

    def print_alive_time(self) -> str:

        self.update_alive_time()

        hours = self.alive_time["Hours"]
        minutes = self.alive_time["Minutes"]
        seconds = self.alive_time["Seconds"]

        alive_time_string = f"{hours:02}:{minutes:02}:{seconds:02}"

        return alive_time_string