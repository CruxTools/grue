# Grue Text Adventure Engine - Main Game Launcher
import importlib
from grue_engine import GrueEngine


def list_available_games():
    """Find all available game modules in the games directory."""
    # In a real implementation, this would scan the directory
    # For our demo, we'll return a hardcoded list
    return [
        {"id": "crystalia_manor", "title": "Crystalia Manor", "description": "Explore a mysterious abandoned mansion"},
        {"id": "dark_dungeon", "title": "Dark Dungeon", "description": "Escape from a dangerous underground prison"}
    ]


def load_game_module(game_id):
    """Dynamically import a game module."""
    try:
        # In a real implementation, you'd import from a games subdirectory
        game_module = importlib.import_module(game_id)
        return game_module
    except ImportError as e:
        print(f"Error loading game module: {e}")
        return None


def display_game_menu():
    """Display a menu of available games."""
    games = list_available_games()

    print("\nGrue - Text Adventure Engine")
    print("=========================")
    print("Available Adventures:")
    print()

    for i, game in enumerate(games, 1):
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
            if 0 <= choice < len(games):
                return games[choice]["id"]
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
        game_module = load_game_module(selected_game_id)
        if not game_module:
            print("Failed to load the selected game. Please try another.")
            continue

        # Create and run the game engine with the selected game
        engine = GrueEngine()
        engine.load_game(game_module)
        engine.start_game()

        # After the game ends, we return to the menu
        print("\nGame over. Returning to main menu...")


if __name__ == "__main__":
    main()