#!/usr/bin/env python3
"""
Sudoku Game - Play Sudoku in the Terminal
A complete interactive Sudoku game with board generation and validation.
"""

import random
from typing import List, Tuple, Optional
from copy import deepcopy


class SudokuGame:
    """Complete Sudoku game implementation with board generation and solving."""
    
    def __init__(self, difficulty: str = "medium"):
        """
        Initialize a new Sudoku game.
        
        Args:
            difficulty: "easy" (40 clues), "medium" (32 clues), "hard" (24 clues)
        """
        self.difficulty = difficulty
        self.clues = {"easy": 40, "medium": 32, "hard": 24}[difficulty]
        self.solution = self._generate_solution()
        self.board = self._create_puzzle()
        self.original_board = deepcopy(self.board)
        self.moves = []
        
    def _generate_solution(self) -> List[List[int]]:
        """Generate a valid completed Sudoku solution."""
        board = [[0] * 9 for _ in range(9)]
        self._fill_board(board)
        return board
    
    def _fill_board(self, board: List[List[int]]) -> bool:
        """Recursively fill the board with valid numbers."""
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    
                    for num in numbers:
                        if self._is_valid(board, row, col, num):
                            board[row][col] = num
                            if self._fill_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    def _is_valid(self, board: List[List[int]], row: int, col: int, num: int) -> bool:
        """Check if placing num at (row, col) is valid."""
        # Check row
        if num in board[row]:
            return False
        
        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def _create_puzzle(self) -> List[List[int]]:
        """Remove numbers from solution to create a puzzle."""
        puzzle = deepcopy(self.solution)
        removed = 0
        
        while removed < (81 - self.clues):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            
            if puzzle[row][col] != 0:
                puzzle[row][col] = 0
                removed += 1
        
        return puzzle
    
    def place_number(self, row: int, col: int, num: int) -> Tuple[bool, str]:
        """
        Place a number on the board.
        
        Args:
            row: 0-8
            col: 0-8
            num: 1-9 (0 to clear)
        
        Returns:
            (success, message)
        """
        # Validate coordinates
        if not (0 <= row <= 8 and 0 <= col <= 8):
            return False, "Invalid coordinates (0-8)"
        
        # Can't modify clue cells
        if self.original_board[row][col] != 0:
            return False, "Cannot modify original clues"
        
        # Clear cell
        if num == 0:
            self.board[row][col] = 0
            self.moves.append((row, col, num))
            return True, "Cell cleared"
        
        # Validate number
        if not (1 <= num <= 9):
            return False, "Number must be 1-9"
        
        # Check validity (allowing duplicates for user input)
        # We'll only validate against the rules
        self.board[row][col] = num
        self.moves.append((row, col, num))
        return True, f"Placed {num} at ({row+1}, {col+1})"
    
    def is_valid_placement(self, row: int, col: int) -> Tuple[bool, str]:
        """Check if current placement at (row, col) violates Sudoku rules."""
        num = self.board[row][col]
        if num == 0:
            return True, "Empty cell"
        
        # Check row
        row_count = sum(1 for c in range(9) if self.board[row][c] == num)
        if row_count > 1:
            return False, f"Duplicate {num} in row {row+1}"
        
        # Check column
        col_count = sum(1 for r in range(9) if self.board[r][col] == num)
        if col_count > 1:
            return False, f"Duplicate {num} in column {col+1}"
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        box_count = sum(
            1 for i in range(box_row, box_row + 3)
            for j in range(box_col, box_col + 3)
            if self.board[i][j] == num
        )
        if box_count > 1:
            return False, f"Duplicate {num} in 3x3 box"
        
        return True, "Valid placement"
    
    def is_solved(self) -> bool:
        """Check if the puzzle is completely and correctly solved."""
        if any(0 in row for row in self.board):
            return False
        
        return self.board == self.solution
    
    def get_hint(self) -> Optional[Tuple[int, int, int]]:
        """Get a hint by returning one cell from the solution."""
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0 and self.original_board[row][col] == 0:
                    return row, col, self.solution[row][col]
        return None
    
    def print_board(self):
        """Print the current game board to the terminal."""
        print("\n  1 2 3 │ 4 5 6 │ 7 8 9")
        print("  ──────┼───────┼──────")
        
        for row in range(9):
            if row != 0 and row % 3 == 0:
                print("  ──────┼───────┼──────")
            
            print(f"{row+1} ", end="")
            for col in range(9):
                if col != 0 and col % 3 == 0:
                    print("│ ", end="")
                
                num = self.board[row][col]
                if num == 0:
                    print(". ", end="")
                else:
                    print(f"{num} ", end="")
            
            print()
        print()
    
    def print_solution(self):
        """Print the solution board."""
        print("\n  1 2 3 │ 4 5 6 │ 7 8 9")
        print("  ──────┼───────┼──────")
        
        for row in range(9):
            if row != 0 and row % 3 == 0:
                print("  ──────┼───────┼──────")
            
            print(f"{row+1} ", end="")
            for col in range(9):
                if col != 0 and col % 3 == 0:
                    print("│ ", end="")
                
                num = self.solution[row][col]
                print(f"{num} ", end="")
            
            print()
        print()


