import time

class Tamagachi:
    def __init__(self, name):
        self.name = name
        self.happiness = 5  # Starts with moderate happiness
    
    def feed(self):
        self.happiness += 2
        print(f"{self.name} enjoys the food! 😋 Happiness: {self.happiness}")

    def hug(self):
        self.happiness += 3
        print(f"{self.name} feels loved! 🤗 Happiness: {self.happiness}")

    def check_status(self):
        if self.happiness >= 10:
            print(f"{self.name} is super happy! 😍")
        elif self.happiness >= 5:
            print(f"{self.name} is doing well! 😊")
        else:
            print(f"{self.name} is feeling lonely... 😢 Give it some love!")