class Tamagachi:
    def __init__(self):

        self.name = "Temp"
        self.gender = "Male"
        self.happiness = 5  # Starts with moderate happiness

        self.image_name = "orange_cat2.png"
        self.image_size = (300, 300)

        self.interactions = ["Feed", "Hug", "Check Status"]

        print("tamagachi object created!")

    def set_name(self, name):
        self.name = name
        print("Name changed to " + self.name)
    
    def set_gender(self, gender:str):
        """
        This function sets the gender of the tamagachi object
        """

        allowed_genders = ["Male", "Female"]

        if gender not in allowed_genders:
            raise ValueError(f'Invalid gender: {gender}. Gender must be male or female')
        else:
            self.gender = gender

        print("Gender changed to " +  self.gender)

    def get_gender(self) -> str:
        return self.gender
    
    def feed(self) -> str:
        self.happiness += 2

        message = f"{self.name} enjoys the food! 😋 Happiness: {self.happiness}"

        return (message)

    def hug(self) -> str:
        self.happiness += 3

        message = f"{self.name} feels loved! 🤗 Happiness: {self.happiness}"

        return (message)

    def check_status(self) -> str:
        if self.happiness >= 10:
            message = f"{self.name} is super happy! 😍"
        elif self.happiness >= 5:
            message = f"{self.name} is doing well! 😊"
        else:
            message = "{self.name} is feeling lonely... 😢 Give it some love!"
        
        return (message)
