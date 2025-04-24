# Grue - Interactive Engine
## Game Module Format Documentation

The Grue Text Adventure Engine is designed to be data-driven, allowing you to create multiple adventure games using the same engine. Each game is defined as a Python module that contains specific data structures. This document explains how to create your own game modules.

## Overview

A game module is a Python file that defines the following components:
- Locations (areas in your game world)
- Items (objects that can be interacted with)
- Characters (beings that inhabit the world)
- Player information (starting location, inventory, stats)
- Game metadata (title, introduction text, etc.)

## Required Data Structures

Each game module must define the following Python dictionaries:

### 1. `locations`

A dictionary of all locations in the game. Each location should have a unique ID as the key and a dictionary of properties as the value.

```python
locations = {
    "room_id": {
        "name": "Room Name",
        "description": "Detailed description of the room.",
        "exits": {
            "north": "connecting_room_id",
            "east": "another_room_id"
        },
        "items": ["item_id1", "item_id2"],
        "characters": ["character_id1"],
        "first_visit": True  # Flag to track if player has visited before
    },
    # More locations...
}
```

**Required location properties:**
- `name`: Display name for the location
- `description`: Text description shown when player enters or looks around
- `exits`: Dictionary mapping directions to other location IDs
- `items`: List of item IDs present in this location
- `characters`: List of character IDs present in this location
- `first_visit`: Boolean indicating if player has visited before (start as True)

### 2. `items`

A dictionary of all items in the game. Each item should have a unique ID as the key and a dictionary of properties as the value.

```python
items = {
    "item_id": {
        "name": "Item Name",
        "description": "Detailed description of the item.",
        "portable": True,  # Can the player pick it up?
        "visible": True,   # Can the player see it?
        "actions": ["take", "drop", "examine", "use"],
        "properties": {
            "weight": 1,
            "opens": "door_id",
            # Any custom properties for your game
        }
    },
    # More items...
}
```

**Required item properties:**
- `name`: Display name for the item
- `description`: Text description shown when examined
- `portable`: Boolean indicating if item can be picked up
- `visible`: Boolean indicating if item can be seen
- `actions`: List of verbs that can be used with this item
- `properties`: Dictionary of custom properties for game mechanics

### 3. `characters`

A dictionary of all characters in the game. Each character should have a unique ID as the key and a dictionary of properties as the value.

```python
characters = {
    "character_id": {
        "name": "Character Name",
        "description": "Detailed description of the character.",
        "friendly": True,  # Is the character friendly to the player?
        "dialogue": {
            "greeting": "Hello there!",
            "help": "Try looking behind the waterfall.",
            "quest": "Please find my lost treasure."
        },
        "inventory": ["item_id1"],  # Items the character has
        "properties": {
            "quest_active": False,
            "quest_completed": False,
            # Any custom properties for your game
        }
    },
    # More characters...
}
```

**Required character properties:**
- `name`: Display name for the character
- `description`: Text description shown when examined
- `friendly`: Boolean indicating if character is friendly
- `dialogue`: Dictionary of different dialogue options
- `inventory`: List of item IDs the character has
- `properties`: Dictionary of custom properties for game mechanics

### 4. `player`

A dictionary defining the player's starting state.

```python
player = {
    "current_location": "starting_room_id",
    "inventory": [],  # Starting items
    "max_inventory": 10,  # Maximum items player can carry
    "stats": {
        "moves": 0,
        # Any custom stats for your game
    }
}
```

**Required player properties:**
- `current_location`: ID of starting location
- `inventory`: List of item IDs the player starts with
- `max_inventory`: Maximum number of items the player can carry
- `stats`: Dictionary of statistics to track

### 5. `game_info`

A dictionary containing metadata about the game.

```python
game_info = {
    "title": "Your Game Title",
    "intro_text": """
Welcome to your adventure!
This is the introduction text that players will see.
    """,
    "author": "Your Name",
    "version": "0.1"
}
```

**Required game_info properties:**
- `title`: The title of your game
- `intro_text`: Introduction text shown at the start
- `author`: Game creator's name
- `version`: Version number

## Example Game Module

Here's a minimal example of a valid game module:

