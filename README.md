# Text MMO-RPG

## Description
This is a text-based Massively Multiplayer Online Role-Playing Game (MMO-RPG) implemented in Python. The game features character creation, exploration, turn-based combat, and character progression.

## Features
- Character creation with customizable stats
- Turn-based combat system
- Spell casting system
- Equipment system with weapons and armor
- Multiple enemy types with unique abilities
- Character leveling and stat distribution
- Exploration of various locations
- Debug mode for easier testing and development

## Installation

### Local Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/text-mmo-rpg.git
   cd text-mmo-rpg
   ```
2. Install the required dependencies:
   ```
   pip install colorama
   ```

### Hugging Face Spaces Deployment
This game can also be deployed as a Hugging Face Space:

1. Create a new Space on Hugging Face, selecting "Streamlit" as the SDK.
2. Upload the following files to your Space:
   - `app.py` (main Streamlit app)
   - `spells.py`
   - `enemies.py`
3. Create a `requirements.txt` file in your Space with the following content:
   ```
   streamlit
   ```

## How to Play

### Local Version
Run the game using Python:
```
python text_mmo_rpg.py
```

Follow the on-screen prompts to create your character and play the game. Use the provided options to explore, battle enemies, rest, and manage your character.

### Hugging Face Spaces Version
Visit the URL of your Hugging Face Space. The game will run in your web browser. Use the provided UI elements to interact with the game.

## Game Commands
- `[E]xplore`: Venture into a random location and potentially encounter enemies
- `[R]est`: Recover some HP, with a chance of being ambushed
- `[C]haracter Sheet`: View your character's stats and equipment
- `[D]istribute Stat Points`: Allocate points to improve your character's attributes
- `[Q]uit`: Exit the game

## Debug Mode
Enter 'admin' as your character name to activate debug mode. This mode provides additional options for testing and development, such as instantly leveling up your character.

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- This project was created as a learning exercise in Python game development.
- Special thanks to the Python and Streamlit communities for their excellent documentation and resources.
