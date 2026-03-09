# Sudoku Game - Terminal Edition

A fully interactive Sudoku game playable directly in your terminal. Generate random puzzles, validate your moves, and solve Sudoku with three difficulty levels.

## Features

- **Three Difficulty Levels**: Easy (40 clues), Medium (32 clues), Hard (24 clues)
- **Board Generation**: Randomly generates unique valid Sudoku puzzles
- **Move Validation**: Real-time checking for Sudoku rule violations
- **Hint System**: Get hints to help solve the puzzle
- **Solution Display**: View the complete solution anytime
- **Intuitive UI**: Clean terminal interface with visual grid formatting

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/greeshmaredddy/sudokogame.git
cd sudokogame
```

## How to Play

Run the game:

```bash
python3 src/sudoku_game.py
```

### Game Controls

1. **Select Difficulty**: Choose from Easy (1), Medium (2), or Hard (3)

2. **Place Numbers**: Enter commands in the format: `row col number`
   - Example: `5 3 7` places 7 at row 5, column 3
   - Rows and columns are numbered 1-9

3. **Available Commands**:
   - `h` - Get a hint
   - `s` - Show the complete solution
   - `0` - Clear a cell (e.g., `5 3 0` clears row 5, column 3)
   - `m` - Return to main menu

### Rules

Standard Sudoku rules apply:
- Each row must contain digits 1-9 without repetition
- Each column must contain digits 1-9 without repetition
- Each 3×3 box must contain digits 1-9 without repetition

The game validates your moves and warns you of any conflicts.

## Examples

**Starting the game:**
```
$ python3 src/sudoku_game.py
```

**Playing:**
```
  1 2 3 │ 4 5 6 │ 7 8 9
  ──────┼───────┼──────
1 . . 3 │ . 2 . │ 6 . .
2 9 . . │ 3 . 5 │ . . 1
3 . . 1 │ 8 . 6 │ 4 . .
  ──────┼───────┼──────
4 . . 8 │ 1 . 2 │ . . 4
5 7 . . │ . . . │ . . 8
6 . . 6 │ 4 . 7 │ 2 . .
  ──────┼───────┼──────
7 . . 4 │ 2 . 1 │ 5 . .
8 6 . . │ 5 . 3 │ . . 2
9 . . 2 │ . 6 . │ 3 . .

Commands:
  Place: <row> <col> <num>  (e.g., 1 1 5)
  Hint:  h
  Show:  s (show solution)
  Clear: <row> <col> 0
  Menu:  m

Enter command: 1 1 5
✓ Placed 5 at (1, 1)
```

## How It Works

- **Puzzle Generation**: The game uses backtracking to generate valid, complete Sudoku solutions, then removes numbers to create puzzles
- **Validation**: Move validation checks row, column, and 3×3 box constraints
- **Hints**: The hint system randomly selects an empty cell from the solution
- **Win Detection**: The game detects when the puzzle is completely and correctly solved

## Project Structure

```
sudokogame/
├── src/
│   └── sudoku_game.py    # Main game implementation
├── README.md             # This file
├── GAMEPLAY.md           # Detailed gameplay guide
└── LICENSE
```

## License

This project is open source. Feel free to use and modify as needed.

## Troubleshooting

**Game won't start**
- Ensure Python 3.6+ is installed: `python3 --version`
- Make sure you're running from the project root directory

**Terminal looks weird**
- Try resizing your terminal window to at least 80 columns wide and 24 rows tall

**Can't place numbers**
- Remember: You cannot modify the original clues (numbers already on the board)
- Use format: `row col number` (e.g., `5 3 7`)

## Future Enhancements

- [ ] Save/Load game progress
- [ ] Timer and difficulty statistics
- [ ] Difficulty rating for generated puzzles
- [ ] Multiple solve strategies as hints
- [ ] Undo/Redo functionality
- [ ] Web-based version

---

Enjoy playing and solving Sudoku puzzles!
