import time
from game_dictionaries import tamagachi_avatars
import threading

class Tamagachi:
    def __init__(self):

        self.name = "Temp"
        self.gender = ""
        self._happiness = 5      #starts with moderate happiness 
        self._energy = 4        #start with high energy
        self._hunger = 4        #hunger for food
        self._level = 1          #level of pet
        self._experience = 10     #experience of pet

        # self.happiness_decay_thread = threading.Thread(target=self.happiness_decay, daemon=True)
        # self.energy_decay_thread = threading.Thread(target=self.energy_decay, daemon=True)
        # self.hunger_decay_thread = threading.Thread(target=self.hunger_decay, daemon=True)

        self.happiness_decay_thread = None
        self.energy_decay_thread = None
        self.hunger_decay_thread = None

        self.decay_threads = [self.happiness_decay_thread, self.energy_decay_thread, self.hunger_decay_thread]

        self.avatar = "Orange Cat 1"
        self.image_size = (150, 150)

        self.birth_time = float()
        self.alive_time = {
            "Hours": None,
            "Minutes": None,
            "Seconds": None
        }

        self.last_interaction_time = {
            "Feed": 0,
            "Hug": 0,
            "Scold": 0,
        }

        self.interactions = ["Feed", "Hug", "Scold", "Check Status", "Level Up"]
        self.current_status = "Idle"


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

    @property
    def happiness(self):
        return self._happiness
    
    @happiness.setter
    def happiness(self, value):
        self._happiness = max(0, min(value, 10))

    @property
    def energy(self):
        return self._energy
    
    @energy.setter
    def energy(self, value):
        self._energy = max(0, min(value, 10))

    @property
    def hunger(self):
        return self._hunger
    
    @hunger.setter
    def hunger(self, value):
        self._hunger = max(0, min(value, 10))

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        self._level = max(1, value)
        
    @property
    def experience(self):
        return self._experience
    
    @experience.setter
    def experience(self, value):

        self._experience = max(1, value)

    def happiness_decay(self):
        while True:
            time.sleep(10)
            if self.energy < 3 or self.hunger < 3:
                self.happiness -= 1
    
    def energy_decay(self):
        while True:
            time.sleep(15)
            self.energy -= 1

    def hunger_decay(self):
        while True:
            time.sleep(20)
            self.hunger -= 1

    def start_decay_threads(self):

        self.init_decay_threads()

        for thread in self.decay_threads:
            thread.start()

    def init_decay_threads(self):
        self.happiness_decay_thread = threading.Thread(target=self.happiness_decay, daemon=True)
        self.energy_decay_thread = threading.Thread(target=self.energy_decay, daemon=True)
        self.hunger_decay_thread = threading.Thread(target=self.hunger_decay, daemon=True)

        self.decay_threads = [self.happiness_decay_thread, self.energy_decay_thread, self.hunger_decay_thread]

    def feed(self):

        can_perform, remaining_time = self.can_perform_action("Feed")

        if can_perform == True:

            self.happiness += 2
            self.experience += 1
            self.hunger += 5

            message = f"{self.name} enjoys the food! 😋"

        else:
            message = f"Feed Cooldown: {remaining_time}"

        return [can_perform, message]

    def hug(self):

        can_perform, remaining_time = self.can_perform_action("Hug")

        if can_perform == True:
            self.happiness += 3
            self.experience += 1

            message = f"{self.name} feels loved! 🤗"

        else:
            message = f"Hug Cooldown: {remaining_time}"

        return [can_perform, message]

    def scold(self):

        can_perform, remaining_time = self.can_perform_action("Scold")

        if can_perform == True:
            self.happiness -= 1
            self.experience += 1

            message = f"{self.name} is flustered 😢"

        else:
            message = f"Scold Cooldown: {remaining_time}"

        return [can_perform, message]

    def level_up(self):
        
        if self.experience >= 10:

            can_perform = True

            self.experience -= 10
            self.level += 1

            message = f"Congratulations! {self.name} leveled up! 🎉"

        else:
            can_perform = False
            message = f"Not enough experience to level up."

        return [can_perform, message]

    def can_perform_action(self, interaction: str):
        
        current_time = time.time()
        last_interaction_time = self.last_interaction_time[interaction]
        remaining_time = round(tamagachi_avatars[self.avatar][interaction]["cooldown"] - (current_time - last_interaction_time))

        if remaining_time <= 0:
            self.last_interaction_time[interaction] = current_time
            return [True, remaining_time]
        else:
            return [False, remaining_time]

    def check_status(self):

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
    
    def animate(self):
        pass