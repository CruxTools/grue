# Crystalia Manor - Game Module for Grue Text Adventure Engine

# Dictionary of all locations
locations = {
    "start": {
        "name": "Entrance Hall",
        "description": "You are in a grand entrance hall with marble floors and a dusty chandelier overhead.",
        "exits": {
            "north": "hallway"
        },
        "items": [],
        "characters": [],
        "first_visit": True
    },
    "hallway": {
        "name": "Main Corridor",
        "description": "You are in a long corridor with faded portraits hanging on wood-paneled walls.",
        "exits": {
            "south": "start",
            "east": "garden"
        },
        "items": ["old_key"],
        "characters": [],
        "first_visit": True
    },
    "garden": {
        "name": "Overgrown Garden",
        "description": "You are in what was once a manicured garden, now wild and overgrown with exotic plants.",
        "exits": {
            "west": "hallway"
        },
        "items": ["flower"],
        "characters": ["gardener"],
        "first_visit": True
    }
}

# Dictionary of all items
items = {
    "old_key": {
        "name": "Old Key",
        "description": "A rusty old key. It might open something nearby.",
        "portable": True,
        "visible": True,
        "actions": ["take", "drop", "examine", "use"],
        "properties": {
            "weight": 1,
            "opens": "locked_door"
        }
    },
    "flower": {
        "name": "Beautiful Flower",
        "description": "A vibrant flower with red and yellow petals.",
        "portable": True,
        "visible": True,
        "actions": ["take", "drop", "examine", "smell"],
        "properties": {
            "weight": 1,
            "fragrance": "sweet"
        }
    },
    "locked_door": {
        "name": "Locked Door",
        "description": "A heavy wooden door with an old keyhole.",
        "portable": False,
        "visible": True,
        "actions": ["examine", "unlock"],
        "properties": {
            "locked": True,
            "key_id": "old_key"
        }
    }
}

# Dictionary of all characters
characters = {
    "gardener": {
        "name": "Ancient Groundskeeper",
        "description": "A wizened old man with gnarled hands tending to the wild plants. His eyes hold secrets.",
        "friendly": True,
        "dialogue": {
            "greeting": "Ah, a visitor to Crystalia Manor? It's been... decades since we've had guests.",
            "help": "If you seek the manor's treasures, look beneath the crumbling fountain.",
            "quest": "The crystal key has been lost somewhere in the east wing. Find it, and many doors will open to you."
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
    "max_inventory": 10,
    "stats": {
        "moves": 0
    }
}

# Game metadata
game_info = {
    "title": "Crystalia Manor",
    "intro_text": """Welcome to Crystalia Manor!

You find yourself in a mysterious mansion with no memory of how you got here.
Perhaps exploring your surroundings will help you understand where you are.

Type 'help' at any time to see available commands.
""",
    "author": "Your Name",
    "version": "0.1"
}