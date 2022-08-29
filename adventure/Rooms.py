Rooms = {                                           # Create a variable called "Rooms" that contains a dictionary

    "red": {                                            # Create a key called "red" with value of everything in the dictionary that follows:
        "name": "The Red room",                             # A key ("name") and value ("The Red room") pair
        "description": """\
            This room is red.
            The brick walls are old and crumbly, and the wall to the north has partially collapsed.
            To the south you see something green.""",       # <-- A multiline string!!!
        "exits": {                                          # Create a key "exits" with value of the dictionary below:
            "south": "green",                                   # Key-value pair: Key is the direction, value is the destination room
            "north": "wasteland"                                # Key-value pair: Key is the direction, value is the destination room
        },
        "items": [ "sword", "shield", "apple" ]             # Create a key called "items" with a value that is a list containing the items as strings
    },                                                  # End of dictionary "red"

    "green": {
        "name": "The Green room",
        "description": """\
            This room is green.
            Every surface is covered with verdandtly green moss that is soft to the touch.""",
        "exits": {
            "north": "red",
            "east": "blue",
            "south": "purple"
        },
        "items": ["golden ring"]
    },

    "purple": {
        "name": "The Purple room",
        "description": """\
            This room is purple.
            Looks like something spewed purple slime all over the place, even the floor is slippery.""",
        "exits": {
            "north": "green"
        },
        "items": ["blue key", "empty bottle" ]

    },

    "blue": {
        "name": "The Blue room",
        "description": """\
            This room is blue.
            It's a large cave of bluish rock, with a bubbling natural fountain at the center of it.
            The water looks drinkable.
            Through an opening in the north wall, you see something glittering, and hear sounds of a large beast breathing as if asleep.
            """,
        "exits": {
            "west": "green",
            "north": "golden"
        },
        "items": []
    },

    "golden": {
        "name": "The Golden room",
        "description": """\
            This room is golden.
            The huge cave is filled with treasure, every inch of it bedecked with gems and gold.
            In the middle of the cave is a mountain of gold, atop which a sleeping dragon lies,
            as golden in color as the rest of the room.""",
        "exits": {
            "south": "blue"
        },

        "items": ["gold", "gold", "gold"]
    }
}                                                       # End of dictionary "Rooms"
