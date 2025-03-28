"""
When adding tamagachi avatars or background use the dictionaries here.

"""

tamagachi_avatars = {
    "Orange Cat 1": {

        "States": {

            "Awake": {

                "default": "orange_cat1_default.png",

                "happy": "orange_cat1_happy.png",

                "sad": "orange_cat1_sad.png",
            },

            "Fatigued": {

                "tired": "orange_cat1_fatigued.png"        #need to add

            },

            "Asleep": {
                
                "sleepy": "orange_cat1_asleep.png"    #need to add

            }
        },

        "Interactions": {

            "Feed": {
                "animation": "orange_cat1_eating.png",
                "frames": 4,
                "cooldown": 30
            },

            "Hug": {
                "animation": "orange_cat1_hugging.png",
                "frames": 4,
                "cooldown": 30
            },

            "Scold": {
                "animation": "orange_cat1_scolding.png",
                "frames": 4,
                "cooldown": 30
            },

            "Level Up": {
                "animation": "orange_cat1_level_up.png",
                "frames": 4,
                "cooldown": 30
            }

        }

    },

    "Orange Cat 2": {
        "default": "orange_cat2_default.png"
    }
}


background_images = {
    "Front Lawn": "front_lawn.jpg",
    "Living Room": "living_room.jpg"
}