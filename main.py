# Import the game engine
from grue_engine import GrueEngine

# Direct imports of game modules
import crystalia_manor
import dark_dungeon

# Dictionary mapping game IDs to modules
GAMES = {
    "crystalia_manor": crystalia_manor,
    "dark_dungeon": dark_dungeon
}


def display_game_menu():
    """Display a menu of available games."""
    game_selection = [
        {"id": "crystalia_manor", "title": "Crystalia Manor", "description": "Explore a mysterious abandoned mansion"},
        {"id": "dark_dungeon", "title": "Dark Dungeon", "description": "Escape from a dangerous underground prison"}
    ]

    print("\nGrue - Text Adventure Engine")
    print("=========================")
    print("Available Adventures:")
    print()

    for i, game in enumerate(game_selection, 1):
        print(f"{i}. {game['title']}")
        print(f"   {game['description']}")
        print()

    print("0. Quit")
    print()

    while True:
        try:
            choice = input("Select an adventure (number): ").strip()
            if choice == '0':
                return None

            choice = int(choice) - 1
            if 0 <= choice < len(game_selection):
                return game_selection[choice]["id"]
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a number.")


def main():
    """Main function to run the game."""

    while True:
        # Display game selection menu
        selected_game_id = display_game_menu()

        if selected_game_id is None:
            print("Thanks for playing! Goodbye.")
            break

        # Load the selected game module
        game_module = GAMES[selected_game_id]

        # Create and run the game engine with the selected game
        engine = GrueEngine()
        engine.load_game(game_module)
        engine.start_game()

        # After the game ends, we return to the menu
        print("\nGame over. Returning to main menu...")


if __name__ == "__main__":
    main()