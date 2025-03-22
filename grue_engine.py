# Grue Text Adventure Engine - Core Engine

class GrueEngine:
    def __init__(self):
        self.locations = {}
        self.items = {}
        self.characters = {}
        self.player = {}
        self.game_info = {}
        self.running = False
        self.current_game = None

    def load_game(self, game_module):
        """Load data from a game module."""
        self.current_game = game_module
        self.locations = game_module.locations
        self.items = game_module.items
        self.characters = game_module.characters
        self.player = game_module.player.copy()  # Copy to allow multiple plays
        self.game_info = game_module.game_info

    def list_available_games(self):
        """Return a list of available games."""
        # In a real implementation, this would scan a directory
        # For now, we'll return a hardcoded list
        return ["crystalia_manor", "dark_dungeon"]

    def start_game(self):
        """Start the game loop."""
        self.running = True
        self.display_intro()

        # Main game loop
        while self.running:
            self.display_location()
            command = input("> ").strip().lower()
            response = self.process_command(command)
            print(response)

    def display_intro(self):
        """Display the game introduction."""
        print(f"\n{self.game_info['title']}")
        print("=" * len(self.game_info['title']))
        print(self.game_info['intro_text'])
        print()

    def display_location(self):
        """Display the current location description."""
        location_id = self.player['current_location']
        location = self.locations[location_id]

        print(f"\n{location['name']}")
        print("-" * len(location['name']))
        print(location['description'])

        # Display exits
        if location['exits']:
            exit_list = ", ".join(location['exits'].keys())
            print(f"Exits: {exit_list}")
        else:
            print("There are no obvious exits.")

        # Display items
        visible_items = [self.items[item_id]['name'] for item_id in location['items']
                         if self.items[item_id]['visible']]
        if visible_items:
            if len(visible_items) == 1:
                print(f"You can see a {visible_items[0]} here.")
            else:
                item_list = ", ".join(visible_items[:-1]) + " and a " + visible_items[-1]
                print(f"You can see a {item_list} here.")

        # Display characters
        if location['characters']:
            for char_id in location['characters']:
                char = self.characters[char_id]
                print(f"There is {char['name']} here.")

    def process_command(self, command):
        """Process a player command and return the response."""
        # Update move counter for every command
        self.player['stats']['moves'] += 1

        # Very basic command processing
        if command in ["quit", "exit", "bye"]:
            self.running = False
            return "Thanks for playing!"

        elif command in ["look", "l"]:
            # We'll let the next loop iteration display the location
            return "You look around."

        elif command.startswith("go "):
            direction = command[3:]  # Remove "go " from the start
            return self.move_player(direction)

        elif command in ["north", "n", "south", "s", "east", "e", "west", "w", "up", "u", "down", "d"]:
            # Handle directional shortcuts
            direction_map = {
                "n": "north", "s": "south", "e": "east", "w": "west",
                "u": "up", "d": "down"
            }
            direction = direction_map.get(command, command)  # Convert shorthand to full direction
            return self.move_player(direction)

        elif command in ["inventory", "i"]:
            return self.show_inventory()

        elif command.startswith("take ") or command.startswith("get "):
            item_name = command[5:] if command.startswith("take ") else command[4:]
            return self.take_item(item_name)

        elif command.startswith("drop "):
            item_name = command[5:]
            return self.drop_item(item_name)

        elif command.startswith("examine ") or command.startswith("look at "):
            target = command[8:] if command.startswith("examine ") else command[8:]
            return self.examine(target)

        elif command.startswith("talk to "):
            char_name = command[8:]
            return self.talk_to(char_name)

        elif command in ["help", "h", "?"]:
            return """
Available commands:
- go [direction] : Move in a direction (north, south, east, west, up, down)
- look           : Look around
- inventory      : Check what you're carrying
- take [item]    : Pick up an item
- drop [item]    : Drop an item you're carrying
- examine [thing]: Look at something more closely
- talk to [char] : Talk to a character
- quit           : End the game
You can also use shortcuts: n, s, e, w for directions, l for look, i for inventory
"""
        else:
            return "I don't understand that command. Type 'help' for a list of commands."

    def move_player(self, direction):
        """Move the player in the specified direction if possible."""
        current_loc = self.locations[self.player['current_location']]

        if direction in current_loc['exits']:
            new_location_id = current_loc['exits'][direction]
            self.player['current_location'] = new_location_id
            new_loc = self.locations[new_location_id]

            # If it's the first visit, we'll just let the main loop show the description
            if new_loc['first_visit']:
                new_loc['first_visit'] = False
                return f"You go {direction} to {new_loc['name']}."
            else:
                return f"You go {direction} to {new_loc['name']}."
        else:
            return f"You can't go {direction} from here."

    def show_inventory(self):
        """Show what the player is carrying."""
        if not self.player['inventory']:
            return "You are not carrying anything."

        items_carried = [self.items[item_id]['name'] for item_id in self.player['inventory']]
        if len(items_carried) == 1:
            return f"You are carrying a {items_carried[0]}."
        else:
            item_list = ", ".join([f"a {item}" for item in items_carried[:-1]]) + f" and a {items_carried[-1]}"
            return f"You are carrying {item_list}."

    def get_item_id_from_name(self, item_name):
        """Convert an item name to its ID. Returns None if not found."""
        # First check if item_name is an exact ID
        if item_name in self.items:
            return item_name

        # Try to match by name
        for item_id, item in self.items.items():
            if item['name'].lower() == item_name.lower():
                return item_id

        # Try to match by partial name (less precise)
        for item_id, item in self.items.items():
            if item_name.lower() in item['name'].lower():
                return item_id

        return None

    def take_item(self, item_name):
        """Try to take an item from the current location."""
        item_id = self.get_item_id_from_name(item_name)

        if not item_id:
            return f"You don't see a {item_name} here."

        current_loc = self.locations[self.player['current_location']]

        if item_id not in current_loc['items']:
            return f"You don't see a {item_name} here."

        item = self.items[item_id]

        if not item['portable']:
            return f"You can't take the {item['name']}."

        if len(self.player['inventory']) >= self.player['max_inventory']:
            return "You can't carry any more items."

        # Remove from location and add to inventory
        current_loc['items'].remove(item_id)
        self.player['inventory'].append(item_id)

        return f"You take the {item['name']}."

    def drop_item(self, item_name):
        """Drop an item from inventory to the current location."""
        item_id = self.get_item_id_from_name(item_name)

        if not item_id or item_id not in self.player['inventory']:
            return f"You don't have a {item_name}."

        item = self.items[item_id]

        # Remove from inventory and add to location
        self.player['inventory'].remove(item_id)
        current_loc = self.locations[self.player['current_location']]
        current_loc['items'].append(item_id)

        return f"You drop the {item['name']}."

    def examine(self, target_name):
        """Examine an item, character, or feature more closely."""
        # First check inventory
        for item_id in self.player['inventory']:
            item = self.items[item_id]
            if target_name.lower() in item['name'].lower():
                return item['description']

        # Then check location items
        current_loc = self.locations[self.player['current_location']]
        for item_id in current_loc['items']:
            item = self.items[item_id]
            if target_name.lower() in item['name'].lower():
                return item['description']

        # Then check location characters
        for char_id in current_loc['characters']:
            char = self.characters[char_id]
            if target_name.lower() in char['name'].lower():
                return char['description']

        # If nothing matches
        return f"You don't see any {target_name} here."

    def talk_to(self, char_name):
        """Talk to a character in the current location."""
        current_loc = self.locations[self.player['current_location']]

        # Find character by name
        target_char = None
        for char_id in current_loc['characters']:
            char = self.characters[char_id]
            if char_name.lower() in char['name'].lower():
                target_char = char
                break

        if not target_char:
            return f"There's no {char_name} here to talk to."

        # For now, just return the greeting dialogue
        return f"{target_char['name']}: \"{target_char['dialogue']['greeting']}\""