import time

class Tamagachi:
    def __init__(self):

        self.name = "Temp"
        self.gender = "Male"
        self.happiness = 5  # Starts with moderate happiness

        self.avatar = "Orange Cat 1"

        self.image_name = "orange_cat1.jpg"
        self.image_size = (300, 300)

        self.start_time = float()
        self.play_time = {
            "Hours": None,
            "Minutes": None,
            "Seconds": None
        }

        self.interactions = ["Feed", "Hug", "Check Status"]

        self.update_play_time()

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

    def update_play_time(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        hours, minutes = divmod(minutes, 60)

        self.play_time["Hours"] = hours
        self.play_time["Minutes"] = minutes
        self.play_time["Seconds"] = seconds

    def print_play_time(self) -> str:

        hours = str(self.play_time["Hours"])
        minutes = str(self.play_time["Minutes"])
        seconds = str(self.play_time["Seconds"])

        play_time_string = f"{hours:02}:{minutes:02}:{seconds:02}"

        return play_time_string