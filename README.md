# 🎮 Sudoku Game - Terminal Edition

A fully functional Sudoku game playable directly in your terminal. Solve randomly generated puzzles with three difficulty levels, real-time validation, and helpful hints.

## Quick Start

```bash
# Clone and run
git clone https://github.com/greeshmaredddy/sudokogame.git
cd sudokogame
python3 src/sudoku_game.py
```

## Features

✨ **Three Difficulty Levels** - Easy, Medium, Hard
✨ **Random Puzzle Generation** - Unique game every time
✨ **Real-Time Validation** - Instant feedback on moves
✨ **Hint System** - Get help when stuck
✨ **Solution Display** - View answers anytime
✨ **Clean Terminal UI** - Beautiful formatting and colors

## Gameplay

```
  1 2 3 │ 4 5 6 │ 7 8 9
  ──────┼───────┼──────
1 . . 3 │ . 2 . │ 6 . .
2 9 . . │ 3 . 5 │ . . 1
3 . . 1 │ 8 . 6 │ 4 . .
  ──────┼───────┼──────
4 . . 8 │ 1 . 2 │ . . 4
...
```

**Commands:**
- Place number: `row col number` (e.g., `5 3 7`)
- Get hint: `h`
- Show solution: `s`
- Clear cell: `row col 0`
- Return to menu: `m`

## Requirements

- Python 3.6+
- No external dependencies

## Full Documentation

- [📖 Detailed Gameplay Guide](GAMEPLAY.md) - Complete instructions and tips
- [🐍 Game Code](src/sudoku_game.py) - Well-commented source code

## How It Works

The game implements:
- **Backtracking Algorithm**: Generates valid Sudoku solutions
- **Puzzle Generation**: Removes numbers to create solvable puzzles
- **Constraint Validation**: Checks row, column, and 3×3 box rules
- **Interactive Terminal UI**: Menu system and game controls

## Project Structure

```
sudokogame/
├── src/sudoku_game.py     # Main game implementation
├── README.md              # This file
├── GAMEPLAY.md            # Detailed guide
└── LICENSE
```

## License

Open source - use and modify freely.

---

**Ready to play?** Run `python3 src/sudoku_game.py` to start!
