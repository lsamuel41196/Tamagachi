class Tamagachi:
    def __init__(self):

        self.name = ""
        self.gender = ""
        self.happiness = 5  # Starts with moderate happiness

        self.image_name = "orange_cat2.png"
        self.image_size = (300, 300)

        print("tamagachi object created!")

    def set_name(self, name):
        self.name = name
        print("Name changed to " + name)
    
    def set_gender(self, gender):
        if gender != "Male" or "Female":
            self.gender = None
        else:
            self.gender = gender

        print("Gender changed to " + gender)

    def get_gender(self):
        return self.gender
    
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