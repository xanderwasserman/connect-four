# Connect Four

This documentation aims to give a better understanding of design choices, the current capabilities of the project, and the roadmap for future improvements.

## Time Spent
Approximately 5.5 hours in total.

## Design Rationale:
The core game logic is implemented using object-oriented principles within the connect_four module, which is completely decoupled from the user interface. This design enables multiple interfaces, both CLI and web, to be built on top of the same robust logic. Key components include:

- **ConnectFourGame:**
    Manages the overall game flow, board state, and turn-taking. Its modular design allows for easy reconfiguration of parameters such as board size, winning streak length, and player tokens.

- **Board:**
    Responsible for maintaining the grid state, placing pieces, and checking win/draw conditions.

- **Player and Computer:**
    Model the human and machine players respectively. While Player handles user input via CLI (or potentially another interface), Computer currently selects moves at random. This abstraction allows for future improvements to the AI.

- **Human-Machine-Interface (HMI)**
    The project supports two HMI types, a CLI interface (implemented in main_cli.py and using functions in hmi/cli_interface.py) and a web interface (using Flask, with templates and static files under hmi/templates and hmi/static). This separation ensures that the core game logic remains untouched regardless of how the game is presented to the user.

Unit tests have been integrated across the codebase, excluding the Web Interface, to ensure reliability and facilitate future changes. They cover core functionality as well as CLI interface interactions.

## Future Enhancements:

- Improve the AI to use a more advanced algorithm for a challenging opponent.
- Expand the web interface to support multiple concurrent players and richer interactions. This could involve persisting game states in a database or leveraging browser sessions to maintain individual game progress.
- Enhance test coverage and add more scenarios to ensure the application handles edge cases gracefully.
- Enhance input validation and error handling throughout the application.

## Known Limitations:

- Basic AI:
    The current "AI" uses random moves, which may result in a suboptimal challenge.
- Single-User:
    The web version currently supports only a single game session. As a result, multiple users accessing the application will share the same game state. Implementing multi-user support would require additional infrastructure (such as session management or a database).