class GameUI:
    """Terminal UI for the Sudoku game."""
    
    def __init__(self):
        self.game: Optional[SudokuGame] = None
    
    def clear_screen(self):
        """Clear the terminal screen."""
        print("\033[2J\033[H", end="")
    
    def print_header(self):
        """Print the game header."""
        print("╔═════════════════════════════════════╗")
        print("║           SUDOKU GAME               ║")
        print("║         Play in Terminal            ║")
        print("╚═════════════════════════════════════╝\n")
    
    def main_menu(self):
        """Display and handle the main menu."""
        while True:
            self.clear_screen()
            self.print_header()
            
            print("1. Easy   (40 clues)")
            print("2. Medium (32 clues)")
            print("3. Hard   (24 clues)")
            print("4. Exit\n")
            
            choice = input("Select difficulty (1-4): ").strip()
            
            if choice == "1":
                self.game = SudokuGame("easy")
                self.play_game()
            elif choice == "2":
                self.game = SudokuGame("medium")
                self.play_game()
            elif choice == "3":
                self.game = SudokuGame("hard")
                self.play_game()
            elif choice == "4":
                print("Thanks for playing! Goodbye!\n")
                break
            else:
                print("Invalid choice. Try again.")
                input("Press Enter to continue...")
    
    def play_game(self):
        """Main game loop."""
        while True:
            self.clear_screen()
            self.print_header()
            
            print(f"Difficulty: {self.game.difficulty.upper()}\n")
            self.game.print_board()
            
            if self.game.is_solved():
                print("🎉 Congratulations! You solved the puzzle!\n")
                input("Press Enter to return to menu...")
                break
            
            print("Commands:")
            print("  Place: <row> <col> <num>  (e.g., 1 1 5)")
            print("  Hint:  h")
            print("  Show:  s (show solution)")
            print("  Clear: <row> <col> 0")
            print("  Menu:  m\n")
            
            command = input("Enter command: ").strip().lower()
            
            if command == "m":
                break
            elif command == "h":
                hint = self.game.get_hint()
                if hint:
                    row, col, num = hint
                    print(f"\n💡 Hint: Position ({row+1}, {col+1}) should be {num}")
                else:
                    print("\n❌ No more hints available!")
                input("Press Enter to continue...")
            elif command == "s":
                print("\nShowing solution:")
                self.game.print_solution()
                input("Press Enter to continue...")
            else:
                parts = command.split()
                if len(parts) == 3:
                    try:
                        row, col, num = int(parts[0]) - 1, int(parts[1]) - 1, int(parts[2])
                        
                        success, msg = self.game.place_number(row, col, num)
                        
                        if success:
                            # Check if placement is valid
                            valid, validation_msg = self.game.is_valid_placement(row, col)
                            if valid:
                                print(f"✓ {msg}")
                            else:
                                print(f"⚠ {msg} - {validation_msg}")
                        else:
                            print(f"✗ {msg}")
                        
                        input("Press Enter to continue...")
                    except (ValueError, IndexError):
                        print("Invalid input. Use format: row col number")
                        input("Press Enter to continue...")
                else:
                    print("Invalid command.")
                    input("Press Enter to continue...")


def main():
    """Entry point for the game."""
    ui = GameUI()
    ui.main_menu()


if __name__ == "__main__":
    main()