```python
# tiny_adventure.py - A minimal Grue Text Adventure

# Dictionary of all locations
locations = {
    "cabin": {
        "name": "Small Cabin",
        "description": "A cozy cabin in the woods. A fire crackles in the hearth.",
        "exits": {
            "outside": "forest"
        },
        "items": ["lantern"],
        "characters": [],
        "first_visit": True
    },
    "forest": {
        "name": "Forest Path",
        "description": "A winding path through tall pine trees.",
        "exits": {
            "inside": "cabin",
            "north": "lake"
        },
        "items": ["stick"],
        "characters": [],
        "first_visit": True
    },
    "lake": {
        "name": "Mountain Lake",
        "description": "A crystal clear lake surrounded by mountains.",
        "exits": {
            "south": "forest"
        },
        "items": [],
        "characters": ["fisherman"],
        "first_visit": True
    }
}

# Dictionary of all items
items = {
    "lantern": {
        "name": "Oil Lantern",
        "description": "A brass oil lantern, currently unlit.",
        "portable": True,
        "visible": True,
        "actions": ["take", "drop", "examine", "light"],
        "properties": {
            "weight": 2,
            "lit": False
        }
    },
    "stick": {
        "name": "Wooden Stick",
        "description": "A sturdy wooden stick.",
        "portable": True,
        "visible": True,
        "actions": ["take", "drop", "examine"],
        "properties": {
            "weight": 1
        }
    }
}

# Dictionary of all characters
characters = {
    "fisherman": {
        "name": "Old Fisherman",
        "description": "An elderly man fishing by the lakeside.",
        "friendly": True,
        "dialogue": {
            "greeting": "Fine day for fishing, isn't it?",
            "help": "I've seen something shiny at the bottom of the lake.",
            "quest": "If you could find my lucky fishing hook, I'd be grateful."
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
    "current_location": "cabin",
    "inventory": [],
    "max_inventory": 5,
    "stats": {
        "moves": 0
    }
}

# Game metadata
game_info = {
    "title": "Tiny Adventure",
    "intro_text": """
Welcome to Tiny Adventure!

You've come to the mountains for a relaxing weekend getaway.
Explore the area and see what you can find.

Type 'help' for a list of commands.
""",
    "author": "Your Name",
    "version": "0.1"
}
```

## Creating a New Game

To create a new game:

1. Create a new Python file with a descriptive name (e.g., `my_adventure.py`)
2. Define all the required dictionaries (`locations`, `items`, `characters`, `player`, `game_info`)
3. Add your game to the list in the `list_available_games()` function in `main.py`:

```python
def list_available_games():
    return [
        {"id": "crystalia_manor", "title": "Crystalia Manor", "description": "Explore a mysterious abandoned mansion"},
        {"id": "dark_dungeon", "title": "Dark Dungeon", "description": "Escape from a dangerous underground prison"},
        {"id": "my_adventure", "title": "My Adventure", "description": "Your game description here"}
    ]
```

## Advanced Tips

1. **Custom Properties**
   - Use the `properties` dictionary to add game-specific attributes to locations, items, and characters
   - The engine will ignore properties it doesn't recognize, so feel free to add any data you need

2. **Special Item Actions**
   - The basic engine recognizes: "take", "drop", "examine", "use"
   - You can add custom actions in the item's `actions` list, then handle them in a modified version of the engine

3. **Expanding the Engine**
   - As you get comfortable, you can modify the `GameEngine` class to add new features like:
     - Combat systems
     - Puzzles that require specific item combinations
     - Character relationships and quests
     - Inventory limitations based on weight

4. **Game State**
   - Use the `first_visit` property of locations to trigger special events when a player first enters
   - Use character and item properties to track game state like quests, locked doors, etc.

## Limitations

The current basic engine has some limitations:
- No built-in saving/loading
- Limited interaction between items
- Basic character interactions (just dialogue)
- No combat system (though you could add one!)

These limitations can be addressed by extending the engine as your programming skills develop.

---

Happy adventuring with the Grue - Text Adventure Engine! Just remember: it's dangerous to go alone in dark places - you might be eaten by a grue!
