# Dark Dungeon - Game Module for Grue Text Adventure Engine

# Dictionary of all locations
locations = {
    "start": {
        "name": "Prison Cell",
        "description": "You are in a damp, dark prison cell. Water drips from the ceiling, and the only light comes from a torch in the hallway.",
        "exits": {
            "north": "dungeon_hall"
        },
        "items": ["broken_chain"],
        "characters": [],
        "first_visit": True
    },
    "dungeon_hall": {
        "name": "Dungeon Hallway",
        "description": "A gloomy hallway lined with other prison cells. Most seem empty and abandoned.",
        "exits": {
            "south": "start",
            "east": "guard_room"
        },
        "items": ["torch"],
        "characters": [],
        "first_visit": True
    },
    "guard_room": {
        "name": "Guard Room",
        "description": "A small chamber where dungeon guards would rest. It appears to have been abandoned in haste.",
        "exits": {
            "west": "dungeon_hall",
            "north": "stairway"
        },
        "items": ["rusty_sword"],
        "characters": ["rat"],
        "first_visit": True
    },
    "stairway": {
        "name": "Winding Staircase",
        "description": "A narrow stone staircase spiraling upward into darkness.",
        "exits": {
            "south": "guard_room",
            "up": "entrance_hall"
        },
        "items": [],
        "characters": [],
        "first_visit": True
    },
    "entrance_hall": {
        "name": "Dungeon Entrance",
        "description": "A cavernous hall with a heavy portcullis blocking the way out.",
        "exits": {
            "down": "stairway"
        },
        "items": ["lever"],
        "characters": ["ghost"],
        "first_visit": True
    }
}

# Dictionary of all items
items = {
    "broken_chain": {
        "name": "Broken Chain",
        "description": "A heavy iron chain with a shackle on one end, broken on the other.",
        "portable": True,
        "visible": True,
        "actions": ["take", "drop", "examine"],
        "properties": {
            "weight": 3
        }
    },
    "torch": {
        "name": "Wall Torch",
        "description": "A flickering torch mounted on the wall, providing dim light.",
        "portable": True,
        "visible": True,
        "actions": ["take", "drop", "examine"],
        "properties": {
            "weight": 1,
            "lit": True
        }
    },
    "rusty_sword": {
        "name": "Rusty Sword",
        "description": "An old sword with a badly corroded blade. Still somewhat sharp.",
        "portable": True,
        "visible": True,
        "actions": ["take", "drop", "examine", "attack"],
        "properties": {
            "weight": 2,
            "damage": 3
        }
    },
    "lever": {
        "name": "Rusted Lever",
        "description": "A heavy iron lever mounted in the wall. It might control the portcullis.",
        "portable": False,
        "visible": True,
        "actions": ["examine", "pull"],
        "properties": {
            "pulled": False
        }
    }
}

# Dictionary of all characters
characters = {
    "rat": {
        "name": "Giant Rat",
        "description": "A rat the size of a small dog, with glowing red eyes and matted fur.",
        "friendly": False,
        "dialogue": {
            "greeting": "*The rat hisses menacingly*",
            "help": "*The rat seems uninterested in helping you*",
            "defeat": "*The rat squeals and scurries away into the darkness*"
        },
        "inventory": [],
        "properties": {
            "health": 5,
            "damage": 1,
            "defeated": False
        }
    },
    "ghost": {
        "name": "Translucent Ghost",
        "description": "The spectral form of what appears to be a former prisoner, floating silently.",
        "friendly": True,
        "dialogue": {
            "greeting": "*A hollow voice whispers* 'Trapped... just like I was...'",
            "help": "'Pull the lever... but beware what comes after...'",
            "quest": "'Find my remains in the eastern cell... let me rest...'",
        },
        "inventory": [],
        "properties": {
            "quest_active": False,
            "quest_completed": False
        }
    }
}

# Player starting state
player = {
    "current_location": "start",
    "inventory": [],
    "max_inventory": 8,
    "stats": {
        "moves": 0,
        "health": 10,
        "max_health": 10
    }
}

# Game metadata
game_info = {
    "title": "Dark Dungeon",
    "intro_text": """Welcome to the Dark Dungeon!

You awaken in a prison cell with no memory of how you got here.
The sound of dripping water and distant moans fills the air.
Can you find your way to freedom?

Type 'help' at any time to see available commands.
""",
    "author": "Your Name",
    "version": "0.1"
}